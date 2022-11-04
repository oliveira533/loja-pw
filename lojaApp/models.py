from tokenize import blank_re
from django.db import models

class Produtos(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=100)
    preco = models.CharField(max_length=10)
    tamanhos = models.CharField(max_length=5)
    image = models.CharField(max_length=1000)
    desc = models.CharField(max_length=1000,blank=True)

    def __str__(self):
        return self.titulo