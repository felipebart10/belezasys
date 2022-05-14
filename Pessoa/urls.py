# Podemos criar urls dentro dos apps
# essa é uma prática profissional, com o intuito de
# deixar o projeto mais organizado.

from django.urls import path

from .views import listar

urlpatterns = [
    path('listar', listar, name='index'),
]