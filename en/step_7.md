## Logging

Let's look at another piece of the `Card` class code: the setter method for the suit property.

```python
@suit.setter
def suit(self, suit):
       if suit in ["hearts", "clubs", "diamonds", "spades"]:
           self._suit = suit
       else:
           print("That's not a suit!")
```

If the user tries to set a suit which is not in the list, at the moment the code prints out `"That's not a suit"`. If we use this class in a real card game program, it would be helpful to be notified when something unexpected is being assigned as a suit. However, we wouldn't necessarily want the player to be notified as well.

Instead of using the `print` function to report the error, we could log it instead.

+ Open the `card.py` file you wrote or downloaded, which contains the code for the `Card` class.

+ At the top of the file, add a line of code to import the `logging` module. This is a standard Python module, so you won't need to install anything extra.

```python
import logging
```

+ Below that, set up your logger. The first line creates the logger, and `__name__` will log which file the problem occurred in. The second line sets how much information you want to see: `DEBUG` is the most detailed level of information. We will discuss these level settings further in the next step.

```Python
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)
```

+ Replace the `print` statement with a statement which logs debug information:

```python
logger.debug("Invalid suit - " + str(suit) )
```

Next, let's test what this looks like when you run the program and set an invalid suit.

+ Create a new file and save it as `log_test.py` in the same folder as your `card.py` code.

+ In the `log_test` file, add some code to import the `Card` class and the `logging` module:

```Python
from card import Card
import logging
```

+ Add a line of code to specify the lowest level of message you would like to see. In this case, we would like to see debug messages.

```python
logging.basicConfig(level=logging.DEBUG)
```

+ Now create a card and try to set an invalid suit:

```python
my_card = Card("hearts", "6")
my_card.suit = "blobs"
```

+ Run the code and you will see a debug message:

![Bad suit](images/bad-suit.png)

Note that the information provided also tells you the file where the logged issue occurred: `card`, i.e. `card.py`.

+ You can improve your logging message by adding more detailed information, for example:

```python
logger.debug("Tried to set an invalid suit (" + str(suit) + ") for " + repr(self) )
```
