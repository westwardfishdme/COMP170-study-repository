"""
This file is an example of what your code after 170 should look like.
This will create a file in your current directory called example.txt
and contain some text that the user has written.

Think of it as a really basic text editor, like "ed"
"""


def create_file(filename: str, text: list[str]):
    """
    Creates a file with some text. Takes a list of strings
    as a parameter and prints it out to the file.
    """
    with open(filename, 'w') as file:
        for line in text:
            file.write(line+"\n")


SAVE_KEYWORD: str = "\\save"


def main():

    all_user_text: list[str] = []
    user_input = ""
    print(f"enter '{SAVE_KEYWORD}' when finished writing:")

    # get all the text from our user. Once they are done typing a single line
    # we push all their text to a list. For them to save; we want them to type
    # \save
    while user_input != SAVE_KEYWORD:
        user_input = input("")
        # we dont want our control word to be appended!
        if user_input != SAVE_KEYWORD:
            all_user_text.append(user_input)

    my_filename = input("What do you want the name of your file to be?: ")
    # create our file!
    create_file(my_filename, all_user_text)


main()
