from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test(request):
    return render(request, "test/test.html")
    
def iniciar1(request):
    
    return render(request, "modelo_inicio.html")

def iniciar(request):
    
    return render(request, "inicio.html")
