from django.db import models

# Create your models here.
class Service(models.Model):
    # nombres de las columnas
    title = models.CharField(max_length=200, verbose_name='Título')
    subtitle = models.CharField(max_length=200, verbose_name='Subtitulo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name='Imagen')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación') 
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')                                                                                                                                                                                                                        

    class Meta:
        verbose_name = 'Servicio' #Indica el nombre del modelo
        verbose_name_plural = 'Servicios'#Nombre del modelo en plural
        ordering = ['-created'] #Ordena los proyectos del más nuevo al más viejo

    def __str__(self) -> str:
        return self.title #Se retornara el nombre del proyecto
                                                                                