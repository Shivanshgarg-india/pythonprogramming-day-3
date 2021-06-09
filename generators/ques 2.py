# create a generator object for the generator function using which the values of the generator function can be accessed

def FirstThree():
    yield 1yield 2yield 3

# main function to print the values
numbers = FirstThree()
print(next(numbers))
print(next(numbers))
print(next(numbers))