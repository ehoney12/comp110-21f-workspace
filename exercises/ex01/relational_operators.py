"""relational operators program."""

__author__ = "730240245"

int1: int = int(input("Left-hand side: "))
int2: int = int(input("Right-hand side: "))
less: bool = (int1 < int2)
greater_or_equal: bool = (int1 >= int2)
equal_to: bool = (int1 == int2)
not_equal_to: bool = (int1 != int2)
print(str(int1) + " < " + str(int2) + " is " + str(less))
print(str(int1) + " >= " + str(int2) + " is " + str(greater_or_equal))
print(str(int1) + " == " + str(int2) + " is " + str(equal_to))
print(str(int1) + " != " + str(int2) + " is " + str(not_equal_to))