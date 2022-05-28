from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import FornecedorModel
from django.urls import reverse_lazy

# Create your views here.


class IndexFornecedorView(ListView):
    models = FornecedorModel
    template_name = "fornecedorIndex.html"
    queryset = FornecedorModel.objects.all()
    context_object_name = "fornecedores"


class CreateFornecedorView(CreateView):
    model = FornecedorModel
    template_name = "fornecedorForm.html"
    fields = [
        "nome",
        "cnpj",
        "telefone",
        "email",
        "endereco",
    ]
    success_url = reverse_lazy("fornecedorIndex")
    extra_context = {"titulo": "Adicionar"}

class UpdateFornecedorView(UpdateView):
    model = FornecedorModel
    template_name = "fornecedorForm.html"
    fields = [
        "nome",
        "cnpj",
        "telefone",
        "email",
        "endereco",
    ]
    success_url = reverse_lazy("fornecedorIndex")
    extra_context = {"titulo": "Editar"}

class DeleteFornecedorView(DeleteView):
    model = FornecedorModel
    template_name = "fornecedorDel.html"
    success_url = reverse_lazy('fornecedorIndex')
