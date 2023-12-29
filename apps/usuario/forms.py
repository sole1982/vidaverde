from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django import forms
from apps.posts.models import Comentario, Post, Categoria
from django.contrib.auth import authenticate, login
from apps.posts.models import Comentario, Post, Categoria

class RegistroUsuarioForm(UserCreationForm):


    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'email', 'imagen']

        def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)
           self.use_required_attribute = False


    class LoginForm(forms.Form):
        username = forms.CharField(label = 'Nombre de usuario')
        password = forms.CharField(label='Contraseña', widget= forms.PasswordInput)

        def login(self, request):
            username = self.cleaned_data.get('username')
            password = self.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login (request, user)