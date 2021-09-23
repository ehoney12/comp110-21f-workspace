"""testing it out."""


points: int = 0

def scene() -> None: 
    """Looking at the Murder Scene."""
    print("You are arrived at the murder scene")
    print("As you inspect each object in the murder scene, I will give you a random amount of points")
    w: str = "weapon"
    b: str = "body"
    d: str = "door"
    l: str = "living room"
    p: int = 1 
    while p > 0: 
        from random import randint
        amount: int = randint(1,20)
        print("Objects: murder, weapon, body, door, living room, bedroom, kitchen, or quit")
        search: str = input("Choose which obects you'd like to inspect")
        if search == w: 
            print()
            print(f"Nice, you got {amount} points")
            print("Here's to total amount of points you've gained")
            global points
            points = points + amount 
            print(f"total points = {points}")
        else: 
            if search == b: 
                print()
                print(f"amazing, you got {amount}")
                print("Here's to total amount of points you've gained")
                global points
                points = points + amount 
                print(f"total points = {points}")
            else: 
                if search == d:
                    print()
                    print(f"amazing, you got {amount}")
                    print("Here's to total amount of points you've gained")
                    global points
                    points = points + amount 
                    print(f"total points = {points}")
                else: 
                    if search == l: 
                        print()
                        print(f"amazing, you got {amount}")
                        print("Here's to total amount of points you've gained")
                        global points
                        points = points + amount 
                        print(f"total points = {points}")
                    else: 
                        p = 0
        p = p

scene()

else: 
                if begin == C: 
                    guess() 
                    print(f"detective points = {points}")
                else: 
                    goodbye()
                    i = 0 