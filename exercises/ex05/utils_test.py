"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730240245"


def test_only_evens_empty() -> None: 
    """Only_evens function edge case testing with empty list."""
    x: list[int] = []
    assert only_evens(x) == []


def test_only_evens_all() -> None:
    """Only_evens function use case testing all even numbers."""
    x: list[int] = [2, 4, 6, 8, 10]
    assert only_evens(x) == [2, 4, 6, 8, 10]


def test_only_evens_none() -> None:
    """Only_evens function use case testing with all odd numbers."""
    x: list[int] = [1, 3, 5, 7, 9]
    assert only_evens(x) == []


def test_sub_empty() -> None: 
    """Sub function edge case testing with empty list."""
    p: list[int] = []
    a: int = 0 
    b: int = 3
    assert sub(p, a, b) == []


def test_sub_interior_testing() -> None:
    """Sub function use case testing."""
    p: list[int] = [1, 7, 9, 10, 12, 14]
    a: int = 2
    b: int = 4 
    assert sub(p, a, b) == [9, 10]


def test_sub_a_less_than_zero() -> None:
    """Sub function use case testing."""
    p: list[int] = [0, 3, 6, 12, 15, 19, 22]
    a: int = -2
    b: int = 6
    assert sub(p, a, b) == [0, 3, 6, 12, 15, 19]


def test_concat_empty_one_list() -> None: 
    """Concat function edge case testing with empty list."""
    one: list[int] = []
    two: list[int] = [1, 2]
    assert concat(one, two) == [1, 2]


def test_concat_len_two() -> None:
    """Concat function use case testing longer length of list two."""
    one: list[int] = [3, 5, 7]
    two: list[int] = [4, 5, 7, 9]
    assert concat(one, two) == [3, 5, 7, 4, 5, 7, 9]


def test_concat_len_one() -> None:
    """Concant function use case testing longer length of list one."""
    one: list[int] = [1, 2, 3, 4]
    two: list[int] = [5]
    assert concat(one, two) == [1, 2, 3, 4, 5]
