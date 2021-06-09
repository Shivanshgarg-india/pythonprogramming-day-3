def FirstThree():
    yield 1yield 2yield 3

# main function to print the values
numbers = FirstThree()
for res in numbers:
    print (res, end = ' ')
