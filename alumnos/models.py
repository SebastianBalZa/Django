from django.db import models

class Genero(models.Model):
    id_genero = models.AutoField(db_column="id_genero", primary_key=True)
    genero = models.CharField(max_length=50, blank=False, null=False)

    def __srt__(self):
       return str(self.genero)

class Alumno(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    id_genero = models.ForeignKey("Genero", on_delete=models.CASCADE, db_column="id_genero")
    telefono = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=100,blank=True,null=True)
    activo = models.IntegerField()

    def __str__(self):
        return str(self.nombre) +" "+ str(self.apellido_paterno)