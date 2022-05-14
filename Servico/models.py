from django.db import models

# Create your models here.
class ProdutoModel(models.Model):
    nome = models.CharField('Nome', max_length=80)
    categoria = models.CharField('Categoria', max_length=30)
    preco_venda = models.DecimalField('Preço de venda', max_digits=7, decimal_places=2)
    tempo_execucao = models.TimeField('Tempo de execução')
