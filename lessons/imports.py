"""Examples of importing in python."""


from lessons import helpers 
from lessons import helpers as hp 
#this will alias the module imported from a package with a local name 

# Import names defined globally in a module
from lessons.helpers import powerful, THE_ANSWER


def main() -> None: 
    """Entrypoint of program."""
    print(helpers.powerful(2, 4))
    print(f"The answer: {hp.THE_ANSWER}") 
    print(powerful(2,4))
    print(THE_ANSWER)

    
if __name__ == "__main__":
    main()