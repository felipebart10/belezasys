from django.db import models

# Create your models here.
class FornecedorModel(models.Model):
    nome = models.CharField('Nome', max_length=70)
    cnpj = models.CharField('CNPJ', max_length=14)
    telefone = models.CharField('Telefone/Celular', max_length=11)
    email = models.EmailField('E-mail', max_length=80)
    endereco = models.CharField('Endereço', max_length=150)

    class Meta:
        verbose_name = 'Fornecedor'

    def __str__(self) -> str:
        return self.nome

    def formatar_cnpj(self):
        return '{}{}.{}{}{}.{}{}{}/{}{}{}{}-{}{}'.format(*self.cnpj)