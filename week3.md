## revision

### lists

- intro
- list operations: append, extend, insert, remove, pop, clear, count, etc
```python
numbers = [1,2,3]
1 in numbers # True
'apple' in numbers # True

numbers.append(4) # [1,2,3,4]
numbers.extend([5,6]) # [1,2,3,4,5,6]
numbers.count() # 6

```
- list loop
``` python
for variable in list:
  # do some stuff with variable
  print(variable)

```
- dictionaries
```python
dictionaryLiterally = {
  'type': 'real dictionary',
  'noOfWords': 9997,
  'words': ['yesterday', 'all', 'my', 'troubles', 'seemed', 'so', 'far', 'away']
  }
```

- function: definition, return
```python
nicknames = {
  'Aegon': 'The conquerer',
  'Vlad': 'The Impaler'
  }


def shoutNickNames(name):
  print('HEY!!! 'name + ' ' + nicknames[name], '. ssup!')


shoutNickNames('Aegon')
shoutNickNames('Vlad')

# return integer
def square(num):
  return num ** 2

print(square(2))
print(square(4))
```

## lambdas and use cases
- inline functions without names
```python
[1,2,3]
listOfCharacters = [
  {
    'name': 'Harry Potter',
    'universe': 'Hogwards',
    'nemesis': ['Voldemort', 'Draco'],
    'role': 'hero',
    'says': 'Expecto Patronas!!'
  },
  {
    'name': 'Anakin',
    'universe': 'Star Wars',
    'nemesis': ['Luke', 'Obi']
    'role': 'villain',
    'says': 'I am your father'
  },
  {
    'name': 'Jon Snow',
    'universe': 'Westeros',
    'nemesis': ['Cersie', 'Ice King']
    'role': 'hero',
    'says': 'I know nothing',
    }
]
roles = map(lambda person: person['role'], listOfCharacters)
print(roles)
heroes = filter(lambda person: person['role'] == 'hero')
print(heroes)
```

# functional programming, map, filter, reduce

## map
map(f, iterA, iterB, ...)

```python
def upper(s):
  return s.upper()

>>> map(upper, ['sentence', 'fragment'])
['SENTENCE', 'FRAGMENT']
>>> [upper(s) for s in ['sentence', 'fragment']]
['SENTENCE', 'FRAGMENT']

```

## filter

filter(predicate, iter) returns a list that contains all the sequence elements that meet a certain condition, and is similarly duplicated by list comprehensions. A predicate is a function that returns the truth value of some condition; for use with filter(), the predicate must take a single value.

filter()
```python
def is_even(x):
  return (x % 2) == 0
>>> filter(is_even, range(10))
[0, 2, 4, 6, 8]
This can also be written as a list comprehension:
```

## reduce
reduce(func, iter, [initial_value]) doesn’t have a counterpart in the itertools module because it cumulatively performs an operation on all the iterable’s elements and therefore can’t be applied to infinite iterables. func must be a function that takes two elements and returns a single value. reduce() takes the first two elements A and B returned by the iterator and calculates func(A, B). It then requests the third element, C, calculates func(func(A, B), C), combines this result with the fourth element returned, and continues until the iterable is exhausted. If the iterable returns no values at all, a TypeError exception is raised. If the initial value is supplied, it’s used as a starting point and func(initial_value, A) is the first calculation.

```python
>>> import operator
>>> reduce(operator.concat, ['A', 'BB', 'C'])
'ABBC'
>>> reduce(operator.concat, [])
Traceback (most recent call last):
  ...
TypeError: reduce() of empty sequence with no initial value
>>> reduce(operator.mul, [1,2,3], 1)
6
>>> reduce(operator.mul, [], 1)
1
```

# Resources
https://docs.python.org/2/howto/functional.html
