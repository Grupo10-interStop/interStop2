from django.http import HttpResponse
from django.shortcuts import render
#from interStop_app.forms import formulario_datos
from interStop_app.models import Departamento
from interStop_app.models import Municipio
from interStop_app.models import ProblemaDes
from interStop_app.models import Sector_afectado
from interStop_app.models import Problema
import datetime


# Create your views here.
class dato:
    cantidad=2
    Depa=""

def recuperar(a):
    registro=Problema.objects.filter(id_departamentop=a)
    cantidadR=registro.count()
    return cantidadR
def test(request):
    return render(request, "test/test.html")

def modelo(request):
    return render(request, "modelo.html")

def formulario(request):

    departamentos = Departamento.objects.all()
    municipios = Municipio.objects.all()
    des_problemas = ProblemaDes.objects.all()
    sector_nombres = Sector_afectado.objects.all()
    return render(request, "formulario.html", {"departamentos":departamentos, "municipios": municipios,
    "des_problema": des_problemas, "sector_nombres": sector_nombres})



def enviar(request):
    
    mensaje = "%r"%request.GET["sect"]
    dep="%r"%request.GET["deps"]
    mun="%r"%request.GET["muni"]
    prob="%r"%request.GET["problms"]
    sec="%r"%request.GET["sect"]
    come="%r"%request.GET["comen"]
    fecha=datetime.date.today()
    
   # identificador=Problema.annotate(Count('id_pro'))    

    problemas=Problema()
    problemas.descripcion=come
    problemas.id_departamentop=dep
    problemas.id_municipiop=mun
    problemas.id_problemap=prob
    problemas.id_sectorp=sec
    problemas.id_usuariop=1
    problemas.fecha=fecha
    problemas.save()
    
    return HttpResponse(mensaje) 

def inicioFormulario(request):
        dep="%r"%request.GET["deps"]
        mun="%r"%request.GET["muni"]
        prob="%r"%request.GET["problms"]
        sec="%r"%request.GET["sect"]
        come="%r"%request.GET["comen"]
        fecha=datetime.date.today()

        problemas=Problema()
        problemas.descripcion=come
        problemas.id_departamentop=dep
        problemas.id_municipiop=mun
        problemas.id_problemap=prob
        problemas.id_sectorp=sec
        problemas.id_usuariop=1
        problemas.fecha=fecha
        problemas.save()

        return render(request, "inicio.html")

