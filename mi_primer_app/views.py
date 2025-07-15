from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from views import saludo, saludo_con_template

def saludo(request):
    return HttpResponse ("Hola Mundo")

def saludo_con_template(request):
    return render (request,'mi_primer_app/saludo.html')