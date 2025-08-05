import random 
#game logic is written here 
def generate_number(a=1,b=100):
     number= random.randint(a,b)
     return number
def test_guess(actual,guess):
     if guess<actual:
          return "the number is lesser"
     elif guess>actual:
          return "the number is bigger"
     else :
          return "correct"
     

