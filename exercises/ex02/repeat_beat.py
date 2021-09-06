"""Repeating a beat in a loop."""

__author__ = "730240245"


# Begin your solution here... 
counter: int = 0 
repeat: str = input("What beat do you want to repeat? ")
maximum: int = int(input("How many times do you want to repeat it? "))
while maximum > counter:
    times: str = (str(" " + repeat) * (maximum - 1))
    print(repeat + times)
    counter = maximum
if maximum <= 0: 
    print("No beat...")


    