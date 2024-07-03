from django.shortcuts import render, HttpResponse, redirect

from cesar import carrito
from cesar.carrito import Carrito
from cesar.models import Producto

# Create your views here.

def index(request):
    context={}
    return render(request, 'cesar/index.html', context)

def registro(request):
    context={}
    return render(request, 'cesar/registro.html', context)

def tienda(request):
    productos = Producto.objects.all()
    return render(request, "cesar/tienda.html",{'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("tienda")

def eliminar_producto(request, producto_id):
    Carrito =  Carrito(request)
    producto =  Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("tienda")

def restar_producto(request, producto_id):
    carrito =  Carrito(request)
    producto =  Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()    
    return redirect("tienda")