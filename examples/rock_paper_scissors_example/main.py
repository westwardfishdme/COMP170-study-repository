"""
This is a simple rewrite of one of my old command line for rock paper scissors.

I had recently rewrote this to better reflect what code at a COMP271
level should look like.
"""

from random import randint
from re import findall as regex

# we also need to get the PatternError for try/except
from re import PatternError
# we use our special errors file to print to STDERR
# should we run into any errors to log
from errors import eprint

# the WinResult class will hold our score


class Player():
    """
    Player class allows us to store our score values, and player choice values.
    """

    def __init__(self, choice: str | None = None):
        self.__win = 0
        self.__lose = 0
        self.__tie = 0
        self.__choice = choice

    # I did not write about decorators in the main readme because this is not
    # something that is expected of you at a 170 level, but essentially these
    # decorators specifically allow you to interact with attributes with
    # operators, or perform get operations without using a function notation.
    @property
    def win(self) -> int:
        """
        returns the wins of a player
        """
        return self.__win

    @property
    def lose(self) -> int:
        """
        returns the losses of a player
        """
        return self.__lose

    @property
    def tie(self) -> int:
        """
        returns the times a player tied
        """
        return self.__tie

    @property
    def choice(self) -> str:
        return self.__choice

    @choice.setter
    def choice(self, new_choice):
        self.__choice = new_choice

    def validate(self, cpu_choice: str):
        """
        Validates the user's choice
        """
        # this can probably be rewritten a bit better,
        # but for the sake of an example; works perfectly fine.

        print(f"I had chosen: {cpu_choice}")

        # check the win conditions:
        if self.__choice == cpu_choice:
            self.__tie += 1
            return
        match cpu_choice:
            case "rock":
                if self.__choice == "paper":
                    self.__win += 1
                if self.__choice == "scissors":
                    self.__lose += 1
            case "paper":
                if self.__choice == "scissors":
                    self.__win += 1
                if self.__choice == "rock":
                    self.__lose += 1
            case "scissors":
                if self.__choice == "rock":
                    self.__win += 1
                if self.__choice == "paper":
                    self.__lose += 1
        print(f"{self.__choice}, {cpu_choice}")

    def interpret(self, valid_opts: list):
        """
        attempt to interpret the user's option...
        we use a ReGEX to check if the string contains
        the user's substring...
        """
        for option in valid_opts:
            try:
                if regex(self.__choice, option):
                    print(f"you meant {option}!")
                    self.__choice = option
                    return
            except PatternError:
                eprint("regex ran into an error!: PatternError")
                exit(1)
        print("i could not find a valid option!")


def cpu_choose_random(valid_opts: list) -> str:
    """
    makes a cpu randomly choose an item.
    """
    # there are 3 options we can choose from: rock, paper, or scissors.

    # remember, lists start from 0, had set the size to just
    # valid_opts.__len__()->[3], we there is a 25% chance that when
    # choice is defined by randint(), we will receive an
    # error message because we are out of range.

    # we also want to do something like this, because say
    # in the future, we want to add something to that list,
    # say... a rocket launcher we can!
    size_rps = len(valid_opts)-1
    cpuidx_choice = randint(0, size_rps)
    print("I have made my choice, and I don't think you can guess what it is!")

    # we return a random choice from valid_opts
    # by using the integer as our index
    return valid_opts[cpuidx_choice]


# = lets run some code! = #

MAX_GAMES: int = 3


def main():
    total_games = 0
    valid_opts = ["rock", "paper", "scissors"]

    player: Player = Player()
    while (total_games < MAX_GAMES):
        # lets play best 2 out of 3.
        # there is better logic that we can
        # use, however since this is a demo
        # we should just do a maximum of 3 games

        # in order to use our methods, we have to call our UserInput class
        player.choice = str(input("\nWhat is your choice?: ")).lower()
        if player.choice == "q" or player.choice == "quit":
            exit(0)
        cpu = cpu_choose_random(valid_opts)

        if not valid_opts.__contains__(player.choice):
            print("that's not a proper option!")
            print("let me see if i can see what you meant...")

            # use our interpret method...
            player.interpret(valid_opts)

        # we validate the choices...
        player.validate(cpu)
        # print out the score.
        print(f"Score:\nWins: {player.win}\nLosses: {
              player.lose}\nTies:{player.tie}")
        total_games = player.lose+player.win+player.tie

    # print to tell the user that they won or lost

    if player.lose < player.win:
        print("You won!")
    elif player.lose > player.win:
        print("You lose!")
    else:
        print("We tied!")


# in most programs, you'll see main called like this, or defined under this.
# see more here: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    main()
