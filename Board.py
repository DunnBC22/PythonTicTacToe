from InputUtilities import InputUtilities as IU


class Board:
    def __init__(self):
        self.aBoard = [x for x in range(10)]

    def resetBoard(self):
        self.aBoard = [x for x in range(10)]
        print('The board has been reset successfully!')

    def showCurrentBoard(self):
        print('\nUpdated Board\n-------------------')
        for x in range(1, len(self.aBoard)):
            print('| ', self.aBoard[x], ' ', end='')
            if ((x % 3) == 0):
                print('| \n-------------------')
        print('\n')

    def spaceAvailable(self, currentSpotValue):
        self.currentSpotValue = currentSpotValue
        if ((self.currentSpotValue != 'X') and (self.currentSpotValue != 'O')):
            return True
        else:
            return False

    def updateBoard(self, spot, symbol, currentPlayer):
        self.spot = spot  # cellLocation
        self.symbol = symbol  # currentPlayer symbol
        self.currentPlayer = currentPlayer  # currentPlayer
        currentSpotValue = self.aBoard[self.spot]
        if (self.spaceAvailable(currentSpotValue)):
            self.aBoard[self.spot] = self.symbol
            self.showCurrentBoard()
        if (not(self.spaceAvailable(currentSpotValue))):
            self.spot = IU.nextCell(self.currentPlayer)
            self.aBoard[self.spot] = self.symbol
            self.showCurrentBoard()

    def check4Winner(self, userSymbol):
        self.userSymbol = userSymbol
        return (((self.aBoard[1]) == userSymbol) and ((self.aBoard[2]) == userSymbol) and ((self.aBoard[3]) == userSymbol)) or \
            (((self.aBoard[4]) == userSymbol) and ((self.aBoard[5]) == userSymbol) and ((self.aBoard[6]) == userSymbol)) or \
            (((self.aBoard[7]) == userSymbol) and ((self.aBoard[8]) == userSymbol) and ((self.aBoard[9]) == userSymbol)) or \
            (((self.aBoard[1]) == userSymbol) and ((self.aBoard[4]) == userSymbol) and ((self.aBoard[7]) == userSymbol)) or \
            (((self.aBoard[2]) == userSymbol) and ((self.aBoard[5]) == userSymbol) and ((self.aBoard[8]) == userSymbol)) or \
            (((self.aBoard[3]) == userSymbol) and ((self.aBoard[6]) == userSymbol) and ((self.aBoard[9]) == userSymbol)) or \
            (((self.aBoard[1]) == userSymbol) and ((self.aBoard[5]) == userSymbol) and ((self.aBoard[9]) == userSymbol)) or \
            (((self.aBoard[3]) == userSymbol) and (
                (self.aBoard[5]) == userSymbol) and ((self.aBoard[7]) == userSymbol))
