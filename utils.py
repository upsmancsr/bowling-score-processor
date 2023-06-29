from .models import Game, Frame

# this function does the logical operations for game score (note: a game is a game for one player)
def calculate_scores(game_id):
    game = Game.objects.get(pk=game_id)
    frames = Frame.objects.filter(game=game)
    rolls = [frame.roll for frame in frames]
    score = 0
    return score
