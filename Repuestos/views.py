from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView # new
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy # new
from .models import *
from .forms import *

# Create your views here.

#REPUESTOS
#Formulario crear repuestos
class CreateRepuesto(CreateView): # new
    model = REPUESTOS
    form_class = FormRepuesto
    template_name = 'newrepuesto.html'
    success_url ="/repuestos/listado"

    #agregar acceso a administrador
    def get(self, request, *args, **kwargs):
        if request.session['misesion'] != '':
            #if request.session['tipo'] == 'Administrador':
             self.object = None
             form_class = self.get_form_class()
             form = self.get_form(form_class)
             return self.render_to_response(
                 self.get_context_data(form=form))
           # else:
               # return render(request, 'login.html')
        else:
            return render(request, 'login.html')


#lista de repuestos
def ListaRepuestos(request):
    if request.method == "GET":
        if request.session['misesion'] != '':
            repuestos = REPUESTOS.objects.all()
            return render(request, 'repuestos.html', {'repuestos': repuestos})
        else:
            return render(request, 'login.html')



#Editar repuestos
class RepuestoUpdate(UpdateView): 
    # specify the model you want to use 
    model = REPUESTOS 
    form_class = FormRepuesto
    template_name = 'editrepuesto.html'
    success_url ="/repuestos/listado"

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


#Eliminar repuestos
class RepuestoDelete(DeleteView): 
    # specify the model you want to use 
    model = REPUESTOS 
    template_name = 'deletecliente.html'
    success_url ="/repuestos/listado"



#VEHICULOS
#Formulario crear vehiculos
class CreateVehiculo(CreateView): # new
    model = VEHICULO
    form_class = FormVehiculo
    template_name = 'newvehiculo.html'
    success_url ="/repuestos/vehiculos"



#lista de vehiculos
def ListaVehiculo(request):
    if request.method == "GET":
        if request.session['misesion'] != '':
            vehiculos = VEHICULO.objects.all()
            return render(request, 'vehiculos.html', {'vehiculos': vehiculos})
        else:
            return render(request, 'login.html')



#Editar vehiculos
class VehiculoUpdate(UpdateView): 
    # specify the model you want to use 
    model = VEHICULO 
    form_class = FormVehiculo
    template_name = 'editvehiculo.html'
    success_url ="/repuestos/vehiculos"

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


#Eliminar vehiculos
class VehiculoDelete(DeleteView): 
    # specify the model you want to use 
    model = VEHICULO 
    template_name = 'deletevehiculo.html'
    success_url ="/repuestos/vehiculos"

