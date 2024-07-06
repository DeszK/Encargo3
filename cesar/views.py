from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from cesar import carrito
from cesar.carrito import Carrito
from cesar.models import Producto

# Create your views here.

def index(request):
    context={}
    return render(request, 'cesar/index.html', context)

def registro(request):
 if request.method !="POST":
    context={"clase":"registro"}
    return render(request, 'cesar/registro.html', context)
 else:
     nombre = request.POST["nombre"]
     contrasena = request.POST["contrasena"]
     user = User.objects.create_user(username=nombre, password=contrasena)
     user.save()
     context={"clase":"registro", "mensaje": "Los datos fueron registrados con exito!"}
     return render(request, 'cesar/registro.html', context)

def tienda(request):
    productos = Producto.objects.all()
    return render(request, "cesar/tienda.html",{'productos':productos})

def contacto(request):
    context={}
    return render(request, 'cesar/contacto.html', context)

def locales(request):
    context={}
    return render(request, 'cesar/locales.html', context)

def perfil(request):
    context={}
    return render(request, 'cesar/perfil.html', context)
    

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
