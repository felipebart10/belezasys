from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import PessoaModel
from django.urls import reverse_lazy

# Create your views here.


class IndexPessoaView(ListView):
    models = PessoaModel
    template_name = "pessoaIndex.html"
    queryset = PessoaModel.objects.all()
    context_object_name = "pessoas"


class CreatePessoaView(CreateView):
    model = PessoaModel
    template_name = "pessoaForm.html"
    fields = [
        "nome",
        "cpf",
        "telefone",
        "email",
        "data_nasc",
        "endereco",
        "sexo",
        "is_colaborador",
    ]
    success_url = reverse_lazy("pessoaIndex")
    extra_context = {"titulo": "Adicionar"}

class UpdatePessoaView(UpdateView):
    model = PessoaModel
    template_name = "pessoaForm.html"
    fields = [
        "nome",
        "cpf",
        "telefone",
        "email",
        "data_nasc",
        "endereco",
        "sexo",
        "is_colaborador",
    ]
    success_url = reverse_lazy("pessoaIndex")
    extra_context = {"titulo": "Editar"}

class DeletePessoaView(DeleteView):
    model = PessoaModel
    template_name = "pessoaDel.html"
    success_url = reverse_lazy('pessoaIndex')
