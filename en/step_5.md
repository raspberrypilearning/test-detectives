## When to assert

Now that you know how to use assert, it's important to also know _when_ to use it.

It is not a good idea to use assert to test user inputs into your code. For example, this use of assert doesn't make sense because you cannot possibly state with certainty what the user will type in:

```python
name = input("Please enter your name: ")
assert name == "Laura"
```

Here are some good ways to use assert to test your program:

- `item in list` - Assert that a particular item is in a list
- `type(var) is IntType` - Assert that a particular variable is an integer (or another data type)
- Checking "can't happen" situations - for example asserting that there are no duplicates in a list
- After calling a function - assert that the return value from a function is reasonable
- `isinstance(class)` - Test that an object is an instance of a particular class
