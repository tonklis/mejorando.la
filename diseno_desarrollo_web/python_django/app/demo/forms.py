from django import forms
from demo.models import *

class LibroForm(forms.ModelForm):
  class Meta:
    model = Libro
