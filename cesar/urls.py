from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('registro', views.registro, name='registro'),
    path('tienda',views.tienda, name='tienda'),
    path('contacto',views.contacto, name='contacto'),
    path('locales',views.locales, name='locales'),
    path('perfil',views.perfil, name='perfil'),
    path('agregar/<int:producto_id>/', views.agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', views.restar_producto, name="Sub"),
    path('limpiar/', views.limpiar_carrito, name="CLS"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('agregar_producto/', views.agregar_producto, name="agregar_producto"),
    path('lista_productos/', views.listar_productos, name="lista_productos"),
    path('modificar_producto/<id>/', views.modificar_producto, name="modificar_producto"),
    path('eliminar_producto/<id>/', views.eliminar_producto, name="eliminar_producto"),
    path('lista_mensajes/', views.lista_mensajes, name="lista_mensajes"),
    path('ver_mensaje/<id>/', views.ver_mensaje, name="ver_mensaje"),
    path('eliminar_mensaje/<id>/', views.eliminar_mensaje, name="eliminar_mensaje"),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
