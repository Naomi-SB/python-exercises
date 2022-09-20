def is_two(number):
    
    if number == 2 or number == ['2']:
        return True
    else:
        return False

def is_vowel(letter):
    if letter == ['a'] or letter == ['e'] or letter == ['i'] or letter == ['o'] or letter == ['u']:
        return True
    else: 
        return False

def is_consonant(letter):
    if letter == ['a'] or letter == ['e'] or letter == ['i'] or letter == ['o'] or letter == ['u']:
        return False
    else: 
        return True

def remove_vowels(word):
  vowels = ('a', 'e', 'i', 'o', 'u')
  for x in word:
    if x in vowels:
      word = word.replace(x, '')
  return word

def capitalize_consonant(word):
  if word[0] in ['a','e','i','o','u','A','E','I','O','U']:
    print(word)
  else:
    print(word.capitalize())


def tip_amount():

  initial_bill_amount = int(input("How much was your bill? "))
  tip_percentage = float(input("What percentage would you like to tip? (enter a decimal number between 0 and 1)"))
  tip_money = (initial_bill_amount * tip_percentage)
  return 'Your total bill is',  initial_bill_amount + tip_money

def apply_discount():
  og_price = int(input("What is the original price? "))
  dc_percentage = float(input("What is the discount as a percentage between 0 and 1? "))
  amount_discounted = og_price * dc_percentage
  return "The new cost is: ", (og_price - amount_discounted)

def handle_commas(number):
  no_commas = number.split(',')
  all_together_now = (''.join(no_commas))
  return int(all_together_now)

while True:
    get_letter_grade = int(input("enter a numerical grade 0-100"))

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

