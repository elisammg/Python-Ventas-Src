from django import forms
from .models import *


class FormUsuarios(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = [           
        'Nombre',
        'Usuario',
        'Password',
        'Rol',
        ]
        labels = {               
            'Nombre':        'Nombre',
            'Usuario':     'Usuario',
            'Password':     'Password',
            'Rol':    'Rol',
        }

        widgets = {

            'Nombre'         :forms.TextInput(attrs={'class':'form-control'}),
            'Usuario'      :forms.TextInput(attrs={'class':'form-control'}),
            'Password'      :forms.PasswordInput(attrs={'class':'form-control'}),   
            'Rol'       :forms.Select(attrs={'class':'form-control'})
        }


class FormLogin(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = [         
        'Usuario',
        'Password',
        ]
        labels = {               
            'Usuario':     'Usuario',
            'Password':     'Password',
        }

        widgets = {

            'Usuario'      :forms.TextInput(attrs={'class':'form-control'}),
            'Password'      :forms.PasswordInput(attrs={'class':'form-control'}),   
        }





class FormVentas(forms.ModelForm):

    class Meta:
        model = Ventas
        fields = [           
            #'Codigo_Venta',
            'Tipo_Venta',
        #    'Fabricante',
            'Vendedor'
        ]
        labels = {               
            #'Codigo_Venta': 'Codigo_Venta',
            'Tipo_Venta':   'Tipo de Venta',
        #    'Fabricante':    'Fabricante',
            'Vendedor':     'Vendedor',
        }
        widgets = {     
           # 'Codigo_Venta' :forms.HiddenInput(attrs={'class':'form-control'}), 
            'Tipo_Venta'  :forms.Select(attrs={'class':'form-control'}),
         #   'Fabricante'  :forms.Select(attrs={'class':'form-control'}),            
            'Vendedor'  :forms.Select(attrs={'class':'form-control'}),
        }

#Factura Cliente Individual
class FormFacturaI(forms.ModelForm):

    class Meta:
        model = FACTURA
        fields = [           
            'Nombre_cliente',
            'Nit',
            #'Total',
            #'Estado'
        ]
        labels = {               
            'Nombre_cliente': 'Nombre Cliente',
            'Nit': 'Nit',
            #'Total':    'Total',
            #'Estado':   'Estado'
        }

        widgets = {
            'Nombre'   :forms.TextInput(attrs={'class':'form-control'}),
            'Nit'   :forms.TextInput(attrs={'class':'form-control'}),
            #'Total'     :forms.NumberInput(attrs={'class':'form-control'}),
            #'Estado'    :forms.TextInput(attrs={'class':'form-control'}),
        }

#Factura Cliente Registrado
class FormFacturaR(forms.ModelForm):

    class Meta:
        model = FACTURA
        fields = [           
            'Cliente',
           # 'Total',
           # 'Estado'
        ]
        labels = {               
            'Cliente':  'Cliente',
            #'Total':    'Total',
            #'Estado':   'Estado'
        }

        widgets = {
            'Cliente'   :forms.Select(attrs={'class':'form-control'}),
            #'Total'     :forms.NumberInput(attrs={'class':'form-control'}),
            #'Estado'    :forms.Select(attrs={'class':'form-control'}),
        }







class FormDVenta(forms.ModelForm):

    class Meta:
        model = Detalle_Venta

        fields = [           
        #'Venta',
        'Repuesto',
        'Cantidad',
        #'Sub_Total',
      #  'Factura'
        ]
        labels = {               
           # 'Venta':        'Venta',
            'Repuesto':     'Repuesto',
            'Cantidad':     'Cantidad',
          #  'Sub_Total':    'Sub Total',
      #      'Factura':      'Factura'
        }

        widgets = {

            #'Venta'         :forms.Select(attrs={'class':'form-control'}),
            #'Repuesto':     forms.ModelChoiceField(queryset=REPUESTOS.objects.all()),
            'Repuesto'      :forms.Select(attrs={'class':'form-control'}),
            'Cantidad'      :forms.NumberInput(attrs={'class':'form-control'}),
          #  'Sub_Total'     :forms.HiddenInput(attrs={'class':'form-control'}),   
      #      'Factura'       :forms.Select(attrs={'class':'form-control'})
        }


class Prueba(forms.Form):
    Repuesto = forms.ModelChoiceField(queryset=REPUESTOS.objects.filter(Stock__gt=0))
    Cantidad = forms.IntegerField()



class PruebaDos(forms.Form):
    Cliente = forms.ModelChoiceField(queryset=Clientes.objects.filter(estado = 'Activo'))

class PruebaTres(forms.Form):
    Cliente = forms.ModelChoiceField(queryset=Clientes.objects.filter(estado = 'Activo', TIPO_ID = 1))
