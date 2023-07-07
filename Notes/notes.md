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

### tip 2
