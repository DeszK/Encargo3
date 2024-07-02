from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    context={}
    return render(request, 'cesar/index.html', context)

def registro(request):
    context={}
    return render(request, 'cesar/registro.html', context)

def tienda(request):
    context={}
    return render(request, "cesar/tienda.html", context)