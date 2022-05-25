import email
from django.db import models

# Create your models here.
class PessoaModel(models.Model):
    nome = models.CharField('Nome', max_length=70)
    cpf = models.CharField('CPF', max_length=11)
    telefone = models.CharField('Telefone/Celular', max_length=11)
    email = models.EmailField('E-mail', max_length=80)
    data_nasc = models.DateField('Data de nascimento')
    endereco = models.CharField('Endereço', max_length=150)
    sexo = models.CharField('Sexo', max_length=1, choices=[('F', 'Feminino'), ('M', 'Masculino')])
    is_colaborador = models.BooleanField('É colaborador?')

    class Meta:
        verbose_name = 'Pessoa'

    def __str__(self):
        return self.nome