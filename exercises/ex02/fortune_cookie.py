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


# Begin your solution here...
fortune_one: int = 1
fortune_two: int = 2 
fortune_three: int = 3 
fortune_four: int = 4
str = input("Your fortune cookie says...")
choose: int = int(randint(1, 4))
if choose == fortune_one:
    print("You will do great on your next comp quiz.")
    print("Now, go spread positive vibes!")
else: 
    if choose == fortune_two: 
        print("You will meet some amazing new people in the next few weeks of your life.")
        print("Now, go spread positive vibes!")
    else: 
        if choose == fortune_three: 
            print("You will win a student lottery ticket for the football game next week.")
            print("Now, go spread positive vibes!")
        else:
            if choose == fortune_four: 
                print("Someone you love will give you a big surprise.")
                print("Now, go spread positive vibes!")