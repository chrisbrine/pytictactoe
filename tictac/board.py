def createBoardRow() -> list[str]:
    return [' ' for _ in range(3)]

def createBoard() -> list[list[str]]:
    return [createBoardRow() for _ in range(3)]

def playBoard(board: list[list[str]], row: int, col: int, player: str) -> bool:
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    return False