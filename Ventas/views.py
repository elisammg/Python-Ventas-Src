import os
from django.template import RequestContext
from django.db.models import Sum
from decimal import Decimal
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.db.models import Count
from django.contrib.auth import authenticate
from django.conf.urls import url, include
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView # new
from django.urls import reverse_lazy # new
from .models import *
from .forms import *

# Create your views here.

def prueba(request):
    if request.method == "POST":
        prueba = Prueba(request.POST)
        if prueba.is_valid():
            prueba.save()
    else:
        prueba = Prueba()
    return render(request, 'prueba.html', {'prueba': prueba})



#Formulario crear usuario
def newuser(request):
    if request.method == "POST":
        if request.session['misesion'] != '':
            if request.session['tipo'] == 'Administrador':
                fnewuser = FormUsuarios(request.POST)
                if fnewuser.is_valid():
                    fnewuser.save()
            else:
                return render(request, 'login.html')
        else:
            return render(request, 'login.html')
    else:
        fnewuser = FormUsuarios()
    return render(request, 'newuser.html', {'fnewuser': fnewuser})




def vista_sesion(request):

    if request.method == 'POST':
        form = FormLogin(request.POST)
        if form.is_valid():
            user = form.cleaned_data["Usuario"]
            password =form.cleaned_data["Password"]
            listaUsuarios=Usuario.objects.all()
            esta=0
            usuariosesion=None
            for us in listaUsuarios:
                if user==us.Usuario and password==us.Password:
                    esta=1
                    usuariosesion=us
                    break
                    
            if esta==1:
                mensaje='bienvenido'
                request.session['misesion']= usuariosesion.ID_USUARIO
                sesion = request.session['misesion']
                print (usuariosesion.Rol)
                if usuariosesion.Rol=='Administrador':
                    return HttpResponseRedirect('administrador')
                elif usuariosesion.Rol=='Vendedor':
                    return HttpResponseRedirect('vendedor')
            else:
                mensaje='usuario o contrasenia incorrecta'
                return render(request,'login.html',{'mensaje':mensaje,'form':form})
        else:
            mensaje = '--'
            return render(request,'login.html',{'mensaje':mensaje,'form':form})
    else:
        form = FormLogin()
        return render(request,'login.html',{'form':form})


def vista_administrador(request):
    if request.method == "GET":
        if request.session['misesion'] != '':
            return render(request, 'welcome.html')
        else:
            return render(request, 'login.html')


def vista_vendedor(request):
    if request.method == "GET":
        if request.session['misesion'] != '':
            return render(request, 'welcome.html')
        else:
            return render(request, 'login.html')


def logout(request):
    request.session['misesion']=''
    form = FormLogin()
    return render(request,'login.html',{'form':form})


"""def vista_Ventas(request):

    if request.method=='POST':   
        form1=FormVentas(request.POST)
        form2=FormDVenta(request.POST)
        if 'btnVenta' in request.POST:

            if form1.is_valid():
                #request.session['idventa'] = form1.Codigo_Venta
                model = form1.save(commit=False)
                form1.save() 

        elif 'btnDetalle' in request.POST:
            if form2.is_valid():

                model = form2.save(commit=False)  
                RepuestoVenta = REPUESTOS.objects.get(Nombre = model.Repuesto)
               # print (model.Repuesto)                       
                model.Sub_Total = model.Cantidad * RepuestoVenta.Precio_Venta
                model.save()
        return HttpResponseRedirect('vender')
    else:
        form1=FormVentas()
        form2=FormDVenta()
        #if request.session['idventa'] != None:
         #   if request
        #lista = Detalle_Venta.objects.get(Venta = form2.Venta)
        lista = Detalle_Venta.objects.all()
        return render(request,'Template_Venta.html',{'form1':form1, 'form2':form2, 'lista':lista})"""




#lista de detalles
def listardetalle(request):
    detalles = Detalle_Venta.objects.all()
    return render(request, 'listardetalle.html', {'detalles': detalles})



#Formulario crear orden con tipo de venta
def newventa(request):
    if request.method == "POST":
        fnewventa = FormVentas(request.POST)
        if fnewventa.is_valid():
            venta = fnewventa.save(commit=True)
            request.session['id_venta'] = venta.Codigo_Venta
            fnewventa.save()
            tventa = fnewventa.cleaned_data["Tipo_Venta"]
            if tventa == "Individual":
                return HttpResponseRedirect('individual')
            elif tventa == "Registrado":
                return HttpResponseRedirect('registrado')
            elif tventa == "Credito":
                return HttpResponseRedirect('credito')
            elif tventa == "Futuro":
                return HttpResponseRedirect('futuro')
    else:
        fnewventa = FormVentas()
    return render(request, 'newventa.html', {'fnewventa': fnewventa})


