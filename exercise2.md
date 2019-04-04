# Exercise

write a rock paper scissor program which:
- prompts for user to choose from three options as numbers(1, 2, 3)
- compare it with random move of opponent from code below
- and says 'you won' or 'you lost' based on his input.
- also print opponent's choice as why you lost or won.

```python
from random import randint # we are using something from a package
possibilities = ['rock', 'paper', 'scissor'] # this is an array of three strings
index = randint(0, 2) # generates a random number from 0 to 3
opponentMove  = possibilities[index]

# your code here
```

## resources:

- String Manipulation: https://www.pythonforbeginners.com/basics/string-manipulation-in-python
- Arrays: https://www.programiz.com/python-programming/array
