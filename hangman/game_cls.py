import random
from enum import Enum
from typing import List


class GameStatus(Enum):
    IN_PROGRESS = 1
    IS_WON = 0
    IS_LOST = -1


class Game:
    def __init__(self, errors: int = 10):
        self.__word: str = ''
        self.__errors_left: int = errors
        self.__letters_tried: List[str] = []
        self.__game_status: GameStatus = GameStatus.IN_PROGRESS

        self.__generate_word()

    @property
    def letters_tried(self) -> str:
        return ', '.join(sorted(self.__letters_tried))

    @property
    def errors_left(self) -> int:
        return self.__errors_left

    def __generate_word(self) -> str:
        if not self.__word:
            with open('words_dict.txt', encoding='utf-8') as file:
                cnt = 0
                for _ in file:
                    cnt += 1
                file.seek(0)
                words = (line.strip() for line in file)
                for _ in range(random.randrange(cnt)):
                    word = next(words)
                self.__word = word
        return self.__word

    def get_state(self) -> str:
        state = []
        for letter in self.__word:
            if letter in self.__letters_tried:
                state.append(letter)
            else:
                state.append('_')
        return ' '.join(state)

    def try_letter(self, letter: str):
        self.__letters_tried.append(letter)
        if letter not in self.__word:
            self.__errors_left -= 1

    def isduplicate(self, letter: str) -> bool:
        return letter in self.letters_tried

    def status(self) -> GameStatus:
        if self.__errors_left == 0:
            self.__game_status = GameStatus.IS_LOST
        elif '_' not in self.get_state():
            self.__game_status = GameStatus.IS_WON
        return self.__game_status

    def show_word(self) -> str:
        if self.__game_status != GameStatus.IN_PROGRESS:
            return self.__word
