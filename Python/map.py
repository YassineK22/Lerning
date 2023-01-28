
#List square
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))

#List Upper
words = ["hello","world","map","function"]
uppercase_words = map(lambda x: x.upper(), words)
print(list(uppercase_words))
