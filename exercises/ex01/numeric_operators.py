"""Elizabeth's numeric operators program."""

__author__ = "730240245"

int1: int = int(input("Left-hand side: "))
int2: int = int(input("Right-hand side: "))
times: int = (int1 ** int2)
division: float = (int1 / int2)
integer_division: int = (int1 // int2)
remainder: int = (int1 % int2)
print(str(int1) + " **" + str(int2) + " is " + str(times))
print(str(int1) + " / " + str(int2) + " is " + str(division))
print(str(int1) + " // " + str(int2) + " is " + str(integer_division))
print(str(int1) + " % " + str(int2) + " is " + str(remainder))