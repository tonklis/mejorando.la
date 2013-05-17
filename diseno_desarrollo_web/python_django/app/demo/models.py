from django.db import models

class Autor(models.Model):
  nombre = models.CharField(blank=True, max_length=100)

  def __unicode__(self):
    return self.nombre

class Libro(models.Model):
  nombre = models.CharField(blank=True, max_length=100)
  creado = models.DateTimeField(blank=True, auto_now = True)
  disponible = models.BooleanField(default=True)
  autor = models.OneToOneField(Autor)
  
  def __unicode__(self):
    return "%s por %s" % (self.nombre, self.autor.nombre)
