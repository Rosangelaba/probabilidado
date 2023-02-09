import random

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.forms.models import model_to_dict
from django.urls import reverse
from django.db.models import Q

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Combinacao, Dica, Partida, Rodada, Alternativa, Resposta
from core.models import Game, Room, Match

# Create your views here.

class Main(TemplateView):
    template_name = 'probdado/main.bkp.html'

class View_Rodada(DetailView):
    template_name = 'probdado/main.html'
    model = Rodada

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()  # rodada
        context = self.get_context_data()
        return self.render_to_response(context)


class View_Revelar(View):
    def get(self, request, *args, **kwargs):
        rodada_pk = self.kwargs.get('rodada_pk')
        rodada = Rodada.objects.filter(pk=rodada_pk).get()
        rodada.estado = 1
        rodada.save()

        url = reverse('probdado:rodada', kwargs={'pk': rodada.pk})
        return HttpResponseRedirect(url)



class View_NovaCombinacao(View):
    def get(self, request, *args, **kwargs):
        game = Game.objects.filter(app='probdado').get()

        room_pk = self.kwargs.get('room_pk')
        room = Room.objects.filter(pk=room_pk).get()

        # TODO? provavelmente não: por enquanto pode selecionar combinação já usada nesta sala: Mas não é necessariamente um problema!
        offset = random.randint(0, 35)
        combinacao = Combinacao.objects.all()[offset:offset+1].get()

        match = Match(game=game, room=room, active=True)
        match.save()

        partida = Partida(match=match, combinacao=combinacao)
        partida.save()

        dicas = combinacao.dica_set.all()
        num_dicas = dicas.count()

        offset = random.randint(0, num_dicas-1)
        dica = Dica.objects.all()[offset:offset+1].get()

        rodada = Rodada(partida=partida, dica=dica, estado=0)
        rodada.save()

        # TODO Criar alternativas

        url = reverse('probdado:rodada', kwargs={'pk': rodada.pk})
        return HttpResponseRedirect(url)


class View_NovaRodada(View):
    def get(self, request, *args, **kwargs):
        match_pk = self.kwargs.get('match_pk')
        match = Match.objects.filter(pk=match_pk).get()

        partida = Partida.objects.filter(match=match).get()

        partida.rodada_set.update(estado=2)

        combinacao = partida.combinacao
        dicas = combinacao.dica_set.all()
        num_dicas = dicas.count()

        # TODO?: por enquanto pode selecionar dica já usada por esta combinação nesta sala: Problema? Talvez não.
        offset = random.randint(0, num_dicas-1)
        dica = Dica.objects.all()[offset:offset+1].get()

        rodada = Rodada(partida=partida, dica=dica, estado=0)
        rodada.save()

        # TODO Criar alternativas

        url = reverse('probdado:rodada', kwargs={'pk': rodada.pk})
        return HttpResponseRedirect(url)