#Vista venta individual
def individual(request):
    findividual=Prueba(request.POST)
    facturaI=FormFacturaI(request.POST)    
    if request.method == "POST":
        if 'btnVentaI' in request.POST:
            if findividual.is_valid():
                print (request.session['id_venta'])
                Ventafk = Ventas.objects.get(Codigo_Venta = request.session['id_venta'])
                Repuestofk = REPUESTOS.objects.get(Nombre = findividual.cleaned_data["Repuesto"])
                midetalle = Detalle_Venta (
                    Venta = Ventafk,
                    Repuesto = Repuestofk,
                    Cantidad = findividual.cleaned_data["Cantidad"],
                    Sub_Total = findividual.cleaned_data["Cantidad"] * Repuestofk.Precio_Venta
                    ) 
                midetalle.save()
            return HttpResponseRedirect('individual')

        elif 'btnFI' in request.POST:
            if facturaI.is_valid():
                print (request.session['id_venta'])
                Ventafki = Ventas.objects.get(Codigo_Venta = request.session['id_venta'])
                Total = Detalle_Venta.objects.filter(Venta = request.session['id_venta']).aggregate(Sum('Sub_Total'))
                TotalI = Total['Sub_Total__sum']
                print(Total['Sub_Total__sum'])
                mifactura = FACTURA (
                    Venta = Ventafki,
                    #componer total  {'Sub_Total__sum': Decimal('150')}
                    Total =  TotalI,
                    Estado = "Cancelado",
                    Nombre_cliente = facturaI.cleaned_data["Nombre_cliente"],
                    Nit = facturaI.cleaned_data["Nit"]
                    ) 
                mifactura.save()
            return HttpResponseRedirect('individual')
    else:
        findividual = Prueba()
        facturaI = FormFacturaI()
        lista = Detalle_Venta.objects.filter(Venta = request.session['id_venta'])
        facturas = FACTURA.objects.filter(Venta = request.session['id_venta'])
    return render(request, 'ventaindividual.html', {'findividual': findividual, 'lista': lista, 'facturaI': facturaI, 'facturas': facturas})


#Venta registrado
def registrado(request):
    fregistro=Prueba(request.POST)
    facturaR=PruebaDos(request.POST)    
    if request.method == "POST":
        if 'btnVentaR' in request.POST:
            if fregistro.is_valid():
                print (request.session['id_venta'])
                Ventafk = Ventas.objects.get(Codigo_Venta = request.session['id_venta'])
                Repuestofk = REPUESTOS.objects.get(Nombre = fregistro.cleaned_data["Repuesto"])
                midetalle = Detalle_Venta (
                    Venta = Ventafk,
                    Repuesto = Repuestofk,
                    Cantidad = fregistro.cleaned_data["Cantidad"],
                    Sub_Total = fregistro.cleaned_data["Cantidad"] * Repuestofk.Precio_Venta
                    ) 
                midetalle.save()
            return HttpResponseRedirect('registrado')

        elif 'btnFR' in request.POST:
            if facturaR.is_valid():
                print (request.session['id_venta'])
                Ventafki = Ventas.objects.get(Codigo_Venta = request.session['id_venta'])
                TipoCliente = Clientes.objects.get(nombre = facturaR.cleaned_data["Cliente"])
                Tipos = Tipo.objects.get(nombre = TipoCliente.TIPO_ID)
                print(Tipos)
                Total = Detalle_Venta.objects.filter(Venta = request.session['id_venta']).aggregate(Sum('Sub_Total'))
                TotalI = Total['Sub_Total__sum'] 
                print(Total['Sub_Total__sum'])
                if Tipos.nombre == 'taller':
                    TotalT = float(float(TotalI) * float(0.9))
                    mifactura = FACTURA (
                        Venta = Ventafki,
                        #componer total  {'Sub_Total__sum': Decimal('150')}
                        Total =  TotalT,
                        Estado = "Cancelado",
                        Cliente = facturaR.cleaned_data["Cliente"],
                        ) 
                    mifactura.save()
                elif Tipos.nombre == 'mayorista':
                    TotalM = float(float(TotalI) * float(0.8))
                    mifactura = FACTURA (
                        Venta = Ventafki,
                        #componer total  {'Sub_Total__sum': Decimal('150')}
                        Total =  TotalM,
                        Estado = "Cancelado",
                        Cliente = facturaR.cleaned_data["Cliente"],
                        ) 
                    mifactura.save()
            return HttpResponseRedirect('registrado')
    else:
        fregistro = Prueba()
        facturaR = PruebaDos()
        lista = Detalle_Venta.objects.filter(Venta = request.session['id_venta'])
        facturas = FACTURA.objects.filter(Venta = request.session['id_venta'])
    return render(request, 'ventaregistrado.html', {'fregistro': fregistro, 'lista': lista, 'facturaR': facturaR, 'facturas': facturas})


