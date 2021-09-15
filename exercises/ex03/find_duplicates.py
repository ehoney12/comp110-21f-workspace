"""Finding duplicate letters in a word."""

__author__ = "730240245"


search: str = input("Enter a word: ")
duplicate: bool = False 
i: int = 0 
while i < len(search): 
    letter: str = str(search[i])
    j: int = i + 1
    while j < len(search):
        other: str = str(search[j])
        if letter == other: 
            print("Found duplicate: " + str(not duplicate))
            i = len(search)
        j += 1 
    if i == (len(search)-1):
        print("Found duplicate: " + str(duplicate))
    i += 1 