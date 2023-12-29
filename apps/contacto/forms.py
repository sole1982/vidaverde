# forms.py
from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    OPCIONES_CONSULTA = [
        ('informacion_general', 'Información General'),
        ('biodiversidad', 'Biodiversidad'),
        ('reciclaje', 'Reciclaje'),
        ('cambio_climatico', 'Cambio Climático'),
        ('vida_verde', 'Vida Verde'),
        ('energias_renovables', 'Energías Renovables'),
        ('huerta_familiar', 'Huerta Familiar'),
        ('permacultura', 'Permacultura'),
        ('educacion_ambiental', 'Educación Ambiental'),
    ]

    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    consulta = forms.ChoiceField(choices=OPCIONES_CONSULTA, widget=forms.Select(attrs={'class': 'form-control'}))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(ContactoForm, self).__init__(*args, **kwargs)
        self.fields['consulta'].widget.choices[0] = ('', 'Seleccione una opción...')

    class Meta:
        model = Contacto
        fields = ['nombre_apellido', 'email', 'asunto', 'mensaje']
