# Tips

### tip 1
However, what if you wanted to get a list of `(value, key)` pairs instead?
*Hint: use `zip()`.*

```python
>>> pricelist = list(zip(prices.values(),prices.keys()))
>>> pricelist
[(490.1, 'GOOG'), (23.45, 'AA'), (91.1, 'IBM'), (34.23, 'MSFT')]
>>>
```

Why would you do this? For one, it allows you to perform certain kinds
of data processing on the dictionary data.

```python
>>> min(pricelist)
(23.45, 'AA')
>>> max(pricelist)
(490.1, 'GOOG')
>>> sorted(pricelist)
[(23.45, 'AA'), (34.23, 'MSFT'), (91.1, 'IBM'), (490.1, 'GOOG')]
>>>
```

This also illustrates an important feature of tuples. When used in
comparisons, tuples are compared element-by-element starting with the
first item. Similar to how strings are compared
character-by-character.

### Argument Passing

When you call a function, the argument variables are names that refer
to the passed values. These values are NOT copies (see [section
2.7](../02_Working_with_data/07_Objects.md)). If mutable data types are
passed (e.g. lists, dicts), they can be modified *in-place*.

```python
def foo(items):
    items.append(42)    # Modifies the input object

a = [1, 2, 3]
foo(a)
print(a)                # [1, 2, 3, 42]
```

**Key point: Functions don't receive a copy of the input arguments.**

### Reassignment vs Modifying

Make sure you understand the subtle difference between modifying a
value and reassigning a variable name.

```python
def foo(items):
    items.append(42)    # Modifies the input object

a = [1, 2, 3]
foo(a)
print(a)                # [1, 2, 3, 42]

# VS
def bar(items):
    items = [4,5,6]    # Changes local `items` variable to point to a different object

b = [1, 2, 3]
bar(b)
print(b)                # [1, 2, 3]
```

*Reminder: Variable assignment never overwrites memory. The name is merely bound to a new value.*
