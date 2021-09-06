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
fortune_one: str = "You will do great one you next comp quiz."
fortune_two: str = "You will meet some amazing new people in the next few weeks of you life."
fortune_three: str = "You will win a student lottery ticket for the football game next week."
fortune_four: str = "Someone you love will give you a big surprise."
print("Your fortune cookie says... ")
choose: int = randint(1, 4)
if choose == 1:
    print(fortune_one)
    print("Now, go spread positive vibes!")
else: 
    if choose == 2: 
        print(fortune_two)
        print("Now, go spread positive vibes!")
    else:
        if choose == 3: 
            print(fortune_three)
            print("Now, go spread positive vibes!")
        else:
            print(fortune_four)
            print("Now, go spread positive vibes!")