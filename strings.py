# strings can be stored in variables
first_name = 'Vraj'
print(first_name)

# you can combine strings with +
first_name = 'Vraj'
last_name = 'Gupta'
print(first_name+last_name)
print('Hello ' + first_name + ' ' + last_name)

# you can use functions to modify strings
sentence = 'Vraj is smart'
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('a'))

# functions help us format strings we save to files and databases, or display to users
first_name2 = input('what is your first name bro: ')
last_name2 = input('what is your last name bro: ')
print('Hello ' + first_name2.capitalize() + ' ' + last_name2.capitalize())