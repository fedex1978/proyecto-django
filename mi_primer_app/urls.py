from django.urls import path
from.views import saludo, saludo_con_template
urlpatterns = [
    path("Hola mundo/", saludo),
    path("hola-mundo-template/", saludo_con_template),

]
