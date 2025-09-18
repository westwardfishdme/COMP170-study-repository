"""
This is a simple rewrite of one of my old command line games for rock paper
scissors it should cover all aspects, with the exception of cython, because
honestly, I only mention it as a passing by statement that you should know
about, but not really need to practice right now.
"""

from random import randint
from re import findall as regex

# we also need to get the PatternError for try/except
from re import PatternError
# we use our special errors file to print to STDERR
# should we run into any errors to log
from errors import eprint


class UserInput:
    """
     When we call UserInput without a method, we will always
     run all code inside of the:
     def __init__(self):

     so for example, say we have:

     >> user_in=UserInput(),

     our code inside of our `def __init__(self)` will run
     first.
    """

    def __init__(self):
        self.choice = str(input("\nWhat is your choice?: ")).lower()
        if self.choice == "q" or self.choice == "quit":
            exit(0)

    def interpret(self: str, valid_opts: list) -> str:

        # attempt to interpret the user's option...
        # we use a ReGEX to check if the string contains
        # the user's substring...
        for option in valid_opts:
            try:
                if regex(self.choice, option):
                    print(f"you meant {option}!")
                    return option
            except PatternError:
                eprint("regex ran into an error!: PatternError")
                break
        print("i could not find a valid option!")


# the WinResult class will hold our score
class WinResult:
    win = 0
    lose = 0
    tie = 0


def opponentsChoice(valid_opts: list) -> str:
    # there are 3 options we can choose from: rock, paper, or scissors.

    # remember, lists start from 0, had set the size to just
    # valid_opts.__len__()->[3], we there is a 25% chance that when
    # choice is defined by randint(), we will recieve an
    # error message because we are out of range.

    # we also want to do something like this, because say
    # in the future, we want to add something to that list,
    # say... a rocket launcher we can!
    size_rps = valid_opts.__len__()-1
    cpuidx_choice = randint(0, size_rps)
    print("\nI have made my choice, and I don't think you can guess what it is!")

    # we return a random choice from valid_opts
    # by using the integer as our index
    return valid_opts[cpuidx_choice]


def validate(user_choice: str, cpu_choice: str) -> ():
    print(f"I had chosen: {cpu_choice}")

    # check the win conditions:
    if user_choice == cpu_choice:
        WinResult.tie += 1
    match cpu_choice:
        case "rock":
            if user_choice == "paper":
                WinResult.win += 1
                return
            if user_choice == "scissors":
                WinResult.lose += 1
                return
        case "paper":
            if user_choice == "scissors":
                WinResult.win += 1
                return
            if user_choice == "rock":
                WinResult.lose += 1
                return
        case "scissors":
            if user_choice == "rock":
                WinResult.win += 1
                return
            if user_choice == "paper":
                WinResult.lose += 1
                return


# = lets run some code! = #
def main():
    total_games = 0
    valid_opts = ["rock", "paper", "scissors"]

    # lets play best 2 out of 3.
    # there is better logic that we can
    # use, however since this is a demo
    # we should just do a maximum of 3 games

    # you can edit this and create your own patch
    # by forking this repository!

    while (total_games < 3):

        # in order to use our methods, we have to call our UserInput class
        input = UserInput()
        cpu = opponentsChoice(valid_opts)

        # ask the user for their choice.

        # we can't find an option
        if not valid_opts.__contains__(input.choice):
            print("thats not a proper option!")
            print("let me see if i can see what you meant...")

            # use our interpret method...
            input.choice = input.interpret(valid_opts)

        # we validate the choices...
        validate(input.choice, cpu)
        # print out the score.
        print(f"Score:\nWins: {WinResult.win}\nLosses: {
              WinResult.lose}\nTies:{WinResult.tie}")
        total_games = WinResult.lose+WinResult.win+WinResult.tie

    # print to tell the user that they won or lost

    if WinResult.lose < WinResult.win:
        print("You won!")
    elif WinResult.lose > WinResult.win:
        print("You lose!")
    else:
        print("We tied!")


# in most programs, you'll see main called like this.
if __name__ == "__main__":
    main()


"""
NOTES:
"""
# in a real program/game, you typically want to define something
# that you wish to remain a secret at the time of the logic
# check. This is because when we create a variable,
# we are storing this in memory.

# Therefore, if someone where to say be running a software
# that can read the memory of our program, they can check
# what is stored and use that knowledge to cheat at our game.

# there are some cases where you need to store that information in memory,
# but the general idea is that if you can-- do it at a good time


# Additionally, instead of a list:
"""
e.g.
["rock","paper","scissors"]
"""
# a professional developer might use something
# called a  'config' file or any other external file
# so that the values are not hard coded into the game!
