from django.shortcuts import render
from interStop_app.models import ProblemaDes
from interStop_app.models import Sector_afectado

# Create your views here.

def form_mod (request):
    des_problemas = ProblemaDes.objects.all()
    sector_nombres = Sector_afectado.objects.all()
    return render(request, "modificar_form.html", {"des_problema": des_problemas, "sector_nombres": sector_nombres})

def agregar_problema(request):
    problema=request.GET["problema_nuevo"]
    nuevo_problema=ProblemaDes()
    nuevo_problema.problema_nombre=problema
    nuevo_problema.save()
    return render(request, "Guardado.html")
def agregar_sector(request):
    sector=request.GET["sector_nuevo"]
    nuevo_sector=Sector_afectado()
    nuevo_sector.sector_nombre=sector
    nuevo_sector.save()
    return render(request, "Guardado.html")
def eliminar_problema(request):
    prob=request.GET["problms"]
    identificador=ProblemaDes.objects.filter(problema_nombre=prob)
    identificador.delete()
    return render(request, "Borrado.html")
def eliminar_sector(request):
    sec=request.GET["sect"]
    identificador=Sector_afectado.objects.filter(sector_nombre=sec)
    identificador.delete()
    return render(request, "Borrado.html")