def inicio(request):
        #PRoblemas totales
        problemas_registrados=Problema.objects.all()        
        cantidad_total=problemas_registrados.count()
        #Registrados por anonimos
        anonimos=Problema.objects.filter(id_usuariop='1')
        cantida_anonimos=anonimos.count()
        #Registrados por el administrador
        administradores=Problema.objects.filter(id_usuariop='2')
        cantida_administrador=administradores.count()
        #Afectados en el estudio
        estudiantes_totales=Problema.objects.filter(id_sectorp="'1'")
        cantida_estudiantes=estudiantes_totales.count()
        #Afectados en el estudio admin
        estudiantes_totales_admin=Problema.objects.filter(id_sectorp="'1'", id_usuariop='2')
        cantida_estudiantes_admin=estudiantes_totales.count()
        #Afectados en el estudio anonimo
        estudiantes_totales_a=Problema.objects.filter(id_sectorp="'1'", id_usuariop='1')
        cantida_estudiantes_a=estudiantes_totales_a.count()
        #Afectados en el trabajo
        trabajadores_totales=Problema.objects.filter(id_sectorp="'2'")
        cantida_trabajadores=trabajadores_totales.count()
        #Afectados en el trabajo
        trabajadores_admin=Problema.objects.filter(id_sectorp="'2'",  id_usuariop='2')
        cantida_trabajadores_a=trabajadores_admin.count()
        #Afectados en el trabajo
        trabajadores_anoni=Problema.objects.filter(id_sectorp="'2'",  id_usuariop='1')
        cantida_trabajadores_anoni=trabajadores_anoni.count()
        #Afectados en lo personal
        per_totales=Problema.objects.filter(id_sectorp="'3'")
        cantida_per=per_totales.count()
        #Afectados en lo personal admin
        per_admin=Problema.objects.filter(id_sectorp="'3'",  id_usuariop='2')
        cantida_per_ad=per_admin.count()
        #Afectados en el trabajo
        per_anoni=Problema.objects.filter(id_sectorp="'3'",  id_usuariop='1')
        cantida_per_anoni=per_anoni.count()

        #Problema mala señal
        mala_señal=Problema.objects.filter(id_problemap="'1'")
        can_mala_señal=mala_señal.count()
        #Problema no me aalcanza
        sin_dinero=Problema.objects.filter(id_problemap="'2'")
        can_sin_dinero=sin_dinero.count()
        #Problema sin cobertura
        sin_cobertura=Problema.objects.filter(id_problemap="'3'")
        can_sin_cobertura=sin_cobertura.count()
        #Problema sin aparato
        sin_aparato=Problema.objects.filter(id_problemap="'4'")
        can_sin_aparato=sin_aparato.count()

        #Recuperar datos por departamento
        can_dep=[1,2,3,4,1,1,1,1,1,1,1,1,1,1]
        for n in [0,1,2,3,4,5,6,7,8,9,10,11,12,13]:
            num=n+1
            can_dep[n] = recuperar(num)
        
        departamentos = Departamento.objects.all()
        nom_dep=["","","","","","","","","","","","","",""]
        n=0
        for dep in departamentos:
            nom_dep[n]=dep.nombre_depa
            n=n+1
        
        depar=[dato,dato,dato,dato,dato,dato,dato,dato,dato,dato,dato,dato,dato,dato]
        for a in [0,1,2,3,4,5,6,7,8,9,10,11,12,13]:
            depar[a].Depa=nom_dep[a]
            depar[a].cantidad=can_dep[a]

        
        #Prueba metodo
        cantidadprueba=recuperar("'3'")
        cantidadprueba=can_dep[1]


        return render(request, "inicio.html", {"cantidad":cantidad_total, "cantidaA":cantida_anonimos, 
        "cantidaAdmin":cantida_administrador, "estudiantes":cantida_estudiantes, "estudiantesad":cantida_estudiantes_admin,
        "estudiantesA":cantida_estudiantes_a, "trabajadores":cantida_trabajadores,"trabajadorA":cantida_trabajadores_a,
        "trabajadorAn":cantida_trabajadores_anoni,"perso":cantida_per, "pesoAd":cantida_per_ad, "perAn":cantida_per_anoni,
        "prueba":cantidadprueba, "DatosDepartamento":depar})

def Formulario_admin(request):
    departamentos = Departamento.objects.all()
    municipios = Municipio.objects.all()
    des_problemas = ProblemaDes.objects.all()
    sector_nombres = Sector_afectado.objects.all()
    
    return render(request, "datosadmin.html", {"departamentos":departamentos, "municipios": municipios,
    "des_problema": des_problemas, "sector_nombres": sector_nombres})

def inicio_Formulario_admin(request):
        dep=request.GET["deps"]
        mun=request.GET["muni"]
        prob="%r"%request.GET["problms"]
        sec="%r"%request.GET["sect"]
        come="Agregado por administrador"
        cantidad=request.GET["cantidad"]
        fecha=datetime.date.today()
        
        can=int(cantidad)

        for num in range(can):
            problemas=Problema()
            problemas.descripcion=come
            problemas.id_departamentop=dep
            problemas.id_municipiop=mun
            problemas.id_problemap=prob
            problemas.id_sectorp=sec
            problemas.id_usuariop=2
            problemas.fecha=fecha
            problemas.save()
        
        return render(request, "inicio.html")