# syntax errors
# easy to track down
# this code will not run at all
# go to the problems section on the terminal
# you can see the syntax error
x = 42
y = 206
if x == y:
    print('Success!!')

# runtime errors
# this cdoe will when run
x = 42
y = 0
print(x / y)

# catching runtime errors
# something is wrong with this code pls help in the github repository
try: 
    print(x / y)
except ZeroDivisionError as e:
    # optimally, log e somewhere
    print('Sorry something went wrong')
except:
    print('Something really went wrong')
finally: 
    print('This always runs on success or failure')
    