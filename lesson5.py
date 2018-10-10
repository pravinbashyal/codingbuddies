a = [1,2,3,4]

# map, filter and reduce

def multiplyBy2( num):
    return num * 2

def odd(num) :
    return num % 2 != 0

def sum(currentValue, aggregate):
    return currentValue + aggregate

doublea = map(multiplyBy2, a)

oddNums = filter(odd, a)

sumOfNums = reduce(sum, a, 0)

print(oddNums, doublea, sumOfNums)

