class PlayingCard:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):  # "getter" property
        return self._rank
    
    @rank.setter
    def rank(self, value):  # "setter" property
        if isinstance(value, str):
            self._rank = value
        else:
            datatype = type(value).__name__
            raise TypeError(f"Rank must be str, not {datatype}")

    @property
    def suit(self):
        return self._suit
    
    @suit.setter
    def suit(self, value):
        if isinstance(value, str):
            self._suit = value
        else:
            datatype = type(value).__name__
            raise TypeError(f"Suit must be str, not {datatype}")

    def __repr__(self):  # implements repr() for this object
        return f"PlayingCard('{self.rank}', '{self.suit}')"

    def __str__(self):   # implements str() for this object
        return f"Card[{self.rank}:{self.suit}]"


if __name__ == "__main__":
    c1 = PlayingCard("8", "Diamonds")
    c2 = PlayingCard("Q", "Hearts")
    print(f"{c1.rank = }")  # invokes 'rank' property
    print(f"{c2.suit = }")
#    c1.color = "red"
    c1.rank = "K"   #  rank(self, "K")
    # c1.rank = 13   # INVALID

    # def spam():
    #     print("spam!!")

    # spam.color = "blue"
    # print(f"{spam.color = }")
    #  str()  repr()
    print(c1)              # str(c1)
    print(str(c1))         # str(c1)
    print(repr(c1))        # repr(c1)
    print(f"{c1 = }")      # repr(c1)
    print(f"{c1 = !s}")    # str(c1)
    