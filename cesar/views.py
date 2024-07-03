from django.shortcuts import render, HttpResponse

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
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    Carrito =  Carrito(request)
    producto =  Producto.objects.ge(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    Carrito =  Carrito(request)
    producto =  Producto.objects.ge(id=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = carrito(request)
    carrito.limpiar()    
    return redirect("Carrito")

def nuestros_productos(request):
    context={}
    return render(request, 'cesar/nuestros_productos.html', context)