"""Counting letters in a string."""

__author__ = "730240245"


# Begin your solution here...
i: int = 0 
search: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
while i < len(word):
    how_many: int = word.count(search)
    print("Count: " + str(how_many))
    i = len(word)