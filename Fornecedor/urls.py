# Podemos criar urls dentro dos apps
# essa é uma prática profissional, com o intuito de
# deixar o projeto mais organizado.

from django.urls import path

from .views import IndexFornecedorView, CreateFornecedorView, UpdateFornecedorView, DeleteFornecedorView

urlpatterns = [
    path('', IndexFornecedorView.as_view(), name='fornecedorIndex'),
    path('new', CreateFornecedorView.as_view(), name='fornecedorNew'),
    path('<int:pk>/edit', UpdateFornecedorView.as_view(), name='fornecedorEdit'),
    path('<int:pk>/delete', DeleteFornecedorView.as_view(), name='fornecedorDel')
]