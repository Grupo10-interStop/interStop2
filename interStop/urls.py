"""interStop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#Para 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#interStop_app
from interStop_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test),
    path('modelo/', views.modelo),
    path('formulario/', views.formulario),
    path('formulario/formulario', views.formulario),
    path('formulario/enviar/', views.enviar),
    path('', views.inicio),
    path('formulario/inicio', views.inicioFormulario),
    path('administrar/formulario', views.Formulario_admin),
    path('formulario_inicio_admin', views.inicio_Formulario_admin),
]

urlpatterns += staticfiles_urlpatterns()