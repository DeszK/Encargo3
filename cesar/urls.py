from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('formulario', views.formulario, name='formulario'),
    path('contacto', views.contacto, name='contacto'),
]
