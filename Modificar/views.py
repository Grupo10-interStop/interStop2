from django.shortcuts import render

# Create your views here.

def form_mod (request):
    
    return render(request, "modificar_form.html")