def credito(request):
    fregistro=Prueba(request.POST)
    facturaR=PruebaDos(request.POST)    
    if request.method == "POST":
        if 'btnVentaR' in request.POST:
            if fregistro.is_valid():
                print (request.session['id_venta'])
                Ventafk = Ventas.objects.get(Codigo_Venta = request.session['id_venta'])
                Repuestofk = REPUESTOS.objects.get(Nombre = fregistro.cleaned_data["Repuesto"])
                midetalle = Detalle_Venta (
                    Venta = Ventafk,
                    Repuesto = Repuestofk,
                    Cantidad = fregistro.cleaned_data["Cantidad"],
                    Sub_Total = fregistro.cleaned_data["Cantidad"] * Repuestofk.Precio_Venta
                    ) 
                midetalle.save()
            return HttpResponseRedirect('credito')

        elif 'btnFR' in request.POST:
            if facturaR.is_valid():
                print (request.session['id_venta'])
                Ventafki = Ventas.objects.get(Codigo_Venta = request.session['id_venta'])
                Total = Detalle_Venta.objects.filter(Venta = request.session['id_venta']).aggregate(Sum('Sub_Total'))
                TotalI = Total['Sub_Total__sum']
                print(Total['Sub_Total__sum'])
                mifactura = FACTURA (
                    Venta = Ventafki,
                    #componer total  {'Sub_Total__sum': Decimal('150')}
                    Total =  TotalI,
                    Estado = "Cancelado",
                    Cliente = facturaR.cleaned_data["Cliente"],
                    ) 
                mifactura.save()
            return HttpResponseRedirect('credito')

        elif 'btnemail' in request.POST:
            elmensaje = 'Pagos Pendientes'
            send_mail(
            'Pagos Pendientes',
            elmensaje,
            'elisamargarita.2899@gmail.com',
            ['elisamargarita.2899@gmail.com'],
            fail_silently=True,)
        return HttpResponseRedirect('credito')
    else:
        fregistro = Prueba()
        facturaR = PruebaDos()
        lista = Detalle_Venta.objects.filter(Venta = request.session['id_venta'])
        facturas = FACTURA.objects.filter(Venta = request.session['id_venta'])
    return render(request, 'ventacredito.html', {'fregistro': fregistro, 'lista': lista, 'facturaR': facturaR, 'facturas': facturas})


def futuro(request):
    fregistro=FormDVenta(request.POST)
    facturaR=PruebaDos(request.POST)    
    if request.method == "POST":
        if 'btnVentaR' in request.POST:
            if fregistro.is_valid():
                print (request.session['id_venta'])
                Ventafk = Ventas.objects.get(Codigo_Venta = request.session['id_venta'])
                Repuestofk = REPUESTOS.objects.get(Nombre = fregistro.cleaned_data["Repuesto"])
                midetalle = Detalle_Venta (
                    Venta = Ventafk,
                    Repuesto = Repuestofk,
                    Cantidad = fregistro.cleaned_data["Cantidad"],
                    Sub_Total = fregistro.cleaned_data["Cantidad"] * Repuestofk.Precio_Venta
                    ) 
                midetalle.save()
            return HttpResponseRedirect('futuro')

        elif 'btnFR' in request.POST:
            if facturaR.is_valid():
                print (request.session['id_venta'])
                Ventafki = Ventas.objects.get(Codigo_Venta = request.session['id_venta'])
                Total = Detalle_Venta.objects.filter(Venta = request.session['id_venta']).aggregate(Sum('Sub_Total'))
                TotalI = Total['Sub_Total__sum']
                print(Total['Sub_Total__sum'])
                mifactura = FACTURA (
                    Venta = Ventafki,
                    #componer total  {'Sub_Total__sum': Decimal('150')}
                    Total =  TotalI,
                    Estado = "Activo",
                    Cliente = facturaR.cleaned_data["Cliente"],
                    ) 
                mifactura.save()
            return HttpResponseRedirect('futuro')
    else:
        fregistro = FormDVenta()
        facturaR = PruebaTres()
        lista = Detalle_Venta.objects.filter(Venta = request.session['id_venta'])
        facturas = FACTURA.objects.filter(Venta = request.session['id_venta'])
    return render(request, 'ventafuturo.html', {'fregistro': fregistro, 'lista': lista, 'facturaR': facturaR, 'facturas': facturas})

