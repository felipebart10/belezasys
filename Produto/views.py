from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import ProdutoModel
from django.urls import reverse_lazy

# Create your views here.

class IndexProdutoView(ListView):
    models = ProdutoModel
    template_name = 'produtoIndex.html'
    queryset = ProdutoModel.objects.all()
    context_object_name = 'produtos'

class CreateProdutoView(CreateView):
    model = ProdutoModel
    template_name = 'produtoForm.html'
    fields = [
        'nome',
        'categoria',
        'marca',
        'fornecedor',
        'peso_liq',
        'preco_custo',
        'preco_venda',
        'estoque_min'
    ]
    success_url = reverse_lazy("produtoIndex")
    extra_context = {"titulo": "Adicionar"}

class UpdateProdutoView(UpdateView):
    template_name = 'produtoForm.html'
    model = ProdutoModel
    fields = [
        'nome',
        'categoria',
        'marca',
        'fornecedor',
        'peso_liq',
        'preco_custo',
        'preco_venda',
        'estoque_min'
    ]
    success_url = reverse_lazy("produtoIndex")
    extra_context = {"titulo": "Editar"}

class DeleteProdutoView(DeleteView):
    model = ProdutoModel
    template_name = "produtoDel.html"
    success_url = reverse_lazy("produtoIndex")