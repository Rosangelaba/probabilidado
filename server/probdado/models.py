from django.db import models

# Create your models here.
class Combinacao(models.Model):
    dado1 = models.IntegerField()
    dado2 = models.IntegerField()
#    CorDado1 = models.CharField(max_length=10)
#    CorDado2 = models.CharField(max_length=10)

    def __str__(self):
        return "{d1} - {d2}".format(d1 = self.dado1, d2 = self.dado2)

class Dica(models.Model):
    text = models.CharField(max_length=256)
    combinacoes = models.ManyToManyField(Combinacao)

    def __str__(self):
        return self.text

# ------------------------------------------------------------------------------

class Partida(models.Model):
    match = models.OneToOneField('core.Match', on_delete=models.CASCADE, primary_key=True)
    combinacao = models.ForeignKey(Combinacao, on_delete=models.CASCADE)

    def __str__(self):
        return "{match}: {combinacao}".format(match = self.match, combinacao=self.combinacao)

class Rodada(models.Model):
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE)
    dica    = models.ForeignKey(Dica, on_delete=models.CASCADE)
    estado  = models.IntegerField(default=0)  # máquina de estado: 0:aceitando alternativas (respostas) dos players, 1:feedback, 2:encerrado

    def __str__(self):
        return "{d} - {e}".format(d=self.dica, e=self.estado)

class Alternativa(models.Model):
    rodada  = models.ForeignKey(Rodada, on_delete=models.CASCADE)
    texto   = models.TextField(max_length=64)
    correta = models.BooleanField(default=False)
    ponto   = models.IntegerField()  # Regra de negócio: probabilidade 10 pontos, combinação 50 pontos, combinação errada -10 pontos

class Resposta(models.Model):
    # Regra de negócio: Protect against multiple selection during the same "Rodada" -- code this rule.
    player      = models.ForeignKey('core.Player', on_delete=models.CASCADE)
    alternativa = models.ForeignKey(Alternativa, on_delete=models.CASCADE)



