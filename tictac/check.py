from tictac.draw import drawBoard

winningCombinations = [
    ((0, 0), (0, 1), (0, 2)), # horizontal
    ((1, 0), (1, 1), (1, 2)), # horizontal
    ((2, 0), (2, 1), (2, 2)), # horizontal
    ((0, 0), (1, 0), (2, 0)), # vertical
    ((0, 1), (1, 1), (2, 1)), # vertical
    ((0, 2), (1, 2), (2, 2)), # vertical
    ((0, 0), (1, 1), (2, 2)), # diagonal
    ((0, 2), (1, 1), (2, 0)), # diagonal
]

def checkGame(board: list[list[str]]) -> str:
    for opt1, opt2, opt3 in winningCombinations:
        if board[opt1[0]][opt1[1]] == board[opt2[0]][opt2[1]] == board[opt3[0]][opt3[1]] and board[opt1[0]][opt1[1]] != ' ':
            return board[opt1[0]][opt1[1]]
    if ' ' not in board[0] and ' ' not in board[1] and ' ' not in board[2]:
        return 'T'
    return ''

def announce(board: list[list[str]], winner: str):
    drawBoard(board)
    print()
    if winner == "T":
        print("Tie! Nobody wins!")
    else:
      print(f"{winner} wins!")
    print()
    print("Game over!")

def checkTurn(board: list[list[str]], turn: str) -> str:
    # check if the game is continuing, announce winner or tie if needed
    # return empty string if game over, otherwise the new turn player
    result = checkGame(board)
    if result != "":
        announce(board, result)
        return ""
    else:
        return "X" if turn == "O" else "O"
    
def firstPlayer() -> str:
    return "X"
