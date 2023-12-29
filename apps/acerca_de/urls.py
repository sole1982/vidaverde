from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'apps.acerca_de'

urlpatterns = [
    path('acerca_de/', views.acerca_de, name='acerca_de'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)