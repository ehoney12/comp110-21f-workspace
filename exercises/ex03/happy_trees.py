"""Drawing forests in a loop."""

__author__ = "730240245"

# The string constant for the pine tree emoji
i: int = 0 
TREE: str = '\U0001F332'
depth: int = int(input("Depth: "))
while i < depth: 
    j: int = i + 1 
    how_many: str = str(TREE * j)
    print(how_many)
    i += 1 