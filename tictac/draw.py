from tictac.clear import clear
from tictac.title import title

def drawBoard(board: list[list[str]]):
    clear()
    title()
    print("  1 2 3")
    for i in range(3):
        print(i + 1, end=" ")
        for j in range(3):
            if j < 2:
                print(board[i][j], end="|")
            else:
                print(board[i][j])
        if i < 2:
            print("  -----")