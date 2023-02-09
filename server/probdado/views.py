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


#~ class Main(TemplateView):
    #~ template_name = 'probdado/main.html'


class Main(TemplateView):
    template_name = 'probdado/main.bkp.htmHttpResponsel'



class View_Rodada(DetailView):
    template_name = 'probdado/main.html'
    model = Rodada

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()  # rodada
        #~ self.rodada = Rodada.objects.filter(partida=self.object).filter(Q(estado=0) | Q(estado=1)).get() #aceitando resposta ou feedback
        context = self.get_context_data()
        return self.render_to_response(context)
#~ self.combinacao = self.object.combinacao
#~ self.dicas      = self.combinacao.dica_set.all()


class View_NovaCombinacao(View):
    def get(self, request, *args, **kwargs):
        game = Game.objects.filter(app='probdado').get()

        room_pk = self.kwargs.get('room_pk')
        room = Room.objects.filter(pk=room_pk).get()

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
        #~ return HttpResponse("DONE!")


#~ class View_NovaRodada(View):
    #~ pass


