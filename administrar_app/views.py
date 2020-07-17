from django.shortcuts import render

# Create your views here.
def administrar(request):
    
    return render(request, "admin.html")