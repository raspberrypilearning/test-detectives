## When to assert

Now that you know how to use `assert`, it's important to also know **when** to use it.

It is not a good idea to use `assert` to test user inputs. For example, the following use of `assert` doesn't make sense, because you cannot possibly state with certainty what the user will type in:

```python
name = input("Please enter your name: ")
assert name == "Laura"
```

Here are some good ways to use `assert` to test your program:

- `item in list` — assert that a particular item is in a list
- `type(var) is IntType` — assert that a particular variable is an integer
- Checking "can't happen" situations — e.g. assert that there are no duplicates in a list
- After calling a function — assert that the return value of a function is reasonable
- `isinstance(class)` — assert that an object is an instance of a particular class
