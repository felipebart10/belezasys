# Podemos criar urls dentro dos apps
# essa é uma prática profissional, com o intuito de
# deixar o projeto mais organizado.

from django.urls import path

from .views import IndexPessoaView, CreatePessoaView, UpdatePessoaView, DeletePessoaView

urlpatterns = [
    path('', IndexPessoaView.as_view(), name='pessoaIndex'),
    path('new', CreatePessoaView.as_view(), name='add_pessoa'),
    path('<int:pk>/edit', UpdatePessoaView.as_view(), name='edit_pessoa'),
    path('<int:pk>/delete', DeletePessoaView.as_view(), name='del_pessoa')
]