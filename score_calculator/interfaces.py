from interface import Interface
from typing import List


class ICard(Interface):
    def get_suit(self) -> str:
        pass

    def get_rank(self) -> str:
        pass


class IGame(Interface):
    pass


class Rules(Interface):
    def get_value_of(card: ICard) -> int:
        pass

    def get_bonus_points(cards_list: List[ICard]) -> int:
        '''
        Returns an integer representing bonus points if any for possessing the input cards.
        '''
        pass
