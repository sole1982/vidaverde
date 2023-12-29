from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import ContactoForm  # Asegúrate de importar tu formulario
from django.conf import settings

class ContactoUsuario(CreateView):
    template_name = 'contacto/contacto.html'
    form_class = ContactoForm
    success_url = reverse_lazy('apps.contacto:contacto')

    def form_valid(self, form):
      try:
        # Obtén los datos del formulario
         nombre = form.cleaned_data['nombre']
         apellido = form.cleaned_data['apellido']
         correo = form.cleaned_data['email']
         consulta = form.cleaned_data['consulta']
         mensaje = form.cleaned_data['mensaje']

        # Construye el cuerpo del correo electrónico
         body = f'Nombre: {nombre}\nApellido: {apellido}\nCorreo: {correo}\nConsulta: {consulta}\nMensaje: {mensaje}'

        # Configura el correo electrónico
         email = EmailMultiAlternatives(
            subject='Mensaje de contacto',
            body=body,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER]  # Reemplaza con la dirección de correo electrónico de destino
        )

        # Agrega un cuerpo HTML si es necesario
         html_content = f'<p>Nombre: {nombre}</p><p>Apellido: {apellido}</p><p>Correo: {correo}</p><p>Consulta: {consulta}</p><p>Mensaje: {mensaje}</p>'
         email.attach_alternative(html_content, 'text/html')

        # Envía el correo electrónico
         email.send()

        # Mensaje de éxito
         messages.success(self.request, 'Consulta enviada.')

         return super().form_valid(form)
      except SMTPDataError as e:
            # Manejo de errores
              print(f"Error al enviar el correo: {e}")
              traceback.print_exc()  # Esto imprimirá la traza de la pila en la consola

            # Mensaje de error
              messages.error(self.request, 'Error al enviar la consulta. Por favor, inténtelo de nuevo más tarde.')

              return super().form_invalid(form)