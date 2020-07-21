## चुनौती: बग जासूस

यहां कुछ कोड है जिनमें दो बग हैं।

+ दिए गए फ़ाइल के नामों से और एक ही फ़ोल्डर(folder) में, कोड के दो वर्गों को अलग से कॉपी(copy) और सेव करें।

+ दो `assert` विवरणों को `bugged_card_test.py` को जोड़ें जो की पास होने चाहिए, लेकिन दो बग्स के कारण नहीं होंगे। जहां यह `ASSERT` कहता है वहाँ जोड़ें।

+ बग(bug) को ढूंढें और ठीक करें!

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
Challenge: bug detective
चुनौती: बग जासूस
चुनौती: बग जासूस
Here is some code containing two bugs.
यहां कुछ कोड है जिनमें दो बग हैं।
यहां कुछ कोड है जिनमें दो बग हैं।
Copy and save the two sections of code separately, with the file names given and in the same folder.
दिए गए फ़ाइल के नामों से और एक ही फ़ोल्डर(folder) में, कोड के दो वर्गों को अलग से कॉपी(copy) और सेव करें।
दिए गए फ़ाइल के नामों से और एक ही फ़ोल्डर(folder) में, कोड के दो वर्गों को अलग से कॉपी(copy) और सेव करें।
Add two <0>assert</0> statements to the <0>bugged_card_test.py</0> file which should pass, but don't, because of the two bugs.
दो <0>assert</0> विवरणों को <0>bugged_card_test.py</0> को जोड़ें जो की पास होने चाहिए, लेकिन दो बग्स के कारण नहीं होंगे।
दो <0>assert</0> विवरणों को <0>bugged_card_test.py</0> को जोड़ें जो की पास होने चाहिए, लेकिन दो बग्स के कारण नहीं होंगे।
Add them where it says <0>ASSERT</0>.
जहां यह <0>ASSERT</0> कहता है वहाँ जोड़ें।
जहां यह <0>ASSERT</0> कहता है वहाँ जोड़ें।
Find and fix the bugs!
बग(bug) को ढूंढें और ठीक करें!
बग(bug) को ढूंढें और ठीक करें!
bugged_card.py
bugged_card.py
bugged_card.py
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
@property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if number in [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]:
            self._number = self._number
        else:
            print("That's not a valid number")
@property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if number in [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]:
            self._number = self._number
        else:
            print("That's not a valid number")
bugged_card_test.py
bugged_card_test.py
bugged_card_test.py
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

--- hints --- --- hint ---

पहला `assert` विवरण होना चाहिए:

```Python
assert card1.suit == "spades"
```

यह विवरण सही होना चाहिए, लेकिन असफल होगा। ऐसा इसलिए है क्यों की `suit`: में गलती है `"Spades"` में एक कैपिटल अक्षर है, तो फिर यह इनपुट `"spades"` अमान्य देखा जाता है जबकि ऐसा नहीं होना चाहिए।

```Python
if suit in ["hearts", "clubs", "diamonds", "Spades"]:
```

`"Spades"` में बड़े `"S"` के साथ छोटा `"s"` को बदलकर ठीक करें।

--- /hint --- --- hint ---

दूसरा `assert` विवरण होना चाहिए:

```python
assert card1.number == card2.number
```

यह विवरण भी विफल हो जाएगा, भले ही `card1` की संख्या मूल रूप से `2` सेट की गयी थी और आपने अभी `card2` की संख्या को `2` में बादल दिया। ऐसा इसलिए है क्यों की `number` setter method: में गलती है `self._number` को दीया गया मूल्य `number` के बजाय स्वयं है, जो आपके द्वारा निर्दिष्ट की हुई संख्या है:

```Python
def number(self, number):
        if number in [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]:
            self._number = self._number
```

इसकी बजाय इसे `self._number = number` पर सेट करके ठीक करें।

--- /hint --- --- /hints ---
