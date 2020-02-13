"""
Stupidly overdone random number generator. Also used to test creating exceptions.
"""
import os
import random

class Error(Exception):
    """Base for user defined exceptions"""
    pass

class YesNoError(Error):
    """Raised when input isn't y or n"""
    pass

def build_str(num):
    """Creates a formatted string to display the number"""
    built_str = ("--------------------\n"
                "| Generated Number |\n"
                "--------------------\n"
                f"\t{num}\n")

    return built_str

def again_prompt():
    """Prompts the user to generate another number. 
    Throws an error if the response isn't y or n"""
    while True:
        try:
            go_again = str(input("Generate another number? (y/n): "))
            if go_again.lower() != "y" and go_again.lower() != "n":
                raise YesNoError
        except YesNoError:
            print("Please enter 'y' or 'n'!")
            continue
        else:
            break

    return go_again 

if __name__ == "__main__":

    rand = random.Random()
    clear = lambda: os.system('cls')
    clear()

    while True:
        try:
            max = int(input("Enter the maximum number: "))
        except ValueError:
            print("Please enter a number!")
            continue

        print(build_str(rand.randint(0, max)))
        go_again = again_prompt()

        if go_again.lower() != "y":
            break

        clear()
