from django.shortcuts import render, redirect, get_object_or_404
from .models import Persona
from .forms import PersonaForm

# Página de formulario
def crear_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_personas')
    else:
        form = PersonaForm()
    return render(request, 'personas/crear_persona.html', {'form': form})

# Página de lista
def lista_personas(request):
    personas = Persona.objects.all()
    return render(request, 'personas/lista_personas.html', {'personas': personas})

# Editar persona
def editar_persona(request, id):
    persona = get_object_or_404(Persona, id=id)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('lista_personas')
    else:
        form = PersonaForm(instance=persona)
    return render(request, 'personas/editar_persona.html', {'form': form})

# Eliminar persona
def eliminar_persona(request, id):
    persona = get_object_or_404(Persona, id=id)
    if request.method == 'POST':
        persona.delete()
        return redirect('lista_personas')
    return render(request, 'personas/eliminar_persona.html', {'persona': persona})
