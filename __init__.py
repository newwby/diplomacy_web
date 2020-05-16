
# INITIAL VERSION FOR OFFLINE BELOW
# SECOND ED. ASSUMES GAME IS ALWAYS IN AN 'ON' STATE AND CAN BE RESET BY ADMIN COMMANDS

from colorama import Fore
from global_scripts.console import clear
import global_data.session_store as session

valid_command = False
while valid_command is False:
    clear()
    valid_command = input(Fore.BLUE + "\nEnter your USER ID: \n")
    if valid_command in session.user_ID:
        # execute log-in process
        pass
    else:
        valid_command = False
        print("User not found.")

"""

while valid_command is False:
    clear()
    print("Welcome to DIPLOMACY.\nWould you like to start a new game or load a game in progress?")
    print("(Type NEW, LOAD, or QUIT)")
    menu_command = input()
    if menu_command.upper() not in ["NEW", "LOAD", "QUIT"]:
        print("Incorrect command.")
    else:
        valid_command == menu_command.upper()
        break

if valid_command == "NEW":
    # execute game startup
    quit()
elif valid_command == "LOAD":
    # load save list into memory, offer selection, load chosen save hash
    quit()
elif valid_command == "QUIT":
    # game stops
    quit()
"""
