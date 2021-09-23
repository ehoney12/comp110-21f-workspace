"""CQ3. A main Fucntion."""


def main() -> None: 
    """The program's entrypoint."""
    print("main()")
    y: float = double(2.0)
    print(halve(y))


def halve(x: float) -> float: 
    """Hlave a value."""
    print(f"halve({x})")
    return x / 2.0 


def double(x: float) -> float: 
    """Double a value."""
    print(f"double({x})")
    return x * 2.0 


if __name__ == "__main__": 
    print("__name__is '__main'")
    main()