

# question 1.a
day_of_the_week = input("What day is it? ")
if day_of_the_week == "Monday":
    print ("Today is Monday")
else:
    print("Today is not Monday")




# question 1.b
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekends = ["Saturday", "Sunday"]

day = input("What day is it? ")

if day in weekdays:
    print("Today is a weekday")
if day in weekends:
    print("Today is a weekend")
else:
    print("Please input a day of the week")
        

# 1.c
hours_worked = int(input("How many hours did you work this week? "))
hourly_rate = int(input("How much do you get paid per hour? "))
pay = (hours_worked * hourly_rate)
overtime = (pay + pay * 0.5)

if hours_worked > 40:
    print(f'Your pay this week will be ${overtime}')
else:
    print(f'Your pay this week will be ${pay}')

# question 2, while loop one
number = 5

while number <= 15:
    print(number)
    number += 1

#question 2, while loop two
#Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
number = 0

while number <= 100:
    print(number)
    print ()
    number += 2


# question 2, while loop three: Alter your loop to count backwards by 5's from 100 to -10.
number = 100
while number >= -10:
    print(number)
    number -= 5


#question 2, while loop four:
#Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:

number = 2
number_squared = (number ** 2)
while number_squared < 1000000:
    print(number_squared)
    number = number_squared
    

#question 2, while loop five, 
#
number = 100
while number >= 0:
    print(number)
    number -= 5

# question 2, for loop i:
#Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

number = int(input("Select a number 1-10:  "))

for i in range (1, 11):
    print (number, 'x', i, '=', i*number)

# question 2, for loop ii:
# write a code that prints the following:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999
i = 0
for i in range (1, 10):
    print(str(i)*i)

#2, break and continue i: 
#Write a program that prompts the user for a positive integer. 
#Next write a loop that prints out the numbers from the number the user entered down to 1.

number = int(input("Pick a number, any number! "))
while number >= 1:
    print(number)
    number -= 1

# 2, break and continue ii:
#Prompt the user to enter a positive number and write a loop that counts from 0 to that number.

number = int(input("Pick a positive number, any positive number! "))
for i in range (-1, number):
    print(i + 1)
   

# 2, break and continue iii:
# odd numbers 1-50 except skipped input number
while True:
    test_number = input("Number to skip is: ")
    if not test_number.isdigit() and if not test_number.isdigit() % 2 == 1:
        print("Sorry, please enter an odd number.")

        

test_number = input("Number to skip is: ")
print(test_number.isdigit())

else:
        for i in range (0, 50):
            if i == test_number
                break
            else 
                print(i + 1)





while True:
    user_num = int(input("Enter a number: "))

    for i in range(1, user_num +1):
        print(f'{i}  |{i**2}   |{i**3}')
    user_yn = input("Would you like to continue? (y/n) ")
    if user_yn.lower() !='y':
        break
         

while True:
    user_grade = int(input("enter a numerical grade 0-100"))

    if user_grade >= 88:
        print('A')
    elif user_grade >= 80:
        print('B')
    elif user_grade >= 67:
        print('C')
    elif user_grade >= 60:
        print ('D')
    else:
        print('F')
    user_yn = input("would you like to continue? (y/n)")
    if user_yn.lower() != 'y':
        break
        