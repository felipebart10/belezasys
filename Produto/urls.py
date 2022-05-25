# Podemos criar urls dentro dos apps
# essa é uma prática profissional, com o intuito de
# deixar o projeto mais organizado.

from django.urls import path

from .views import IndexProdutoView, CreateProdutoView, UpdateProdutoView, DeleteProdutoView

urlpatterns = [
    path('', IndexProdutoView.as_view(), name='produtoIndex'),
    path('new', CreateProdutoView.as_view(), name='produtoNew'),
    path('<int:pk>/edit', UpdateProdutoView.as_view(), name='produtoEdit'),
    path('<int:pk>/delete', DeleteProdutoView.as_view(), name='produtoDel')
]