from playingcard import PlayingCard
from carddeck import CardDeck

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()  # call method in base (parent) class
        for num in 1, 2:
            card = PlayingCard(f"Joker{num}", "*** JOKER ***")
            self._cards.append(card)

if __name__ == "__main__":
    j1 = JokerDeck()
    j1.shuffle()
    print(f"{j1.cards = }")
