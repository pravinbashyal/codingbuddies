write a program for Rock Paper Scissor Lizard Spock.

Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
(and as it always has) Rock crushes Scissors

Requirements:
- program asks user for one of five options
- the response from the program is selected at random. hint below
    ```python
from random import randint # we are using something from a package
randint(0, 6) # generates a random number from 0 to 6
    ```
- the program has 10 retries for the user.
- if the score is greater than 5, the user wins.

# any kind of enhancement is a plus.
