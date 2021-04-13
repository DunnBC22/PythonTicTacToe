from InputUtilities import InputUtilities as IU


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def getPlayerName(self):
        return (self.name)

    def getPlayerSymbol(self):
        return (self.symbol)

    def nextMove(self, currentPlayer, aBoard):
        self.currentPlayer = currentPlayer
        self.aBoard = aBoard
        cellLocation = IU.nextCell(self.currentPlayer)
        self.aBoard.updateBoard(cellLocation,
                                self.symbol, self.currentPlayer)
