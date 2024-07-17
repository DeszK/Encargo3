from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProductoForm, ContactoForm
from django.core.paginator import Paginator
from django.http import Http404


from cesar import carrito
from cesar.carrito import Carrito
from cesar.models import Contacto, Producto

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

def agregar_producto(request):

    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado Correctamente")
        else:
            data["form"] = formulario

    return render(request, 'cesar/agregar_producto.html', data)

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Enviado Correctamente")
        else:
            data["form"] = formulario

    return render(request, 'cesar/contacto.html', data)

def listar_productos(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': productos,
        'paginator': paginator
    }

    return render(request, 'cesar/lista_productos.html', data)

def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)
    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="lista_productos")
        data["form"] = formulario

    return render(request, 'cesar/modificar_producto.html', data)

def eliminar_producto(request, id):
    
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="lista_productos")

def lista_mensajes(request):
    productos = Contacto.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': productos,
        'paginator': paginator
    }

    return render(request, 'cesar/lista_mensajes.html', data)

def ver_mensaje(request, id):

    producto = get_object_or_404(Contacto, id=id)
    data = {
        'form': ContactoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="lista_productos")
        data["form"] = formulario

    return render(request, 'cesar/ver_mensaje.html', data)

def eliminar_mensaje(request, id):
    
    producto = get_object_or_404(Contacto, id=id)
    producto.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="lista_mensajes")