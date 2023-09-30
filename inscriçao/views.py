from django.shortcuts import render , get_object_or_404
from . import models

def Index(request):
    alunos = models.Aluno.objects.all()
    return  render(request, 'index.html',{'alunos':alunos})

def aluno(request, id):
    aluno = get_object_or_404(models.Aluno, id=id)
    return render(request, 'aluno.html',{'aluno' :aluno})
