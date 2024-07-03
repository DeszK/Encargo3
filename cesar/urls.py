from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('registro', views.registro, name='registro'),
    path('tienda',views.tienda, name='tienda'),
    path('nuestros_productos',views.nuestros_productos, name='nuestros_productos'),
]
