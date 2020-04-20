from dataclasses import dataclass


@dataclass(frozen=True)
class Question:
    text: str
    answer: bool
    comment: str
