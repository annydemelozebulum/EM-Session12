import random


class Card:
    SUITS = ["♣", "♦", "♥", "♠"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, suit, rank):
        if suit not in self.SUITS:
            raise Exception(f"Invalid Suit, needs to be one of: {self.SUITS}")
        if rank not in self.RANKS:
            raise Exception(f"Invalid Rank, needs to be one of: {self.RANKS}")
        self._rank = rank
        self._suit = suit

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    #need to be able to print card

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __repr__(self):
        return self.__str__()

class Deck:
    def __init__(self):
        cards = []
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                cards.append(Card(suit=suit, rank=rank))
        cards = tuple(cards)
        self._cards = cards

    def shuffle(self):
        cards = list(self.cards)
        random.shuffle(cards)
        self._cards = tuple(cards)

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self.cards)




card = Card("♦","K")
print(card)

card2 = Card(rank="2", suit="♣")
print(card2)

cards_list = [card, card2]
print(cards_list)

deck = Deck()
deck.shuffle()
print(deck)



