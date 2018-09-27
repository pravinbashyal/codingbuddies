from random import randint # we are using something from a package random

random_digit= randint(0, 9) # generates a random number from 0 to 9

computerGuessedNumber = []

for i in range(3):
    computerGuessedNumber.append(randint(0,9))

print(computerGuessedNumber)

while True:
    userGuessedNumber = input('guess the three digit number: ')
    userGuessedNumber = list(userGuessedNumber)
    numberOfCorrectDigits = 0
    numberOfCorrectPositions = 0
    for c_pos, c_digit in enumerate(computerGuessedNumber):
        for u_pos, u_digit in enumerate(userGuessedNumber):
            if (str(c_digit ) == str(u_digit)):
                numberOfCorrectDigits = numberOfCorrectDigits + 1
                if(c_pos == u_pos):
                    numberOfCorrectPositions = numberOfCorrectPositions + 1
    print('you guessed \n' + str(numberOfCorrectDigits )+ ' digits correctly \n' + str(numberOfCorrectPositions) + ' positions correctly')
    if(numberOfCorrectDigits == 3 and numberOfCorrectPositions == 3) :
        print('you win')
        break
