from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView # new
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy # new
from django.http import HttpResponse
from django.db import connection
from .models import *
from .forms import *

# Create your views here.
def Modificar_Suscripcion(self):
    with connection.cursor() as cursor:
        cursor.callproc('Modificar_Suscripcion')
    return HttpResponse('Hola')

#Formulario crear cliente
class CreateCliente(CreateView): # new
    model = Clientes
    form_class = FormularioCliente
    template_name = 'newcliente.html'
    success_url ="/clientes/listado"





#lista de clientes
def ListaClientes(request):
    #clientes = Clientes.objects.all()
    #return render(request, 'clientes.html', {'clientes': clientes})
    if request.method == "GET":
        if request.session['misesion'] != '':
            clientes = Clientes.objects.all()
            return render(request, 'clientes.html', {'clientes': clientes})
        else:
            return render(request, 'login.html')



#Editar Clientes
class ClientesUpdate(UpdateView): 
    # specify the model you want to use 
    model = Clientes 
    form_class = FormularioCliente
    template_name = 'editarcliente.html'
    success_url ="/clientes/listado"
    
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


#Eliminar Clientes
class ClienteDelete(DeleteView): 
    # specify the model you want to use 
    model = Clientes 
    template_name = 'deletecliente.html'
    success_url ="/clientes/listado"
