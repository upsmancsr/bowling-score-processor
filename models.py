from django.db import models


# As examples, here are the models that could be used keep track of scores and persists scores throughout a game.
# Each of these Django models would correspond to a database table.

# Player model to represent each player. A Player might play multiple games.
class Player(models.Model):
    name = models.CharField(max_length=200)


# Game model for each game played, where one game came corresponds to one player.
class Game(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)


# Frame model for each frame in a player's game. Each frame has a foreign key tying it to a game. 
# The number is the frame number within the game.
# The Score is the score for the frame
class Frame(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    score = models.PositiveIntegerField(null=True, blank=True)


# Roll model for each roll a player makes. Each roll corresponds to a frame.
# The number indicates which roll (1 or 2) within the frame.
# pins_knocked_down, is_strike, and is_spare are self explanatory
class Roll(models.Model):
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    pins_knocked_down = models.PositiveIntegerField()
    is_strike = models.BooleanField(default=False)
    is_spare = models.BooleanField(default=False)
