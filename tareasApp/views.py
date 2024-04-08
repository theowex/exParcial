from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

lista_tareas = [
    ['Web', 'Desarrollo de la web', '2024-04-12', 'EN PROGRESO', 'Owen'],
    ['Marketing', 'Creación de campañas', '2024-04-16', 'EN PROGRESO', 'Kate'],
    ['Web scraping', 'Análisis de webs', '2024-04-28', 'EN PROGRESO', 'Johar']
]

# Create your views here.
def index(request):
    return render(request, 'index.html', {
        'lista_tareas': lista_tareas
    })

def nuevaTarea(request):
    if request.method == "POST":
        print(request.POST)
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        fechaFin = request.POST.get('fechaFin')
        responsable = request.POST.get('responsable')
        lista_tareas.append([nombre, descripcion, fechaFin, 'EN PROGRESO', responsable])
        return HttpResponseRedirect(reverse('tareasApp:index'))
    return render(request, 'nuevaTarea.html')