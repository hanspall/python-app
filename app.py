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

#=====================mosh solution=======================
# price = 1000000
# has_good_credit = False
# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price

# print(f"Down Payment: ${down_payment}")

#================================Logic Operators========================================
###-----AND-------#### /// Both conditoin will be true ///
# has_high_income = True
# has_good_credit = False

# if has_high_income and has_good_credit:
#     print("Eligible for loan")


###-----OR------#### /// At Least one condition should be true ///
# has_high_income = True
# has_good_credit = False

# if has_high_income or has_good_credit:
#     print("Eligible for loan")

###----NOT-----#####

#if applicant has good credit and doesn't have a criminal record.

# has_good_credit = True
# has_criminal_record = False #/True

# if has_good_credit and not has_criminal_recoranswerd:
#     print("Eligible for loan")

#=================Comparison Operators==============================
###------- greater ( > ) ---------------------###
###------- greater than equal to ( >= ) ------###
###------- Less Than ( < ) -------------------###
###------- Less Than Equal to ( <= ) ---------###
###------- Equality Operater ( == ) ----------###
###------- Not Equal To ( != ) ---------------###

# temprature = 35
# if temprature > 30:
#     print("It's hot day")
# else:
#     print("It's not a hot day")

#------------------Excercise_-------------------
#practice - If name is less than 3 chracters long than print name must be at leat 3 characters
#otherwise if it's more than 50 characters long than print name can be maximum of 50 characters
#otherwise name looks good!


# user_name = input("Fill your name: ")

# if len(user_name) < 3:
#     print("Name must be atleast 3 characters")
# elif len(user_name) > 50:
#     print("Name must be maximum of 50 characters")
# else:
#     print("name looks good!")
 
###------------WHILE---------------------##########

# i = 1
# while i <= 5:# Weight_kilogram = input(convert * float(user_wieght_pound))
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

#     print(i)
#     i = i + 1
# print("Done")

#String mulitplication in while loop

# i = 1
# while i <=5:
#     print("*" * i)
#     i = i + 1

#####-----__Guess Game-----

# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == secret_number:
#         print("you won !")
#         break
# else:
#     print("Sorry you loss!")

##---------Car Game-------------##

# help = '''
# start - to start the car
# stop - to stop the car
# quit - to exit
# '''
# start = ("Car Started...Ready to go!")
# stop = ("Car Stopped")

# input_ask = True

# while input_ask:
#     command = input()
#     if command.lower()  == "help":
#         print(help)
#     elif command.lower() == "start":
#         print(start)
#     elif command.lower() == "stop":
#         print(stop)
#     elif command.lower() == "quit":
#         input_ask = False
#         break
#     else:
#         print("I dont understand")



limit = 3
ask_limit = 0
print("Welcome on SAMO Calculater")


while ask_limit < limit:
    method = input("Give Option Between -Add, -subtract, -Divide, Quit: ") 
    if method.lower() == "quit":
        answer = "You Quit"
        break  
    elif method.lower() != "add" and method.lower() != "subtract" and method.lower() != "divide":
        answer = "Invalid Command"
        break
    first_number = input("First Number: ")
    second_number = input("Second Number: ")       
    ask_limit += 1
    if method.lower() == "add":
        answer =  input(int(first_number) + int(second_number))
    elif method.lower() == "subtract":
        answer =  input(int(first_number) - int(second_number))
    elif method.lower() == "divide":
        answer =  input(int(first_number) // int(second_number))  


if ask_limit == 3:
    print("Sorry! Your limit exceeded")
    member = input("Please enter code for unlimited excess: ")    #//code = buy//

    if member.lower()  == "buy":
        member_new = True
        
        while member_new:
            method = input("Give Option Between -Add, -subtract, -Divide, Quit: ") 
            if method.lower() == "quit":
                answer = "You Quit"
                break  
            elif method.lower() != "add" and method.lower() != "subtract" and method.lower() != "divide":
                answer = "Invalid Command"
                break        
            first_number = input("First Number: ")
            second_number = input("Second Number: ")
            if method.lower() == "add":
                answer =  input(int(first_number) + int(second_number))
            elif method.lower() == "subtract":
                answer =  input(int(first_number) - int(second_number))
            elif method.lower() == "divide":
                answer =  input(int(first_number) // int(second_number))  
            else:
                answer = "Invalid Command"
                break 
        

print(answer)
