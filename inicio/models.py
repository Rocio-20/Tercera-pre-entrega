from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=30)
    def __str__(self):
      return f'{self.id} - {self.nombre}'

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    def __str__(self):
      return f'{self.id} - {self.nombre}'

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    anio_de_publicacion = models.DateField()
    hojas = models.IntegerField()   
    descripcion = RichTextField()
    portada = models.ImageField(upload_to='imagenes_libros/', null=True)

    
    def __str__(self):
      return self.titulo
    
