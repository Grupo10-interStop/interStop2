from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as dj_login

# Create your views here.

def test(request):
    return render(request, "test/test.html")

def secioniniciada(request):

        if request.method=="POST":
            usu = 'test'
            cont = request.POST["password"]
            usuC = 2
            usuario=authenticate(username=usu, password=cont)
            #para test user:test password: 12test34
            if usuario is not None:
                dj_login(request, usuario)
                return HttpResponseRedirect('/')
            else:
                return render(request, "login.html")
            
        
        return render(request, "inicio.html")


def login(request):
  
    return render(request, "login.html")

def iniciar(request):
    
    return render(request, "iniciosesion.html")
