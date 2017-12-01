## Logging

Let's look at another piece of the `Card` class code - the setter method for the suit property:

```python
@suit.setter
def suit(self, suit):
       if suit in ["hearts", "clubs", "diamonds", "spades"]:
           self._suit = suit
       else:
           print("That's not a suit!")
```

If the user tries to set a suit which is not in the list, at the moment the code prints out `"That's not a suit"`. If this class were to be used in a real card game program, it would be important to know that something unexpected was being assigned as a suit, but we wouldn't necessarily want the player to have to see this message.

Instead of using the `print` function to report the error, we could log it instead.

+ Open your `card.py` file which should contain the code for the `Card` and `Deck` classes.

+ At the start of the file add this line of code to import the logging module. This module is installed with Python by default so you shouldn't need to install anything extra.

```python
import logging
```

+ Replace the `print` statement with a warning statement:

```python
logging.warning("Invalid suit - " + str(suit) )
```
