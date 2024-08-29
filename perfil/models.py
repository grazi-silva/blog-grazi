from django.db import models


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    ano_conclusao = models.IntegerField()

    def __str__(self):
        return f"{self.nome} - {self.instituicao}"


class Interesse(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
