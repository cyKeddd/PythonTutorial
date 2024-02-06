# numbers can be stored in variables
pi = 3.14159
print(pi)

# ** mean exponents
# you can do math with numbers using inputs and variables
first_num = 5
second_num = 6
print(first_num + second_num)
print(first_num ** second_num)

# if you combine strings with numbers, python will get confused
# to solve the problem you should be displaying a string that contains numbers you must convert into strings
days_in_feb = 28
print(str(days_in_feb) + ' days in February')

# numbers can be stored as strings
# numbers stored as strings are treated as strings
# if you put these two together then python will add these two and then show it
first_num = '6'
second_num = '2'
print(first_num + second_num)

# the input function will always return a string
first_num = input('Enter first number: ')
second_num = input('Enter second number: ')
print(first_num + second_num)

# numbers stored as strings must be converted to numeric values before doing math
# int will change it to a number before doing math
# float will not change it to a number before doing math
first_num = input('Enter a different number: ')
second_num = input('Enter the second number: ')
print(int(first_num) + int(second_num))
print(float(first_num) + float(second_num))

# numeric values are used for math operations and to specify individual rows in lists and arrays
# price_with_tax = price + price * federal_tax