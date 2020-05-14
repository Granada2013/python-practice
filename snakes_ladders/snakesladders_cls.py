from enum import Enum


class Status(Enum):
    IN_PROGRESS = 1
    GAME_OVER = 0


class SnakesLadders:
    UPS_DOWNS = {2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 78: 98, 87: 94,
                 16: 6, 46: 25, 49: 11, 62: 19, 64: 60, 74: 53, 89: 68, 92: 88, 95: 75, 99: 80}

    def __init__(self):
        self.position_1 = self.position_2 = 0
        self.turn = 1
        self.status = Status.IN_PROGRESS

    @staticmethod
    def is_double(die1, die2):
        return die1 == die2

    def switch_turn(self):
        self.turn = 1 if self.turn == 2 else 2

    def play(self, die1: int, die2: int):
        if any((i == 100 for i in (self.position_1, self.position_2))):
            self.status = Status.GAME_OVER
            return "Game over!"

        position = self.position_1 if self.turn == 1 else self.position_2
        position += (die1 + die2)
        x = self.turn

        if position > 100:
            position = (200 - position)
        if position in SnakesLadders.UPS_DOWNS:
            position = SnakesLadders.UPS_DOWNS[position]
        if self.turn == 1:
            self.position_1 = position
        else:
            self.position_2 = position

        if not self.is_double(die1, die2): self.switch_turn()
        return f"Player {x} Wins!" if position == 100 else f"Player {x} is on square {position}"