def only_evens(x: list[int]) -> list:
    """Return list containing only even numbers of input list."""
    i: int = 0 
    even: list[int] = list()
    while i < len(x):
        number: int = x[i]
        remainder: int = number % 2
        if remainder == 0: 
            even.append(number)
        i = i + 1 
    return even 