from random import randint
from snakes_ladders.snakesladders_cls import SnakesLadders, Status

game = SnakesLadders()
while game.status != Status.GAME_OVER:
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    print(game.play(die1, die2))
