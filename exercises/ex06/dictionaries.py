"""Practice with dictionaries."""

__author__ = "730240245"

# Define your functions below


def invert(input: dict[str, str]) -> dict[str, str]:
    """Returns a dictionary with inverted keys and values."""
    give: dict[str, str] = {}
    for key in input:
        a: str = input[key]
        if a in give: 
            raise KeyError("cannot have two of the same keys: make sure each of your values are unique.")
        give[a] = key
    return give


def favorite_color(x: dict[str, str]) -> str:
    """Returns the most frequent color that appears in the dictionary."""
    most: dict[str, int] = {}
    for key in x: 
        b: str = x[key]
        if b in most: 
            most[b] += 1
        else: 
            most[b] = 1 
    i: int = 0 
    p: str = ""
    for key in most: 
        if most[key] > i: 
            i = most[key]
            p = key 
    return p 


def count(c: list[str]) -> dict[str, int]: 
    """Returns a dictionary with values as the number of times the key appears in a list."""
    a: dict[str, int] = {} 
    i: int = 0 
    while i < len(c):
        r: str = c[i]
        if r in a: 
            a[r] += 1 
        else: 
            a[r] = 1 
        i += 1
    return a 