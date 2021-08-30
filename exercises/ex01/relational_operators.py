"""relational operators program."""

__author__ = "730240245"

int1 = input("Left-hand side: ")
int2 = input("Right-hand side: ")
less: bool = (int1 < int2)
greater_or_equal: bool = (int1 >= int2)
print(int1 + " < " + int2 + " is " + str(less))
print(int1 + " >= " + int2 + " is " + str(greater_or_equal))
print(int1 + " == " + int2 + " is " + str(int1 == int2))
print(int1 + " != " + int2 + " is " + str(int1 != int2))