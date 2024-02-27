price = input('how much did you pay? ')

price = float(price)
if price >= 1.00:
    tax = .07
else:
    tax = 0
print('Tax rate is: ' + str(tax))

#case sensitivity
country = input('Enter the name of your home country: ')
if country.lower() == 'india':
    print('So you must like samosas!')
else:
    print('You are not form India')
