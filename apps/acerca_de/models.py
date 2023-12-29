from django.db import models

class Miembro(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen= models.ImageField(null=True, blank=True, upload_to= 'media', default='usuario/user-default.png')

    def __str__(self):
        return self.nombre
