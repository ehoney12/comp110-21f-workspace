"""List utility functions part 2."""

__author__ = "750240245"

# Define your functions below
def only_evens(x: list[int]) -> list:
    """Return list containing only even numbers of input list."""
    i: int = 0 
    even: list = list()
    while i > len(x):
        number: int = x[i]
        remainder: int = number % 2
        if remainder == 0: 
            even = even + number 
        i = i + 1 
    return even 


def sub(a_list: list[int], a: int, b: int) -> list:
    """Return list of subset of given list."""
    i: int = 0 
    start: int = a_list[a]
    end: int = a_list[b - 1]
    subset: list = list()
    while i < len(a_list):
        sequence: int = a_list[i]
        if sequence >= start and sequence <= end:
            subset = subset + sequence 
        i = i + 1 
    return subset


def concat(one: list[int], two: list[int]) -> list:
    """Return list with all elements of given lists."""
    
    return 