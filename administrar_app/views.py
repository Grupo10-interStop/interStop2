from django.shortcuts import render
from interStop_app.models import Departamento
from interStop_app.models import Problema
from interStop_app.models import ProblemaDes


# Create your views here.
def administrar(request):
    departamentos = Departamento.objects.all()
    return render(request, "admin.html", {"departamentos":departamentos}) 
def eliminar_seguro(request):
    departamentos = Departamento.objects.all()
    return render(request, "eliminar.html", {"departamentos":departamentos})

def eliminar_eliminado(request):
    dep=request.GET["deps"]
    identificador=Problema.objects.filter(id_departamentop=dep)
    identificador.delete()
    """
    for borrar in identificador:
        if borrar.id_departamentop == 1:
            borrar.delete() 
        """
    return render(request, "admin.html")
def agregar_problema(request):
    problema=request.GET["problema_nuevo"]
    nuevo_problema=ProblemaDes()
    nuevo_problema.problema_nombre=problema
    nuevo_problema.save()
    return render(request, "admin.html")


