# Podemos criar urls dentro dos apps
# essa é uma prática profissional, com o intuito de
# deixar o projeto mais organizado.

from django.urls import path

from .views import CreateServicoView, UpdateServicoView, IndexServicoView, DeleteServicoView

urlpatterns = [
    path('', IndexServicoView.as_view(), name='servicoIndex'),
    path('new', CreateServicoView.as_view(), name='servicoNew'),
    path('<int:pk>/edit', UpdateServicoView.as_view(), name='servicoEdit'),
    path('<int:pk>/delete', DeleteServicoView.as_view(), name='servicoDel')
]