"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730240245"


def invert_same_key() -> None: 
    """Invert function edge case testing with more than one of same key."""
    input: dict[str, str] = {'bone': 'dog', 'toy': 'dog'}
    assert invert(input) == KeyError("cannot have two of the same keys: make sure each of your values are unique")


def invert_letters() -> None:
    """Invert function use case testing with letters."""
    input: dict[str, str] = {'c': 'r', 't': 'q', 'b': 'w'}
    assert invert(input) == {'r': 'c', 'q': 't', 'w': 'b'}


def test_invert_words() -> None: 
    """Invert function use case testing with words."""
    input: dict[str, str] = {'hi': 'hey', 'who': 'you'}
    assert invert(input) == {'hey': 'hi', 'you': 'who'} 


def test_favorite_color_tie_between_two() -> None:
    """Favorite_color function use case testing with a tie between two colors."""
    x: dict[str, str] = {'Ally': 'blue', 'Karen': 'purple', 'Jeff': 'blue', 'Carol': 'purple'}
    assert favorite_color(x) == 'blue'


def test_favorite_color_all_different_colors() -> None:
    """Favorite_color function use case testing with all different colors."""
    x: dict[str, str] = {'Steven': 'green', 'Mark': 'grey', 'Tony': 'orange'}
    assert favorite_color(x) == 'green'


def test_favorite_color_one_color() -> None:
    """Favorite_color function edge case testing with one color."""
    x: dict[str, str] = {'Mary': 'pink', 'Sara': 'pink', 'Anthony': 'pink'}
    assert favorite_color(x) == 'pink'


def test_count_empty_list() -> None:
    """Count functon edge case testing with empty list."""
    c: list[str] = []
    assert count(c) == {}


def test_count_different_str() -> None:
    """Count function use case testing with different words."""
    c: list[str] = ['fall', 'pumpkins', 'Halloween', 'candy']
    assert count(c) == {'fall': 1, 'pumpkins': 1, 'Halloween': 1, 'candy': 1}


def test_count_duplicates_and_more() -> None: 
    """Count function use case testing with words that appear multiple times in list."""
    c: list[str] = ['coffee', 'sugar', 'spice', 'sugar', 'sugar', 'coffee', 'cream']
    assert count(c) == {'cofee': 2, 'sugar': 3, 'spice': 1}