from typing import List
from true_false_game.question_cls import Question
from enum import Enum


class GameStatus(Enum):
    GAME_OVER = 0
    IN_PROGRESS = 1


class Game:
    def __init__(self, path: str, errors: int = 3):
        self.__errors_commited = 0
        self.__errors_allowed = errors + 1
        self.__file_path = path
        self.__question_base: List[Question] = []
        self.__current_question = 0
        self.__status = GameStatus.IN_PROGRESS

        self.__set_questions_base(self.__file_path, self.__question_base)

    def __set_questions_base(self, __file_path, __question_base):
        with open(self.__file_path, encoding='utf-8') as file:
            for line in file:
                q = self.__parse_line(line)
                self.__question_base.append(q)

    def __parse_line(self, line) -> Question:
        line = line.strip().split(';')
        text = line[0]
        answer = True if line[1] == 'Yes' else False
        comment = line[2]
        return Question(text, answer, comment)

    def __last_question_passed(self):
        return self.__current_question == len(self.__question_base)

    def game_status(self):
        if self.__errors_commited == self.__errors_allowed or self.__last_question_passed():
            self.__status = GameStatus.GAME_OVER
        return self.__status

    def next_question(self) -> Question:
        return self.__question_base[self.__current_question]

    def isrightanswer(self, answer):
        def answer_to_bool():
            return answer == 'y'
        if not self.__question_base[self.__current_question].answer == answer_to_bool():
            self.__errors_commited += 1
            self.__current_question += 1
            return False
        self.__current_question += 1
        return True

    def game_result(self):
        if self.__errors_commited == self.__errors_allowed:
            return f'You lost! Errors commited: {self.__errors_commited}/{self.__errors_allowed}'
        elif self.__last_question_passed():
            return f'You won!\nQuestions passed: {self.__current_question}\n' \
                   f'Errors commited: {self.__errors_commited}/{self.__errors_allowed}'
