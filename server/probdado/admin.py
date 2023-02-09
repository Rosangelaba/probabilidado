from django.contrib import admin

from . import models
# Register your models here.
admin.site.register(models.Combinacao)
admin.site.register(models.Dica)

admin.site.register(models.Partida)
admin.site.register(models.Rodada)
admin.site.register(models.Alternativa)
admin.site.register(models.Resposta)
