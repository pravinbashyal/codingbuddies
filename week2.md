
# revision

## data types
    - primitive: string, numbers(int and float), boolean(True, False)

## operators
    - arithmetic: +, -, /, *, ** , %
    - boolean: and, or
    - comparison: ==, <=, >=, !=

## brief intro to function and return types

## brief intro to control statements: if

# agenda for today

## immutable and mutable

## lists
    - list intro
    - list operations: slicing, concatenation, append, len

## if statement revisited
    ```python
        if <condition>:
            # execute something
        elif <condition2>:
            # execute something else
        else:
            # execute last resort/ goto option/ default behavior
    ```

## loops
    - while loop:
        - pairs best when there is no predefined number of iterations.

```python
while <condition>:
    # do something
    # new condition arises
    # loop will terminate of re run

# example
from random import randint # we are using something from a package

possibilities = [True, True, False, True, False, False, True, True, True, False, True, True, True]
raoulJohnAndMarkusLunchTimeIsNotFree = possibilities[1]

while raoulJohnAndMarkusLunchTimeIsNotFree:
    print('Ask: (^o^)／ Oh hoy fellas, ready for coding buddies?')
    raoulJohnAndMarkusLunchTimeIsNotFree = possibilities[randint(0, possibilities.len() -1 )]
    if raoulJohnAndMarkusLunchTimeIsNotFree:
        print('(；一_一) Sorry man we have something far important than coding buddies.')
    else:
        print('ヽ(^。^)ノヽ(^o^)丿＼(^o^)／     ヽ(´ー｀)┌')
```
    - for loop:
        - pairs best with lists or if something has finite number of iterations

```python
days = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' ]
moods = [
    'Arrgh. boy here we go again',
    'why is time so slow',
    'made it half way through',
    'yayy football. looking fwd to the weekend',
    'beer and pizza guys, beer and pizza',
    'this is going to be awesome weekend',
    'shit its almost over'
]

for day in days:
    print('today is ' + day)

for i in range(days.len()-1):
    print(moods[i] '. its ' + days[i])
```

## break and continue

`break` breaks out of the current loop </br>

whereas `continue` disregards the code flow that follows current iteration and continues with the loop

``` python
distances = ['here', 'there', 'sky', 'at moon', 'inifinity and beyond']

def skyIsTheLimit:
  for distance in distances:
    print('i\'m ' + distance)
    if distance == 'sky':
      print('sky is my limit')
      break

def skipMoon:
  for distance in distances:
    if distance == 'at moon':
      continue
    print('i\'m ' + distance)

```

## tuples

- like lists but immutable
```python
tuppleWare = ('some', 'random', 'collection')
```

## functions

```python
def functionName(arguments):
  # do function stuffs
  # return or not return
```
