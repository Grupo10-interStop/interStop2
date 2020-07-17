from django.db import models

# Create your models here.

class Departamento(models.Model):
    id=models.IntegerField(primary_key=True,max_length=2)
    nombre_depa=models.CharField(max_length=20)
    def __str__(self):
        return self.nombre_depa

class Municipio(models.Model):
    id=models.CharField(primary_key=True,max_length=3)
    nombre_muni=models.CharField(max_length=30)
    departamento=models.ForeignKey(Departamento,on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.nombre_muni

class ProblemaDes(models.Model):
    id_problema=models.CharField(primary_key=True,max_length=3)
    problema_nombre=models.CharField(max_length=50)
    def __str__(self):
        return self.problema_nombre

class Sector_afectado(models.Model):
    id_sector=models.CharField(primary_key=True,max_length=3)
    sector_nombre=models.CharField(max_length =30)

class Usuario(models.Model):
    nombre=models.CharField(max_length=40)
    contraseña=models.CharField(max_length=10)

class Problema(models.Model):
    descripcion=models.CharField(max_length=100)
    id_sectorp=models.CharField(max_length=3)
    fecha=models.DateField()
    id_problemap=models.CharField(max_length=3)
    id_departamentop=models.CharField(max_length=3)
    id_municipiop=models.CharField(max_length=3)
    id_usuariop=models.CharField(max_length=3)


    