from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
from django.template.context import RequestContext
from demo.models import *
#para el hot trick
from django.shortcuts import render_to_response

def home(request):
  libros = Libro.objects.filter(disponible = True)
  return render_to_response('galeria.html', context_instance=RequestContext(request, {"libros":libros}))

def index_view(request):
  cadena = "Hola mejorandola"
  return HttpResponse(cadena)

def post(request, id):
  #Conseguir objeto de BD
  return HttpResponse("Este es el post %s" % id)

def hora_actual(request):
  ahora = datetime.now()
  t = get_template("template1.html")
  c = Context({'hora': ahora})
  html = t.render(c)
  return HttpResponse(html)

def hora_actual_hot_trick(request):
  hora = datetime.now()
  usuario = "Arturo"
  rango = range(1,10)
  return render_to_response('template1.html', locals())

from demo.forms import LibroForm

def agregar(request):
  if request.method == 'POST':
    form = LibroForm(request.POST)
    if form.is_valid():
      form.save()
      cd = form.cleaned_data
      #send_mail(cd['subject'], cd['message'],)
      return HttpResponseRedirect('/')
  else:
    form = LibroForm()
  data = {'form': form}
  #return render_to_response('agregar.html', {'form': form}) 
  return render_to_response('agregar.html', context_instance=RequestContext(request, data))
