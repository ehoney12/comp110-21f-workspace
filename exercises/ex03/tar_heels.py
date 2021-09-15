"""An exercise in remainders and boolean logic."""

__author__ = "730240245"


# Begin your solution here...
int1: int = int(input("Enter an int: "))
divis_by_2: int = (int1 % 2)
divis_by_7: int = (int1 % 7)
if divis_by_2 == 0:
    if divis_by_7 == 0:
        print("TAR HEELS")
    else:
        print("TAR")
else: 
    if divis_by_7 == 0: 
        print("HEELS")
    else:
        print("CAROLINA")