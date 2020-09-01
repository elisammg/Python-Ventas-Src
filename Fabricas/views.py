from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, CreateView # new
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy # new
from rest_framework import viewsets
from .serializers import *
import urllib.request as ur
from django.db import connection
import json
from .models import *
from .forms import *



# Create your views here.

global Numero 
Numero = 15

#global ListaPedidos 
#ListaPedidos = []


#Formulario crear cliente
class CreateFabrica(CreateView): # new
    model = FABRICA
    form_class = FormularioFabrica
    template_name = 'newfabrica.html'
    success_url ="/fabricas/listado"

#agregar acceso a administrador
    def get(self, request, *args, **kwargs):
        if request.session['misesion'] != '':
            #if request.session['tipo'] == 'Administrador':
           self.object = None
           form_class = self.get_form_class()
           form = self.get_form(form_class)
           return self.render_to_response(
               self.get_context_data(form=form))
            #else:
             #   return render(request, 'login.html')
        else:
            return render(request, 'login.html')


#lista de clientes
def ListaFabricas(request):
    fabricas = FABRICA.objects.all()
    return render(request, 'fabricas.html', {'fabricas': fabricas})



#Editar FABRICAS
class FabricasUpdate(UpdateView): 
    # specify the model you want to use 
    model = FABRICA
    form_class = FormularioFabrica
    template_name = 'editarfabrica.html'
    success_url ="/fabricas/listado"

#agregar acceso a administrador
    def get(self, request, *args, **kwargs):
        if request.session['misesion'] != '':
            if request.session['tipo'] == 'Administrador':
               self.object = None
               form_class = self.get_form_class()
               form = self.get_form(form_class)
               return self.render_to_response(
                   self.get_context_data(form=form))
            else:
                return render(request, 'login.html')
        else:
            return render(request, 'login.html')


#Eliminar FABRICAS
class FabricaDelete(DeleteView): 
    # specify the model you want to use 
    model = FABRICA
    template_name = 'deletefabrica.html'
    success_url ="/fabricas/listado"


def CrearPedido(request):
    if request.method=='POST':
        #if request.session['misesion'] != '':
         #   if request.session['tipo'] == 'Administrador':
        form = FormularioPedidos(request.POST)
        if form.is_valid():
            #producto_fk = Producto.objects.get(codigoProducto= form.cleaned_data['Productos'])
            Pedidoid = form.save(commit = True)
            request.session['id_pedido'] = Pedidoid.Codigo_Pedido
            print(request.session['id_pedido'])
            mipedido=Pedidos_Fabrica(
                Codigo_Fabrica = None,
                Fecha_Recepcion = None, 
                Total = None,
                Estado  = 'enviado'
            )
            #mipedido.save()
            return HttpResponseRedirect('detallepedido')
               #else:
                    #return render(request, 'login.html')
        #else:
            #return render(request, 'login.html')
    else:
        form = FormularioPedidos()
    return render(request,'crearpedido.html',{'form':form})



def CrearDetallePedido(request):
    if request.method=='POST':
        form = FormularioDetallePedido(request.POST)
        if form.is_valid():
            #producto_fk = Producto.objects.get(codigoProducto= form.cleaned_data['Productos'])
            pedido_fk = Pedidos_Fabrica.objects.get(Codigo_Pedido = request.session['id_pedido'])
            print(pedido_fk)
            #fabricante_fk=Fabricante.objects.get(Codigo_Fabrica=form.cleaned_data['Fabrica'])
            mipedido=Detalle_Pedido(
                Productos= form.cleaned_data['Productos'],
                Cantidad= form.cleaned_data['Cantidad'],
                Fabricante= form.cleaned_data['Fabricante'], 
                Sub_Total= Numero,
                Pedidofk =pedido_fk
            )
            mipedido.save()
            return HttpResponseRedirect('detallepedido')
    else:
        form = FormularioDetallePedido()
        lista = Detalle_Pedido.objects.filter(Pedidofk = request.session['id_pedido'])
    return render(request,'DPedido.html',{'form':form, 'lista': lista})




def RecepcionFabrica(request):
    if request.method=='GET':
        lista=Recepcion.objects.all()
    return render(request,'Recepcion.html',{'lista':lista})


