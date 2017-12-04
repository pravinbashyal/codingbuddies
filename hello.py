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
