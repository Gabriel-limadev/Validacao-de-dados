from django.db import models

class Registro(models.Model):
    data_pesquisa = models.DateField()
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14)
    cep = models.CharField(max_length=9)
    celular = models.CharField(max_length=12)