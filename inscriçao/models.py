from django.db import models

class Aluno(models.Model):
    foto = models.ImageField(upload_to='fotos')
    nome = models.CharField(max_length=250)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=11)
    endereço = models.CharField(max_length=255)
    cep = models.CharField(max_length=8)
    email = models.EmailField(max_length=200)
    contatos = models.CharField(max_length=11)

    def __str__(self):
       return self.nome




