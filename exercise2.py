# The below script will ask for 3 inputs. Each input will be based
# on the price of the items - the price is determined by you. The output
# should print the total of the 3 inputs rounded to 2 decimal places e.g
#
#   1 coffee @ $ 2.00
#   1 sandwich @ $ 4.99
#   1 cake @ $ 2.75
#
#   Your total bill is $ 9.74

# Modify the line below
name = str(input("Please enter your name: "))
age = int(input("Please enter your age: "))
if age >= 18:
    print('You are welcome to our Restaurant')
else:
    print('You are too young to come here!')
coffee = float(input('1 coffee @: $ '))

# Modify the line below
sandwich = float(input('1 sandwich @: $ '))

# Modify the line below
cake = float(input('1 cake @: $ '))

bill_total = coffee + sandwich + cake

print('Your total bill is $', bill_total)
print("Thanks for your Patronage. Please Call again Mr/Miss/Mrs {}".format(name))