from Player import Player
from Board import Board
from InputUtilities import InputUtilities as IU


def playGame():
    # initiate the two players
    player_one = Player(IU.setName(), 'X')
    player_two = Player(IU.setName(), 'O')

    # set the gameboard
    gameBoard = Board()
    gameBoard.showCurrentBoard()

    for turn in range(100):
        if ((turn % 2) == 0):
            current_player = player_one
        elif ((turn % 2) == 1):
            current_player = player_two

        current_player.nextMove(current_player, gameBoard)

        if (gameBoard.check4Winner(current_player.getPlayerSymbol())):
            print('Congrats!', current_player.getPlayerName(), 'won!')
            quit()


if __name__ == '__main__':
    playGame()
    quit()
