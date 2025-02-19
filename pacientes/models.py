from django.db import models
from django.urls import reverse

class Pacientes(models.Model):

    queixa_choices = (
        ('TDAH', 'Transtorno do Déficit de Atenção com Hiperatividade'),
        ('TEA', 'Transtorno do Espectro Autista'),
        ('D', 'Depressão'),
        ('A', 'Ansiedade'),
        ('TAG', 'Transtorno de Ansiedade Generalizada'),
        ('TA', 'Transtorno Alimentar'),
        ('TOC', 'Transtorno Obsessivo Compulsivo'),
        ('TPS', 'Transtorno do Processamento Sensorial'),
        ('TDI', 'Transtorno Dissociativo de Identidade'),
        ('SEP', 'Síndrome do Esgotamento Profissional (Burnout)'),
        ('DISL', 'Dislexia'),
        ('DISC', 'Discalculia'),
    )

    nome = models.CharField(max_length=255)
    email = models.EmailField()
    tel = models.CharField(max_length=16, null=True, blank=True)
    foto = models.ImageField(upload_to='fotos')
    pagamento_em_dia = models.BooleanField(default=True)
    queixa = models.CharField(max_length=4, choices=queixa_choices)

    def __str__(self):
        return self.nome

class Tarefas(models.Model):
    frequencia_choices = (
        ('D', 'Diáriamente'),
        ('1S', '1 vez por semana'),
        ('2S', '2 vezes por semana'),
        ('3S', '3 vezes por semana'),
        ('4S', '4 vezes por semana'),
        ('5S', '5 vezes por semana'),
        ('5M', '5 vezes por mês'),
        ('4M', '4 vezes por mês'),
        ('3M', '3 vezes por mês'),
        ('2M', '2 vezes por mês'),
        ('1M', '1 vez por mês'),
        ('N', 'Ao necessitar')
    )

    tarefa = models.CharField(max_length=255)
    instrucoes = models.TextField()
    frequencia = models.CharField(max_length=2, choices=frequencia_choices, default='D')

    def __str__(self):
        return self.tarefa
    
class Consultas(models.Model):
    humor = models.PositiveIntegerField()
    registro_geral = models.TextField()
    video = models.FileField(upload_to="video")
    tarefas = models.ManyToManyField(Tarefas)
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.paciente.nome
    
    @property
    def link_publico(self):
        '''    outra forma: 
        return f"http:///127.0.0.1:8000/{reverse('consulta_publica', kwargs={'id':self.id})}"
                                                       'name'              'parametro':valor
        '''
        return f'http:///127.0.0.1:8000/consulta_publica/{self.id}'
    