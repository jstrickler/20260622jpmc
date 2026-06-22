import random
from playingcard import PlayingCard

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self):
        self._make_deck()
    
    def _make_deck(self):
        self._cards = []   # list of cards
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = PlayingCard(rank, suit)
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @property
    def cards(self):
        return self._cards
    
    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}()"
    
    def __str__(self):
        class_name = type(self).__name__
        return f"{class_name}/{len(self)}"

    def __len__(self):
        return len(self.cards)
    
    @classmethod
    def get_suits(cls):  # CLASS method
        return cls.SUITS

if __name__ == "__main__":
    d1 = CardDeck()
    d2 = CardDeck()
    d1.shuffle()
    print(f"{d1.cards = }")
    print(f"{d1 = }")
    print(f"{d1 = !s}")
    print(f"{d1.get_suits() = }")
    print(f"{CardDeck.get_suits() = }")
    

