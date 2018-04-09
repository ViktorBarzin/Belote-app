from score_calculator.interfaces import ICard
from interface import implements


class Card(implements(ICard)):
    def get_suit(self) -> str:
        pass

    def get_rank(self) -> str:
        pass
