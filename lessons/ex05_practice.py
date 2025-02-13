def only_evens(x: list[int]) -> list:
    """Return list containing only even numbers of input list."""
    i: int = 0 
    even: list = list()
    while i < len(x):
        number: int = x[i]
        remainder: int = number % 2
        if remainder == 0: 
            even = even + number 
        i = i + 1 
    return even 

    
def sub(p: list[int], a: int, b: int) -> list:
    """Return list of subset of given list."""
    subset: list[int] = list()
    if len(p) == 0 or a > len(p) or b <= 0:
        return subset
    if a < 0: 
        a = 0
    if b > len(p):
        b = len(p)
    i: int = 0 
    start: int = p[a]
    end: int = p[b - 1]
    while i < len(p):
        sequence: int = p[i]
        if sequence >= start and sequence <= end:
            subset.append(sequence)
        i = i + 1 
    return subset


def concat(one: list[int], two: list[int]) -> list:
    """Return list with all elements of given lists."""
    new: list[int] = list()
    i: int = 0 
    j: int = 0 
    while i < len(two):
        while j < len(one):
            add: int = one[j]
            new.append(add)
            j = j + 1
        add2: int = two[i]
        new.append(add2)
        i = i + 1 
    return new