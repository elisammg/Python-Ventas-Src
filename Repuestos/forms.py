from django import forms
from .models import *

class FormVehiculo(forms.ModelForm):

    class Meta:
        model = VEHICULO
        fields = [           
            #'rol',
            'Marca',
            'Linea',
            'Anio',         
            'Codigo_Universal'
        ]
        labels = {               
            #'rol'                   :'Tipo de Usuario',         
            'Marca'                 :'Marca',
            'Linea'                 :'Linea',
            'Anio'                  :'Anio',         
            'Codigo_Universal'      :'Codigo_Universal', 
        }
        widgets = {
            #'rol'                   :forms.Select(attrs={'class':'form-control'}),        
            'Marca'                 :forms.TextInput(attrs={'class':'form-control'}),       
            'Linea'                 :forms.TextInput(attrs={'class':'form-control'}),
            'Anio'                  :forms.TextInput(attrs={'class':'form-control'}),
            'Codigo_Universal'      :forms.TextInput(attrs={'class':'form-control'}),   
        }

class FormRepuesto(forms.ModelForm):

    class Meta:
        model = REPUESTOS
        fields = [           
            #'rol',
            #'Precio_De_Lista',
            'Modelo_De_Parte',
            'Nombre',         
            'Descripcion',
            'Vehiculo_Compatible',
            'Stock',
            'Fabrica',
            'Precio_Fabricante',
            'Precio_Venta'
        ]
        labels = {               
           # 'Precio_De_Lista':      'Precio de Lista',
            'Modelo_De_Parte':      'Modelo de Parte',
            'Nombre':               'Nombre',         
            'Descripcion':          'Descripcion',
            'Vehiculo_Compatible':  'Vehiculo Compatible',
            'Stock':                'Stock',
            'Fabrica':              'Fabrica',
            'Precio_Fabricante':    'Precio de Fabricante',
            'Precio_Venta':         'Precio de Venta'
        }
        widgets = {
           # 'Precio_De_Lista'      :forms.NumberInput(attrs={'class':'form-control'}),
            'Modelo_De_Parte'      :forms.NumberInput(attrs={'class':'form-control'}),
            'Nombre'               :forms.TextInput(attrs={'class':'form-control'}),         
            'Descripcion'          :forms.Textarea(attrs={'class':'form-control'}),
            'Vehiculo_Compatible'  :forms.Select(attrs={'class':'form-control'}),
            'Stock'                :forms.NumberInput(attrs={'class':'form-control'}),
            'Fabrica'              :forms.Select(attrs={'class':'form-control'}),
            'Precio_Fabricante'    :forms.NumberInput(attrs={'class':'form-control'}),
            'Precio_Venta'         :forms.NumberInput(attrs={'class':'form-control'}),
        }