def pedidosapi(request):
    #urlapi = "http://192.168.1.25:8080/pedidosapi"    
    #responseapi = ur.urlopen(urlapi)
    #apipedidos = json.loads(responseapi.read())
    #print(apipedidos)
    fabricas = FABRICA.objects.all()
    #print(fabricas)
    global ListaPedidos
    ListaPedidos = []
    for fab in fabricas:

        urledit = "http://" + fab.IP + ":" + fab.Puerto + "/pedidosapi"
        #print(urledit)
        #urlapi = "http://192.168.1.25:8080/pedidosapi"
        responseapi = ur.urlopen(urledit)
        apipedidos = json.loads(responseapi.read())
        ListaPedidos.append(apipedidos)
    #print(ListaPedidos)
    return render(request, 'recibirpedido.html', {'ListaPedidos' : ListaPedidos})


def guardarpedido(request, pk):
    if request.method=='GET':
        print(pk)
        pedido = None
        esta = False 
        for lp in ListaPedidos:
            for lp2 in lp:           
                if lp2['id'] == pk:
                    pedido = lp2
                    esta = True
                    break
            if esta == True:                
                break
        if pedido != None:
            recibido = Prueba(
            idfk = pedido['id'],
            fecha_recibido = pedido['fecha_recibido'],
            fecha_entrega = pedido['fecha_entrega'],
            estado = pedido['estado'],
            repuestos = pedido['repuestos'],
            clientes = pedido['clientes'],
            precio_final = pedido['precio_final'],
            cantidad = pedido['cantidad']
            )
            recibido.save()
        else:
            print('vacio')
    return HttpResponse('Guardado Correctamente')



#REST PEDIDOS ENVIAR
class FabricaViewSet(viewsets.ModelViewSet):
    queryset = FABRICA.objects.all()
    serializer_class = FabricaSerializer


class PedidosViewSet(viewsets.ModelViewSet):
    queryset = Pedidos_Fabrica.objects.all()
    serializer_class = PedidosSerializer



class DetalleViewSet(viewsets.ModelViewSet):
    queryset = Detalle_Pedido.objects.all()
    serializer_class = DetalleSerializer



"""def pedidosapi(request):
    #urlapi = "http://192.168.1.25:8080/pedidosapi"    
    #responseapi = ur.urlopen(urlapi)
    #apipedidos = json.loads(responseapi.read())
    #print(apipedidos)
    fabricas = FABRICA.objects.all()
    #print(fabricas)
    global ListaPedidos
    ListaPedidos = []
    for fab in fabricas:

        urledit = "http://" + fab.IP + ":" + fab.Puerto + "/envioapi"
        #print(urledit)
        #urlapi = "http://192.168.1.25:8080/pedidosapi"
        responseapi = ur.urlopen(urledit)
        apipedidos = json.loads(responseapi.read())
        ListaPedidos.append(apipedidos)
    #print(ListaPedidos)
    return render(request, 'recibirpedido.html', {'ListaPedidos' : ListaPedidos})"""

"""def guardarpedido(request, pk):
    if request.method=='GET':
        print(pk)
        pedido = None
        esta = False 
        for lp in ListaPedidos:
            for lp2 in lp:           
                if lp2['id'] == pk:
                    pedido = lp2
                    esta = True
                    break
            if esta == True:                
                break
        if pedido != None:
            recibido = Recepcion_Fabrica(    
            Numero_De_Parte = pedido['numero_de_parte'],
            Nombre_Producto = pedido['nombre_producto'],
            Fecha_Pedido = str(pedido['fecha_recibido']).replace('T06:00:00.000+0000',''),
            Fecha_Recepcion = str(pedido['fecha_entrega']).replace('T06:00:00.000+0000',''),
            Cantidad = str(pedido['cantidad']),
            Precio_Fabricante = str(pedido['precio_fabricante']),
            Precio_lista = str(pedido['precio_fabricante']),
            Total = str(pedido['precio_final'])
            )
            recibido.save()
            with connection.cursor() as cursor:
                cursor.callproc('Repuestos_Insertar', [str(recibido.Numero_De_Parte), str(recibido.Nombre_Producto), str(recibido.Nombre_Producto), str(recibido.Cantidad), str(recibido.Precio_Fabricante), '81', str(pedido['vehiculo_compatible'])])
            return HttpResponse('Funciono')
        else:
            print('vacio')
    return HttpResponse('hola')"""