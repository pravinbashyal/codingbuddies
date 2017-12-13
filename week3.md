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
    'universe': 'Hogwards',
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
