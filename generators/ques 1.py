# A simple generator function that yields the first three numbers.

def FirstThree():
  yield 1yield 2yield 3
# main function to print the values
for res in FirstThree():
  print (res, end = ' ')