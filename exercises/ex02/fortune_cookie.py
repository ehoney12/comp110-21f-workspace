"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730240245"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


one: int = 1
two: int = 2 
three: int = 3 
four: int = 4
str = input("Your fortune cookie says...")
from random import randint 
random: int = int(randint(1, 4))
if random == one:
    print("You will do great on your next comp quiz.")
    print("Now, go spread positive vibes!")
else: 
    if random == two: 
        print("You will meet some amazing new people in the next few weeks of your life.")
        print("Now, go spread positive vibes!")
    else: 
        if random == three: 
            print("You will win a student lottery ticket for the football game next week.")
            print("Now, go spread positive vibes!")
        else: 
            print("Someone you love will give you a big surprise.")
            print("Now, go spread positive vibes!")
    

