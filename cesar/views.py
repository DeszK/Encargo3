from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, 'cesar/index.html', context)

def registro(request):
    context={}
    return render(request, 'cesar/registro.html', context)