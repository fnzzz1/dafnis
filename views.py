# Importamos render para renderizar plantillas HTML
# Importamos redirect para redirigir después de una acción
# Importamos get_object_or_404 para obtener un objeto o lanzar un error 404 si no existe
from django.shortcuts import render, redirect, get_object_or_404

# Importamos el modelo Persona para interactuar con la base de datos
from .models import Persona

# Importamos el formulario PersonaForm para manejar la creación y edición de personas
from .forms import PersonaForm

# Vista para crear una nueva persona
def crear_persona(request):
    if request.method == 'POST':  # Si el formulario se envía
        form = PersonaForm(request.POST)  # Llenamos el formulario con los datos enviados
        if form.is_valid():  # Validamos el formulario
            form.save()  # Guardamos la nueva persona en la base de datos
            return redirect('lista_personas')  # Redirigimos a la lista de personas
    else:
        form = PersonaForm()  # Si es una petición GET, mostramos un formulario vacío
    return render(request, 'personas/crear_persona.html', {'form': form})  # Renderizamos la plantilla con el formulario

# Vista para listar todas las personas
def lista_personas(request):
    personas = Persona.objects.all()  # Obtenemos todas las personas de la base de datos
    return render(request, 'personas/lista_personas.html', {'personas': personas})  # Renderizamos la plantilla con la lista

# Vista para editar una persona existente
def editar_persona(request, id):
    persona = get_object_or_404(Persona, id=id)  # Buscamos la persona por su ID, o mostramos un error 404 si no existe
    if request.method == 'POST':  # Si el formulario se envía
        form = PersonaForm(request.POST, instance=persona)  # Llenamos el formulario con los datos de la persona
        if form.is_valid():  # Validamos el formulario
            form.save()  # Guardamos los cambios en la base de datos
            return redirect('lista_personas')  # Redirigimos a la lista de personas
    else:
        form = PersonaForm(instance=persona)  # Si es una petición GET, mostramos el formulario con los datos actuales
    return render(request, 'personas/editar_persona.html', {'form': form})  # Renderizamos la plantilla con el formulario

# Vista para eliminar una persona
def eliminar_persona(request, id):
    persona = get_object_or_404(Persona, id=id)  # Buscamos la persona por su ID
    if request.method == 'POST':  # Si el usuario confirma la eliminación
        persona.delete()  # Eliminamos la persona de la base de datos
        return redirect('lista_personas')  # Redirigimos a la lista de personas
    return render(request, 'personas/eliminar_persona.html', {'persona': persona})  # Renderizamos la plantilla de confirmación
