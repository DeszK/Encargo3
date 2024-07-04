from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('registro', views.registro, name='registro'),
    path('tienda',views.tienda, name='tienda'),
    path('contacto',views.contacto, name='contacto'),
    path('locales',views.locales, name='locales'),
    path('agregar/<int:producto_id>/', views.agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', views.restar_producto, name="Sub"),
    path('limpiar/', views.limpiar_carrito, name="CLS"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
