# formatting strings
firstname = 'Vraj'
lastname = 'Gupta'

# each one of these will give the exact same answer

# output = 'Hello, ' + firstname + ' ' + lastname
# output = 'Hello, {} {}'.format(firstname, lastname)
# output = 'Hello, {0} {1}'.format(firstname, lastname)

# only available in Python 3
output = f'Hello, {firstname} {lastname}'
print(output)