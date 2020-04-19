# name = input('what is your name? ')
# color = input('what is your favourite color? ')
# print(name + ' likes '+ color)

# birth_year = input('birth year:')
# print(type(birth_year))
# age = input(2019 - int(birth_year))
# print(age)


# user_wieght_pound = input('what is your weight in pounds? ')
# convert = 0.45
# Weight_kilogram = input(convert * float(user_wieght_pound))
# print(Weight_kilogram)

# email = '''
# Hi Sam,

# We received your request. I will update you once it resolved.

# Thanks
# The Support Team
# '''
# print(email)

# course = 'Python for Begginers'
# another = course[:]
# print(course[1:-1])


# first = 'Gurpreet'
# last = 'Singh'
# msg = f'{first} [{last}] is a coder'
# print(msg)

# course = 'Python for Begginers'
# print(course.replace('g','t'))
# print(course.find('t'))

# course = 'python for beginners'
# print(course.title())

# //Augmented Assignment Operator//
# x = 10
# x += 3
# print(x)

# Operator Precedence
# Exponentiation 2 ** 3
# multiplication or division 
# addition or subtraction

# x = 8.45
# print(abs(-90.9))

#import math module 

# import math 
# print(math.ceil(2.9))
# print(math.floor(5.4))


# //-----------------IF Function-----------//

# is_hot = False
# is_cold = False

# if is_hot:
#     print("It's hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
#     pass

# else:
#     print("It's lovely day")
# print('Enjoy your day')

# House_price = 1000000
# credit_score = False
# if credit_score:
#     print((House_price/100) * 10)
# else:
#     print((House_price/100) * 20)

# print("Down Payment")
#=====================mosh solution=======================
price = 1000000
has_good_credit = False
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(f"Down Payment: ${down_payment}")


