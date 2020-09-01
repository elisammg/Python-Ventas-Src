from django import forms
from .models import *

class FormularioTipo(forms.ModelForm): 

    class Meta:
        model = Tipo
        fields = [           
            #'rol', 
      
            'nombre',        
            'Descuento',            
        ]
        labels = {               
            #'rol'                   :'Tipo de Cliente',         

            'nombre'            :'Nombre',
            'Descuento'         :'Descuento',  
                      
        }
        widgets = {
            #'rol'                   :forms.Select(attrs={'class':'form-control'}),        
            'nombre'                :forms.Select(attrs={'class':'form-control'}),        
            'Descuento'             :forms.TextInput(attrs={'class':'form-control'}), 
        }



class FormularioCliente(forms.ModelForm): 

    class Meta:
        model = Clientes
        fields = [           
            #'rol', 
      
            'nombre',
            'nit',
            'email', 
            'telefono',        
            'patente',            
            'fecha_inicio',
            'fecha_fin', 
            'TIPO_ID',            
        ]
        labels = {               
            #'rol'               :'Cliente',         

            'nombre'            :'Nombre',
            'nit'               :'Nit',         
            'email'             :'Email',
            'telefono'          :'Telefono',
            'patente'           :'Patente',            
            'fecha_inicio'      :'Fecha de inicio',         
            'fecha_fin'       :'Fecha final',
            'TIPO_ID'           :'Tipo', 

                      
        }
        widgets = {
            #'rol'                   :forms.Select(attrs={'class':'form-control'}),        
            'nombre'                :forms.TextInput(attrs={'class':'form-control'}),
            'nit'                   :forms.TextInput(attrs={'class':'form-control'}),
            'email'                 :forms.TextInput(attrs={'class':'form-control'}),
            'telefono'              :forms.TextInput(attrs={'class':'form-control'}),         
            'patente'               :forms.ClearableFileInput(),  
            'fecha_inicio'          :forms.DateInput(attrs={'class':'form-control'}),
            'fecha_fin'           :forms.DateInput(attrs={'class':'form-control'}), 
            'TIPO_ID'               :forms.Select(attrs={'class':'form-control'}), 
        }