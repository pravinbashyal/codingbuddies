from random import randint # we are using something from a package random

random_digit= randint(0, 9) # generates a random number from 0 to 9

computerGuessedNumber = []

for i in range(3):
    computerGuessedNumber.append(randint(0,9))

print(computerGuessedNumber)

while True:
    userGuessedNumber = input('guess the three digit number: ')
    conaosdifjaosidjf
