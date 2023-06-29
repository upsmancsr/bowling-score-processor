from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=200)

class Game(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

class Frame(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(null=True, blank=True)
