############################Exercises########################## ###########
############################################################################
################# IDENTIFY THE DATA TYPES OF THE FOLLOWING:#################
############################################################################
# 99.9: FLOAT

# "False": string

# False: boolean

# '0': string

# 0: int

# True: boolean

# 'True': string

# [{}]: list of a dictionary

# {'a': []}: dictionary containing a string and a list

############################################################################
################# IWHAT DATA TYPE WOULD BEST REPRESENT: ###################
############################################################################

#A term or phrase typed into a search box? A STRING

# If a user is logged in? BOOLEAN

# A discount amount to apply to a user's shopping cart? FLOAT

# Whether or not a coupon code is valid? BOOLEAN

# An email address typed into a registration form? LIST

# The price of a product? INT OR FLOAT

# A Matrix? TUPLE

# The email addresses collected from a registration form? STRING

# Information about applicants to Codeup's data science program? DICTIONARY

############################################################################
##################### PREDICT RESULTS THEN EVALUATE ########################
############################################################################

'1'+2
#prediction: ERROR
# execution: ERROR

6 % 4
#prediction: 2
# execution: 2

type(6 % 4)
#prediction: int
# execution: int

type(type(6 % 4))
#prediction: type
# execution: type

'3 + 4 is ' + 3 + 4
#prediction: ERROR
# execution: ERROR

0 < 0
#prediction: FALSE
# execution: FALSE

'False' == False
#prediction: FALSE
# execution: FALSE

True == 'True'
#prediction: TRUE
# execution: FALSE****

5 >= -5
#prediction: TRUE
# execution: TRUE

True or "42"
#prediction: TRUE
# execution: TRUE

6 % 5
#prediction: 1
# execution:1

5 < 4 and 1 == 1
#prediction: FALSE
# execution: FALSE

'codeup' == 'codeup' and 'codeup' == 'Codeup'
#prediction: FALSE
# execution: FALSE

4 >= 0 and 1 !== '1'
#prediction: FALSE
# execution: SYNTAX ERROR********

6 % 3 == 0
#prediction: TRUE
# execution: TRUE

5 % 2 != 0
#prediction: FALSE
# execution: TRUE*********

[1] + 2
#prediction: 3
# execution: ERROR********

[1] + [2]
#prediction: 3
# execution: [1, 2]********

[1] * 2
#prediction: ERROR
# execution: [1, 1]*******

[1] * [2]
#prediction: [2]
# execution: ERROR *******

[] + [] == []
#prediction: []
# execution: TRUE*****

{} + {}
#prediction: ERROR
# execution: ERROR


############################################################################
######################## WRITE CODE FOR SCENARIOS ##########################
############################################################################

#1. Little Mermaid (3 days), Brother Bear (5 days), Hercules (1 day). $3 per day, per movie.

#total_price_per_day = sum('period' * price_per_movie_day)

price_per_movie_day = [3, 3, 3]
movies_rented = {
    'titles' : ['Little Mermaid', 'Brother Bear', 'Hercules'],
    'period' : [3, 5, 1]
            }
cost_per_title = []
for value1, value2 in zip(price_per_movie_day, movies_rented['period']):
        cost_per_title.append(value1 * value2)
print(cost_per_title)
total_cost = sum(cost_per_title)
print(total_cost)

#2. How much will you receive in payment for this week? 
compensation = {
    'Facebook' : 350,
    'Amazon': 380,
    'Google': 400
}

hours_worked = {
    'Facebook' : 10,
    'Amazon' : 4,
    'Google': 6
}
Facebook_total = (compensation['Facebook'] * hours_worked['Facebook'])
print(Facebook_total)
Amazon_total = (compensation['Amazon'] * hours_worked['Amazon'])
Google_total = (compensation['Google'] * hours_worked['Google'])
total_paid = Facebook_total + Amazon_total + Google_total
print(total_paid)

#3. A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.
student_has_no_conflict = True
class_has_opening = True
can_enroll = student_has_no_conflict and class_has_opening
print(can_enroll)

#4. A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.
#products_purchased
#premium_member
#offer_valid (meaning NOT expired)
#offer_applied

minimum_requirement = 2
products_purchased = 3
premium_member = True
offer_valid = True

products_purchased > minimum_requirement

if (products_purchased > minimum_requirement) and (premium_member == True) and (offer_valid == True):
    print ('Your offer is applied!')

############################################################################
############################# BOOLEAN PASSWORD #############################
############################################################################
the password must be at least 5 characters
the username must be no more than 20 characters
the password must not be the same as the username
bonus neither the username or password can start or end with whitespace

password = 'j'
username = 'o'



password_minimum_length == len(password) >= 5

username_maximum_length == len(username) <=20

username != password


