## Challenge: bug detective

Here is some code which contains 2 bugs.

+ Copy the code and save it with the filenames given, in the same folder.  

+ Add two **assert** statements to the `bugged_card_test.py` file which should pass, but don't.

+ Find and fix the two bugs!

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

--- hints ---
--- hint ---
The first assert statement should be:

```Python
assert card1.suit == "spades"
```

This statement should be True, but will fail. This is because there is a mistake in the `suit` setter method - `"Spades"` has a capital letter, so the input of `"spades"` is seen as invalid, when it should not be.

```Python
if suit in ["hearts", "clubs", "diamonds", "Spades"]:
```

Fix it by replacing the capital `"S"`in `"Spades"` with a lowercase `"s"`.

--- /hint ---
--- hint ---
The second assert statement should be:

```python
assert card1.number == card2.number
```

This statement will also fail, even though `card1`'s number was originally set as 2 and you just changed `card2`'s number to 2 as well. This is because there is a mistake in the `number` setter method - the value of `self._number` is assigned as itself, rather than `number` which is the new number you specified.

```Python
def number(self, number):
        if number in [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]:
            self._number = self._number
```

Fix it by setting `self._number = number` instead.

--- /hint ---
--- /hints ---
