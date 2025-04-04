# Importamos path para definir las rutas de la aplicación
# Importamos views para asociar las rutas con las funciones correspondientes
from django.urls import path
from . import views
# Definimos las rutas específicas de la aplicación "personas"
urlpatterns = [
      # Ruta para crear una persona, llama a la vista 'crear_persona'
    path('crear/', views.crear_persona, name='crear_persona'),
    path('lista/', views.lista_personas, name='lista_personas'),
    path('editar/<int:id>/', views.editar_persona, name='editar_persona'),
    path('eliminar/<int:id>/', views.eliminar_persona, name='eliminar_persona'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('personas/', include('personas.urls')),
]
