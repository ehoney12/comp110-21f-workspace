"""Choose Your Own Adventure Project."""

__author__ = 730240245

player: str = ""
points: int = 0
sus_1: str = "Freddy"
sus_2: str = "Susan"
sus_3: str = "Mike"
sus_4: str = "Hally"
yes: str = "yes"
no: str = "no"
i: int = 1 


def main() -> None: 
    """The programs entrypoint."""
    greet()
    print("You will begin the game with 0 detective points")
    print("As you continue to find clues throughout the game, I will update you on your total detective points")
    print("You have 4 options to choose from")
    print("Each option will give you instructions on what to do and how you can accumulate points.")
    input("Follow along and solve her mystery!! when you're ready to continue, press any key ")
    print("")
    global i 
    while i > 0: 
        A: str = "profile"
        B: str = "scene"
        C: str = "guess"
        print("To look at Sally's profile, type profile")
        print("To look at the murder scene, type scene")
        print("To take a guess at the murderer, type guess")
        print("To end the game, type end")
        print("")
        begin: str = input("Which option would you like to choose? ")
        print("")
        if begin == A: 
            a: int = sally(0)
            print("Here's the total amount of points you've gained from looking at Sally's profile")
            print(a)
            global points
            points = points + a 
            print(f"total detective points = {points}")
            print("")
        else: 
            if begin == B: 
                scene() 
                print(f"Detective points = {points}")
                print("")
            else: 
                if begin == C: 
                    guess()
                    print(f"Detective points = {points}")
                    print("")
                else: 
                    goodbye()
                    return None
        i = i 


def goodbye() -> None: 
    """Goodbye Message."""
    print("I hope you enjoyed the game!")
    print("We hope to see you next time.")
    print("Before you go, here are the total points you have accumalated throughout the game:")
    print(f"Detective points = {points}")
    

def guess() -> None: 
    """Guessing the Murderer."""
    print(f"So {player} think you're ready to guess the murder?")
    print("It will cost you 50 points for each attempt to guess the murderer")
    print("If you guess correcly, you win 1000 points and You win the game!")
    print("")
    print("Here's how many points you've got so far")
    global points
    print(f"Detective points = {points}")
    ready: str = input("Are you sure you want to guess? type yes or no ")
    if ready == yes:
        if points > 50: 
            print("Okay, I like the confidence.")
            points = points - 50 
            print(f"Detective points = {points}")
            f: int = 1 
            while f > 0: 
                murderer: str = input("Who do you think is the murderer? ")
                if murderer == sus_1:
                    print("CONGRATS! YOU HAVE SOLVED THE MYSTERY") 
                    print("Looks like you've got great detective skills")
                    points = points + 1000
                    return None
                else: 
                    print("")
                    print("That's not quite right.") 
                    print(f"remaining detective points = {points}")
                    again: str = input("Would you like to try again? type yes or no ")
                    if again == no: 
                        return None
                    else: 
                        if points < 50: 
                            print("Sorry, looks like you don't have enough points to guess.")
                            print("Play the other sections to accumlate points and try again!")
                            print("")
                            input("Press any key to continue ")
                            return None
                print("")
                points = points - 50 
                print(f"Detective points = {points}")
                f = f 
        else: 
            print("Sorry, looks like you don't have enough points to guess.")
            print("Play the other sections to accumulate points and try again!")
            print("")
            return None


