#  Remove all of the vowels in a string
string = 'my anme is shivansh '
answer = "".join([char for char in string if char not in ["a","e","i","o","u"]])