from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sessions.backends.signed_cookies import SessionStore

# Datos simulados de productos
productos = {
    1: {'nombre': 'Laptop', 'precio': 800},
    2: {'nombre': 'Teléfono', 'precio': 500},
    3: {'nombre': 'Tablet', 'precio': 300}
}

def index(request: HttpRequest):
    return render(request, 'index.html', {'productos': productos})

def agregar(request: HttpRequest, id: int):
    if 'carrito' not in request.session:
        request.session['carrito'] = {}
    carrito = request.session['carrito']
    
    if str(id) in carrito:
        carrito[str(id)]['cantidad'] += 1
    else:
        carrito[str(id)] = {'nombre': productos[id]['nombre'], 'precio': productos[id]['precio'], 'cantidad': 1}
    
    request.session.modified = True
    return redirect('index')

def ver_carrito(request: HttpRequest):
    carrito = request.session.get('carrito', {})
    total = sum(item['precio'] * item['cantidad'] for item in carrito.values())
    return render(request, 'carrito.html', {'carrito': carrito, 'total': total})

def vaciar_carrito(request: HttpRequest):
    if 'carrito' in request.session:
        del request.session['carrito']
    return redirect('index')

urlpatterns = [
    path('', index, name='index'),
    path('agregar/<int:id>/', agregar, name='agregar'),
    path('carrito/', ver_carrito, name='carrito'),
    path('vaciar/', vaciar_carrito, name='vaciar_carrito'),
]

def back (request):
    return render(request, "cc.html")

def dos (request):
    return render(request, "dos.html")
# Create your views here.
