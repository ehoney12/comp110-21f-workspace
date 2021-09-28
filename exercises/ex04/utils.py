"""List utility functions."""

__author__ = "730240245"


# TODO: Implement your functions here.
def all(y: list[int], x: int) -> bool: 
    """Return True if list numbers match x, Return False otherwise or an Empty List."""
    i: int  = 0 
    while i < len(y):
        number: int = y[i]
        if x != number or y == list(): 
            return False 
        i = i + 1 
    return True 


def is_equal(a: list[int], b: list[int]) -> bool: 
    """Return True if lists are equal, return false otherwise."""
    i: int = 0 
    while i < len(a): 
        list_a: int = a[i]
        list_b: int = b[i]
        if len(a) != len(b) or list_a != list_b:
            return False 
        i = i + 1 
    return True 


def max(input: list[int]) -> int: 
    """Return the largest int value in the list."""
    if input == list():    
        raise ValueError("max() arg is an empty List")
    i: int = 0 
    biggest: int = -99999 
    while i < len(input):
        if input[i] > biggest: 
           biggest = input[i] 
        i = i + 1 
    return biggest
