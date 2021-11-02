"""Utility functions."""

__author__ = "730240245"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read CVS of data into a list of rows."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(one: list[dict[str, str]], two: str) -> list[str]:
    """List of values in a single column whose name is the second parameter."""
    result: list[str] = []
    i: int = 0 
    while i < len(one):
        a: dict[str, str] = one[i]
        for key in a: 
            b: str = a[key]
            if key == two: 
                result.append(b)
        i += 1
    return result 


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform table into dictionary."""
    result: dict[str, list[str]] = {}
    i: int = 0 
    while i < len(table):
        first_row: dict[str, str] = table[i]
        for column in first_row:
            result[column] = column_values(table, column)
        i += 1
    return result 


def head(one: dict[str, list[str]], N: int) -> dict[str, list[str]]: 
    """Produce new column-based table with only the first N rows of data."""
    result: dict[str, list[str]] = {}
    if N >= len(one): 
        return one 
    for key in one: 
        a: list[str] = []
        i: int = 0 
        while i < N: 
            b: str = one[key][i]
            a.append(b)
            i += 1 
        result[key] = a 
    return result


def select(one: dict[str, list[str]], two: list[str]) -> dict[str, list[str]]:
    """Produce new column-based table with specific subset of original column."""
    result: dict[str, list[str]] = {}
    i: int = 0 
    while i < len(two): 
        a: str = two[i]
        if a in one: 
            b: list[str] = one[a] 
            result[a] = b
        i += 1 
    return result


def concat(one: dict[str, list[str]], two: dict[str, list[str]]) -> dict[str, list[str]]: 
    """Produce new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {} 
    for key in one: 
        add: list[str] = one[key]
        result[key] = add 
    for key in two: 
        if key in result: 
            a: list[str] = result[key]
            add2: list[str] = two[key]
            i: int = 0 
            while i < len(add2): 
                b: str = add2[i]
                a.append(b)
                i += 1
            result[key] = a 
        else: 
            add3: list[str] = two[key]
            result[key] = add3
    return result


def count(a: list[str]) -> dict[str, int]:
    """Return dictionary with key's as str and value's as the number of times the key appears."""
    result: dict[str, int] = {}
    i: int = 0 
    while i < len(a):
        b: str = a[i]
        if b in result:
            result[b] += 1
        else:
            result[b] = 1 
        i += 1 
    return result