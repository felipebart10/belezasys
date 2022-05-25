from statistics import mode
from django.db import models

# Create your models here.
class ProdutoModel(models.Model):
    nome = models.CharField('Nome', max_length=80)
    categoria = models.CharField('Categoria', max_length=30) # vai virar tabela própria
    marca = models.CharField('Marca', max_length=30) # vai virar tabela própria
    fornecedor = models.CharField('Fornecedor', max_length=30)
    peso_liq = models.IntegerField('Peso líquido (g)')
    preco_custo = models.DecimalField('Preço de custo', max_digits=7, decimal_places=2)
    preco_venda = models.DecimalField('Preço de venda', max_digits=7, decimal_places=2)
    estoque_min = models.IntegerField('Estoque mínimo')
    
    class Meta:
        verbose_name = 'Produto'

    def __str__(self) -> str:
        return self.nome