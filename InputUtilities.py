from operator import concat
import re


class InputUtilities:
    def __init__(self):
        pass

    @staticmethod
    def setName():
        nameInput = input("What is the name of this player? ")
        nameInput = re.sub(r'#\?\$%-!@^<>/\\\|', '', nameInput)
        print("Thank you for entering your name,", nameInput)
        return nameInput

    @staticmethod
    def nextCell(currentPlayer):
        cellLocation = input(
            concat(currentPlayer.getPlayerName(), ", What spot would you like next? "))
        try:
            isinstance(int(cellLocation), int)
        except ValueError:
            print('This is not a valid integer. Please try again.')
        else:
            cellLocation = int(cellLocation)

        if (cellLocation in range(1, 10)):
            return cellLocation
        else:
            print("The only valid entries are 1 through 9. Please try again!")
            InputUtilities.nextCell(currentPlayer)
