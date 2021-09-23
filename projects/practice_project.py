"""Choose Your Own Adventure."""

__author__ = 730240245

#Global variables 
player: str = ""
points: int = 0
sus_1: str = "Freddy"
sus_2: str = "Susan"
sus_3: str = "Mike"
sus_4: str = "Hally"
yes: str = "yes"
no: str = "no"
i: int = 0 

def main() -> None: 
    """The programs entrypoint."""
    greet()
    print("Let's start with the basics")
    print("You will begin the game with 0 points")
    print("In this game, you can choose to look at Sally's profile, look at the murder scene or guess the murderer or end the game"
    while i > 0: 
        print("To look at Sally's profile, type profile")
        print("To look at the murder scene, type scene")
        print("To take a guess at the murder, type guess")
        print("To end the game, type end")
        A: str = "profile"
        B: str = "scene"
        C: str = "guess"
        D: str = "end"
        begin: str = input("Which option would you like to choose? ")
        if begin == A: 
            a: int = Sally(0)
            print("Here's the total amount of points you've gained from looking at Sally's profile")
            print(a)
            global points 
            points = points + a 
            print("Here's the total amount of detective points you now have")
            print(points)
        else: 
            if begin == B:
                scene()
                print(f"detective points = {points}")
            else: 
                if begin == C: 
                    guess()
                    print(f"detective points = {points}")
                else: 
                    goodbye()
                    i = 0 
        i = i 
        

def Sally(x: int) -> int: 
    """Sally's Profile."""
    print(f"Hi {player}. In this section of the mystery, you will be able to look at some information collected about Sally's murder.")
    print("You can look at the suspect list or the interogation statements from each suspect")
    print("For each option, you will be given points but these points will not be added to your total points until you choose to end this section of the game")
    print("I will keep tract of your points and update you on the total points you've gained from this section only.")
    print(f"So far, your profile points = {x}")
    print("Here's what we already know:")
    print("She was well known for her bakery in your small town of Huffleton.")
    print("Last night, your police station got a call from her neighbor saying they heard load noises and screaming coming from her room. When you and your team arrived to the scene, Sally was found dead in her room.")
    print("To look at the description of the list of supects type suspects: 10 points")
    print("To view each suspects interogation statements type statements: 5 points each")
    print("To exit Sally's profile, type quit")
    sus: str = "suspects"
    state: str = "statements" 
    while i > 0: 
        which: str = input("To collect further information, which option would you like to select? ")
        if which == sus: 
            if which == sus:
            print("Freddy: One of Sally's assistant pastery cheif's at her bakery")
            print("Susan: Sally's Mom")
            print("Mike: Sally's Brother")
            print("Hally: Sally's neighbor who made the call")
            x = x + 10 
            print(f"profile points = {x}")
        else: 
            if which == state: 
                print("optons: Freddy, Susan, Mike, Hally or quit")
                repeat: int = 1 
                while repeat > 0:
                    who: str = input("Who's statement would you like to read? ")
                    if who == sus_1: 
                        print("Everybody loved Sally. And even more so, everybody loves her baked goods. I dont know who do such a thing.")
                        x = x + 5
                        print(f"profile points = {x}")
                    else: 
                        if who == sus_2: 
                            print("So distraught from the loss of her daughter, She was unable to come in for interogation. Dead End.")
                            x = x + 5
                            print(f"profile points = {x}")
                        else: 
                            if who == sus_3:
                                print("I know I shouldn't say things like this but she wasnt always the person everybody thought she was. I knew the real side of her. She had this coming.")
                                x = x + 5 
                                print(f"profile points = {x}")
                            else: 
                                if who == sus_4:
                                    print("I don't know who would do this. I was never really close to Sally. Even though everybody in town knew her from her bakery, She never had a lot of visitors and spent most of her days alone. Although, I do remember her brother's car outside the other day when she wasn't home but I didn't think too much of it because sometimes he'll come over to feed her dog.")
                                    x = x + 5 
                                    print(f"profile points = {x}")
                                else: 
                                    repeat = 0
                        repeat = repeat
        i = i 
    return x
        
def scene() -> None: 
    """Looking at the Murder Scene."""
    from random import randint
    print("You are arrived at the murder scene")
    print("As you inspect each object in the murder scene, I will give you a random amount of points")
    1: str = "weapon"
    2: str = "body"
    3: str = "door"
    4: str = "floor"
    5: "living room"
    6: str = "kitchen"
    while i > 0: 
        amount: int = randint(1,20)
        print("Objects: murder, weapon, body, door, living room, bedroom, kitchen, or quit)
        search: str = input("Choose which obects you'd like to inspect")
        if search == 1: 
            print()
            print(f"Nice, you got {amount} points")
            print("Here's to total amount of points you've gained")
            global points
            points = points + amount 
            print(f"total points = {points}")
        else: 
            if search == 2: 
                print()
                print(f"amazing, you got {amount}"")
                print("Here's to total amount of points you've gained")
                global points
                points = points + amount 
                print(f"total points = {points}")
            else: 
                if search == 3:
                    print()
                    print(f"amazing, you got {amount}"")
                    print("Here's to total amount of points you've gained")
                    global points
                    points = points + amount 
                    print(f"total points = {points}")
                else: 
                    if search == 4: 
                        print()
                        print(f"amazing, you got {amount}"")
                        print("Here's to total amount of points you've gained")
                        global points
                        points = points + amount 
                        print(f"total points = {points}")
                    else: 
                        if search == 5: 
                            print()
                             print(f"amazing, you got {amount}"")
                            print("Here's to total amount of points you've gained")
                            global points
                            points = points + amount 
                            print(f"total points = {points}")
                        else: 
                            if search == 6: 
                                print()
                                print(f"amazing, you got {amount}"")
                                print("Here's to total amount of points you've gained")
                                global points
                                points = points + amount 
                                print(f"total points = {points}")
                            else: 
                                i = 0
        i = i
        





def guess() -> None: 
    """Guessing the Murderer"""
    print("So you think you're ready to guess the murder?")
    print("It will cost you 50 points make an attempt to guess the murderer")
    print("Just a reminder, you are allowed to guess as many times are you'd like but if you guess incorrectly you will lose 100 points")
    print("If you guess correcly, you win 1000 points and You win the game!")
    print("Here's how many points you've got so far")
    b: int = points
    ready: str = input("Are you sure you want to guess? type yes or no")
        if ready == yes:
            if b > 50: 
                print("Okay, I like the confidence.")
                globals points
                points = points - 50 
                print(f"dectective points = {points}")
                while i > 0: 
                    murderer: str = input("Who do you think is the murderer?")
                    if murderer == sus_1:
                        print("CONGRATS! YOU HAVE SOLVED THE MYSTERY") 
                        print("Looks like you've got great detective skills")
                        globals points 
                        points = points + 1000
                    else: 
                        print("That's not quite right. Sorry but I'm going to have to deduct 100 points.")
                        global points 
                        points = points - 100 
                        print(f"remaining detective points = {points}")
                        again: str = input("Would you like to try again? type yes or no")
                            if again == no: 
                                i = 0 
                            else: 
                                if b < 50 
                                    print("Sorry, looks like you don't have enough points to guess.")
                                    print("Play the other sections to accumlate points and try again!")
                                    i = 0
                    i = i 
            else: 
                print("Sorry, looks like you don't have enough points to guess.")
                print("Play the other sections to accumulate points and try again!")
            


    
def goodbye() -> None: 
    """Goodbye message."""
    print("I hope you enjoyed the game!")
    print("We hope to see you next time.")
    print("Before you go, here are the total points you have accumalated throughout the game:")
    print(points)

def greet() -> None: 
    """Introduction."""
    print("Welcome to the Sally's Murder Mystery")
    print("Before we begin, let's introduce ourselves. My name is Elizabeth")
    global player 
    player = input("What is your name? ")
    print(f"Hi {player}, it's very nice to meet you. I will be your guide through the mystery.")
    print('If you would like to read the intructions before beginning the game, type "instructions"')
    print('If you would like to begin the mystery without reading the instructions, type "continue"')
    a: str = "instructions"
    play: str = input("What would you like to do? ")
    if a == play: 
        print("How to Play")
        print("Choose a mystery you want to solve.")
        print("You will be given a list of options to choose from")
        print("Type in the option you want to solve the mystery")
        print("Each clue will lead you closer to solving the mystery.")
        print("If you find a clue, I will give you detective points.")
        print("The amount of points will be given at random.")
        print("These points are how you will ")
        print("To win the game, ")
    

if __name__ == "__main__":
    main () 