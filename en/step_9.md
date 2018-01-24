## Challenge: log detective

+ Download the [`deck.py`](resources/deck.py) file and add it to the same folder as your `card.py` and `log_test.py` files.

+ Add a logger with the level `DEBUG` to the `deck.py` file.

+ Add a log `info()` statement to record whenever a deck object has been created.

+ Inside your `log_test.py` file, import the `Deck` class:

```python
from deck import Deck
```

+ Then, create a deck object:

```python
deck = Deck()
```

+ Run the program. Now you should see information that the deck was created, in addition to the debug statement about the invalid suit.

![Info log](images/info-log.png)
