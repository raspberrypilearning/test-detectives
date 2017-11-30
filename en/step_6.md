## Challenge: bug detective 1

Here is some code which contains 2 bugs.

+ Copy the code and save it with the filenames given, in the same folder.  

+ Add two **assert** statements to the `bugged_card_test.py` file which should pass, but don't.

+ Fix the two bugs!

### bugged_card.py
```python
class Card:

    def __init__(self, suit, number):
        self._suit = suit
        self._number = number

    def __repr__(self):
        return self._number + " of " + self._suit

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit):
           if suit in ["hearts", "clubs", "diamonds", "Spades"]:
               self._suit = suit
           else:
               print("That's not a suit!")

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if number in [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]:
            self._number = self._number
        else:
            print("That's not a valid number")

```

### bugged_card_test.py

```python
from bugged_card import Card

# Create two cards
card1 = Card("hearts", "2")
card2 = Card("clubs", "A")

# Print out their values
print(card1)
print(card2)

# Change the suit of the first card
card1.suit = "spades"

# ASSERT 1 - check card1 is now spades


# Change the number of card 2
card2.number = "2"

# ASSERT 2 - card1 and card2 should now have the same number

```
