from django import forms
from .models import *

class FormularioFabrica(forms.ModelForm): 
    class Meta:
        model = FABRICA
        fields = [           
            #'rol', 
      
            'IP',
            'Puerto',
            'Nombre', 
            'Password'              
        ]
        labels = {               
            #'rol'                   :'Tipo de Cliente',         

            'IP'            :'IP',
            'Puerto'        :'Puerto',         
            'Nombre'        :'Nombre',        
            'Password'        :'Password',  
                      
        }
        widgets = {
            #'rol'                   :forms.Select(attrs={'class':'form-control'}), 
            'IP'                :forms.TextInput(attrs={'class':'form-control'}),
            'Puerto'            :forms.TextInput(attrs={'class':'form-control'}),         
            'Nombre'            :forms.TextInput(attrs={'class':'form-control'}),
            'Password'            :forms.TextInput(attrs={'class':'form-control'}), 
        }


class FormularioPedidos(forms.ModelForm): 
    class Meta:
        model = Pedidos_Fabrica
        fields = [           
            #'rol', 
      
            #'Codigo_Fabrica',
            #'Fecha_Pedido',
            #'Fecha_Recepcion',
            #'Total',
            #'Estado',

        ]
        labels = {               
            #'rol'                   :'Tipo de Cliente',         

            #'Codigo_Fabrica'            :'Codigo Fabrica',
            #'Fecha_Pedido'              :'Fecha pedido',         
            #'Fecha_Recepcion'           :'Fecha recepcion', 
            #'Total'                     :'Total',  
            #'Estado'                    :'Estado', 
                      
        }
        widgets = {
            #'rol'                   :forms.Select(attrs={'class':'form-control'}),
            #'Codigo_Fabrica'            :forms.Select(attrs={'class':'form-control'}), 
            #'Fecha_Pedido'              :forms.DateInput(attrs={'class':'form-control'}),
            #'Fecha_Recepcion'           :forms.DateInput(attrs={'class':'form-control'}),         
            #'Total'                     :forms.NumberInput(attrs={'class':'form-control'}),       
            #'Estado'                    :forms.Select(attrs={'class':'form-control'}), 

        }



class FormularioRecepcion(forms.ModelForm): 


    class Meta:
        model = Recepcion_Fabrica
        fields = [           
            #'rol', 
      
            'Codigo_Pedido',
            #'Codigo_ProductoFab',
            'Precio_lista',
            'Numero_De_Parte',
            'Nombre_Producto',
            'Fecha_Pedido',
            'Fecha_Recepcion',
            'Cantidad',
            'Precio_Fabricante',
            'Total',
            #'Pedido_Fabrica',

        ]
        labels = {               
            #'rol'                   :'Tipo de Cliente',         

            'Codigo_Pedido'            :'Codigo Fabrica',
            #'Codigo_ProductoFab'       :'Codigo Producto Fabrica',         
            'Precio_lista'             :'Precio de lista', 
            'Numero_De_Parte'          :'Numero de Parte',  
            'Nombre_Producto'          :'Nombre de producto', 
            'Fecha_Pedido'             :'Fecha pedido', 
            'Fecha_Recepcion'          :'Fecha recepcion', 
            'Cantidad'                 :'Cantidad', 
            'Precio_Fabricante'        :'Precio fabricante', 
            'Total'                    :'Total', 
            #'Pedido_Fabrica'           :'Pedido_Fabrica', 
                      
        }
        widgets = {
            #'rol'                   :forms.Select(attrs={'class':'form-control'}),
            'Codigo_Pedido'                 :forms.TextInput(attrs={'class':'form-control'}), 
            #'Codigo_ProductoFab'            :forms.NumberInput(attrs={'class':'form-control'}),
            'Precio_lista'                  :forms.NumberInput(attrs={'class':'form-control'}),         
            'Numero_De_Parte'               :forms.NumberInput(attrs={'class':'form-control'}),       
            'Nombre_Producto'               :forms.TextInput(attrs={'class':'form-control'}),    
            'Fecha_Pedido'                  :forms.DateInput(attrs={'class':'form-control'}),    
            'Fecha_Recepcion'               :forms.DateInput(attrs={'class':'form-control'}),    
            'Cantidad'                      :forms.NumberInput(attrs={'class':'form-control'}),    
            'Precio_Fabricante'             :forms.NumberInput(attrs={'class':'form-control'}),    
            'Total'                         :forms.NumberInput(attrs={'class':'form-control'}),    
            #'Pedido_Fabrica'                :forms.Select(attrs={'class':'form-control'}), 

        }




class FormularioDetallePedido(forms.ModelForm): 
    class Meta:
        model = Detalle_Pedido
        fields = [           
            #'rol', 
            'Productos',
            'Cantidad',
            'Fabricante', 
            #'Sub_Total',
            #'Pedidofk'             
        ]
        labels = {               
            #'rol'                   :'Tipo de Cliente',         

            'Productos'         :'Producto',
            'Cantidad'          :'Cantidad',         
            'Fabricante'        :'Fabricante',        
            #'Sub_Total'         :'Sub total', 
            #'Pedidofk':         'Pedido', 
                      
        }
        widgets = {
            #'rol'                   :forms.Select(attrs={'class':'form-control'}), 
            'Productos'                :forms.TextInput(attrs={'class':'form-control'}),
            'Cantidad'            :forms.TextInput(attrs={'class':'form-control'}),         
            'Fabricante'            :forms.Select(attrs={'class':'form-control'}),
            #'Sub_Total'            :forms.TextInput(attrs={'class':'form-control'}),
            #'Pedidofk'            :forms.Select(attrs={'class':'form-control'}), 
        }
