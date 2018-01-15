## To log or not to log

Logging is useful because you can change the level of detail for messages you wish to see. Here are the possible levels, going from most detail to least:

![Level table](images/level-table.png)

_Information from [Python Logging How To](https://docs.python.org/3.6/howto/logging.html#logging-advanced-tutorial){:target="_blank"}_

Instead of using `logger.debug()`, you can log messages at different levels, for example `logger.info()`, `logger.warning()`, `logger.error()`, or `logger.critical()`.

When you are debugging your program, you will want to set the level of the logger to `DEBUG` to get the most information. However, once your program is finished, you probably don't want to see so much information.

+ In `card.py`, change the level of the logger to `CRITICAL`:

```python
logger.setLevel(level=logging.CRITICAL)
```

+ Run the `log_test.py` program again. You will no longer see any log messages, because you have asked to only see the most important (critical) messages. Since you didn't add any `logger.critical()` messages to your program, there is nothing to show.

+ Change your logging level back to `DEBUG`.
