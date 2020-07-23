## चुनौती: बग(bug) जासूस

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
from bugged_card import Card

# दो कार्ड तयार करें
card1 = Card("hearts", "2")
card2 = Card("clubs", "A")

# उनके मूल्य प्रिंट करें
print(card1)
print(card2)

# पहले कार्ड का सुट बदलें
card1.suit = "spades"

# ASSERT 1 - card1 अब काला पत्ता है इसकी जाँच करें


# card 2 की संख्या बदलें
card2.number = "2"

# ASSERT 2 - card1 और card2 पर अब समान संख्या होनी चाहिए
```

--- hints ---
 --- hint ---

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

--- /hint ------ /hints ---
