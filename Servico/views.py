from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ServicoModel
from django.urls import reverse_lazy

# Create your views here.


class IndexServicoView(ListView):
    models = ServicoModel
    template_name = "servicoIndex.html"
    queryset = ServicoModel.objects.all()
    context_object_name = "servicos"

class CreateServicoView(CreateView):
    model = ServicoModel
    template_name = "servicoForm.html"
    fields = [
        "nome",
        "categoria",
        "preco_venda",
        "tempo_execucao",
    ]
    success_url = reverse_lazy("servicoIndex")
    extra_context = {"titulo": "Adicionar"}

class UpdateServicoView(UpdateView):
    model = ServicoModel
    template_name = "servicoForm.html"
    fields = [
        "nome",
        "categoria",
        'preco_venda',
        'tempo_execucao'
    ]
    success_url = reverse_lazy("servicoIndex")
    extra_context = {"titulo": "Editar"}

class DeleteServicoView(DeleteView):
    model = ServicoModel
    template_name = "servicoDel.html"
    success_url = reverse_lazy('servicoIndex')
