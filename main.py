from tictac.draw import drawBoard
from tictac.board import createBoard, playBoard
from tictac.prompt import prompt
from tictac.check import checkTurn, firstPlayer
from tictac.title import instructions

def game():
  instructions()
  board = createBoard()
  turn = firstPlayer()

  while turn:
    drawBoard(board)
    row, col = prompt(turn)
    if playBoard(board, row, col, turn):
      turn = checkTurn(board, turn)
    else:
      print("Invalid move!")

game()