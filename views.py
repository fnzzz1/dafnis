# Importamos render para renderizar plantillas HTML
# Importamos redirect para redirigir después de una acción
from django.shortcuts import render, redirect

# Importamos HttpRequest para manejar las solicitudes HTTP
from django.http import HttpRequest

# Importamos path para definir rutas de la aplicación
from django.urls import path

# Importamos settings para manejar archivos estáticos
# Importamos static para servir archivos estáticos en desarrollo
from django.conf import settings
from django.conf.urls.static import static

# Importamos SessionStore para manejar sesiones con cookies firmadas
from django.contrib.sessions.backends.signed_cookies import SessionStore

# Datos simulados de productos en un diccionario
productos = {
    1: {'nombre': 'Laptop', 'precio': 800},
    2: {'nombre': 'Teléfono', 'precio': 500},
    3: {'nombre': 'Tablet', 'precio': 300}
}

# Vista principal que muestra los productos disponibles
def index(request: HttpRequest):
    return render(request, 'index.html', {'productos': productos})  # Pasamos los productos a la plantilla

# Vista para agregar un producto al carrito
def agregar(request: HttpRequest, id: int):
    if 'carrito' not in request.session:  # Si no existe un carrito en la sesión, lo inicializamos
        request.session['carrito'] = {}
    
    carrito = request.session['carrito']  # Obtenemos el carrito actual de la sesión
    
    if str(id) in carrito:  # Si el producto ya está en el carrito, aumentamos la cantidad
        carrito[str(id)]['cantidad'] += 1
    else:  # Si el producto no está en el carrito, lo agregamos con cantidad 1
        carrito[str(id)] = {'nombre': productos[id]['nombre'], 'precio': productos[id]['precio'], 'cantidad': 1}
    
    request.session.modified = True  # Marcamos la sesión como modificada para que se guarden los cambios
    return redirect('index')  # Redirigimos a la página principal

# Vista para mostrar los productos en el carrito
def ver_carrito(request: HttpRequest):
    carrito = request.session.get('carrito', {})  # Obtenemos el carrito de la sesión, o un diccionario vacío si no existe
    total = sum(item['precio'] * item['cantidad'] for item in carrito.values())  # Calculamos el total del carrito
    return render(request, 'carrito.html', {'carrito': carrito, 'total': total})  # Pasamos los datos a la plantilla

# Vista para vaciar el carrito
def vaciar_carrito(request: HttpRequest):
    if 'carrito' in request.session:  # Si el carrito existe en la sesión, lo eliminamos
        del request.session['carrito']
    return redirect('index')  # Redirigimos a la página principal

# Definición de rutas de la aplicación
urlpatterns = [
    path('', index, name='index'),  # Ruta de la página principal
    path('agregar/<int:id>/', agregar, name='agregar'),  # Ruta para agregar un producto al carrito
    path('carrito/', ver_carrito, name='carrito'),  # Ruta para ver el carrito
    path('vaciar/', vaciar_carrito, name='vaciar_carrito'),  # Ruta para vaciar el carrito
]

# Vista para renderizar la plantilla "cc.html"
def back(request):
    return render(request, "cc.html")

# Vista para renderizar la plantilla "dos.html"
def dos(request):
    return render(request, "dos.html")

# Create your views here.
