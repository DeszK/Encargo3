from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProductoForm, ContactoForm, CustomUserCreationForm
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


from cesar import carrito
from cesar.carrito import Carrito
from cesar.models import Contacto, Producto

# Create your views here.

def index(request):
    context={}
    return render(request, 'cesar/index.html', context)


def tienda(request):
    productos = Producto.objects.all()
    return render(request, "cesar/tienda.html",{'productos':productos})


def locales(request):
    context={}
    return render(request, 'cesar/locales.html', context)

def perfil(request):
    context={}
    return render(request, 'cesar/perfil.html', context)
    

def agregar_producto_carrito(request, producto_id):
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

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado exitosamente")
            return redirect(to="index")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

def send_email(mail):
    context = {'mail': mail}
    template = get_template('cesar/correo.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Respuesta Chico Cesar',
        '',
        settings.EMAIL_HOST_USER,
        [mail]
    )
    email.attach_alternative(content, 'text/html')
    email.send()

def correo(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        send_email(mail)
        return redirect('lista_mensajes')
    return render(request, 'cesar/lista_mensajes.html', {})


