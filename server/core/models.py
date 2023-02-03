from django.db import models

from django.contrib.auth.models import AbstractUser

from core import utils

class User(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username


class Game(models.Model):
    name = models.CharField(max_length=64)
    app = models.CharField(max_length=32)
    max_players = models.IntegerField(default=4)


class Room(models.Model):
    owner    = models.ForeignKey(User, on_delete=models.CASCADE)
    code     = models.CharField(max_length=16)  # (64 + 8) / 5 = 14.4
    active   = models.BooleanField(default=True)

    def create_room(self, game, owner):
        pass


class Player(models.Model):
    # YKL: check how to do it with sessions!
    room = models.ManyToManyField(Room)
    active   = models.BooleanField(default=True)


class Match(models.Model):
    room   = models.ForeignKey(Room, on_delete=models.CASCADE)
    game   = models.ForeignKey(Game, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)


class Score(models.Model):
    match  = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    score  = models.IntegerField(default=0)