def scene() -> None: 
    """Looking at the Murder Scene."""
    print(f"Hey {player}, You've arrived at the murder scene")
    print("As you inspect each object in the murder scene, I will give you a random amount of points")
    w: str = "weapon"
    b: str = "body"
    d: str = "door"
    l: str = "living room"
    p: int = 1
    while p > 0:
        from random import randint
        amount: int = randint(1, 20)
        print("")
        print("Objects: weapon, body, door, living room, or quit")
        search: str = input("Choose which obects you'd like to inspect ")
        print("")
        if search == w: 
            print(f"The murder weapon was a knife and after searching for fingerprints, you found matches with {sus_1} and {sus_3}")
        else: 
            if search == b: 
                print(f"After inspecting Sally's body, you notice a hair strand that matches {sus_2}")
            else: 
                if search == d:
                    print("After inspecting the door, it is obvious the door was broken into and someone had to break in by force")
                else: 
                    if search == l: 
                        print("From searching the living room, play a voicemail that's been left on the landline.")
                        print(f"listening to it, you match the voice with {sus_1} and conclude the voicemail was a quite aggressive message left for Sally")
                    else: 
                        print("You are leaving the murder scene")
                        input("Press any key to continue")
                        print("")
                        return None 
        print(f"Nice! You got {amount} points")
        global points
        points = points + amount
        print(f"Detective points = {points}")
        print("")
        p = p 


def sally(x: int) -> int: 
    """Sally's profile."""
    print(f"Hi {player}. In this section of the mystery, You will be able to look at some key information about the murder.")
    print("In this section of the game, I will not add the points collected from each option you choose until after you choose to quit this section")
    print("Once you are done looking at the profile, I will inform you of the total points collected in this section and your total detective points")
    print("")
    sus: str = "suspects"
    state: str = "statements" 
    o: int = 1 
    while o > 0:
        print("Here are your options for this section:")
        print("To look at the list of suspects, type suspects: 10 points")
        print("To look at the interogation statements of each suspect, type statements: 5 points each")
        print("To exit Sally's profile, type quit") 
        print("")
        which: str = input("To collect further information, which option would you like to select? ")
        if which == sus:
            print("Here are the list of suspects")
            print("Freddy: One of Sally's assistant pastery cheif's at her bakery")
            print("Susan: Sally's Mom")
            print("Mike: Sally's Brother")
            print("Hally: Sally's neighbor who made the call")
            print("")
            x = x + 10 
        else: 
            if which == state: 
                y: int = 1 
                while y > 0: 
                    print("optons: Freddy, Susan, Mike, Hally or end")
                    print("")
                    who: str = input("Who's statement would you like to read? ")
                    if who == sus_1:
                        print("Everybody loved Sally. And even more so, everybody loves her baked goods. I dont know who do such a thing.")
                        x = x + 5 
                    else: 
                        if who == sus_2: 
                            print("So distraught from the loss of her daughter, She was unable to come in for interogation.")
                            x = x + 5
                        else: 
                            if who == sus_3: 
                                print("I know I shouldn't say things like this but she wasnt always the person everybody thought she was. I knew the real side of her. She had this coming.")
                                x = x + 5 
                            else: 
                                if who == sus_4: 
                                    print("I don't know who would do this. I was never really close to Sally. Even though everybody in town knew her from her bakery, She never had a lot of visitors and spent most of her days alone. Although, I do remember her brother's car outside the other day when she wasn't home but I didn't think too much of it because sometimes he'll come over to feed her dog.")
                                    x = x + 5
                                else: 
                                    y = 0 
                    print("")
                    y = y 
            else: 
                print("You've closed Sally's profile")
                input("Press any key to continue back to the homepage ")
                print(" ")
                o = 0 
                return x
        input("Press any key to continue")
        print("")
        o = o 
    return x 
    

def greet() -> None: 
    """Introduction."""
    print("Welcome to Sally's Murder Mystery")
    print("before we begin, let's introduce ourselves. My name is Elizabeth")
    global player
    player = input("What is your name ")
    print(f"Hi {player}, it's very nice to meet you.")
    print("")
    print("Here's how to play")
    print("You must use your detective skills to determine who killed Sally")
    print("Throughout the game, you will gain detective points")
    print("These detective points will be used when you want to guess who committed the murder")
    print("Guess the murderer correctly and you win the game")
    input("Press any key to continue ")
    print("")


if __name__ == "__main__":
    main()