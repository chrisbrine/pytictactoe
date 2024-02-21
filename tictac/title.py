import sys, os
from tictac.clear import clear

def wait_key():
    ''' Wait for a key press on the console and return it. '''
    result = None
    if os.name == 'nt':
        import msvcrt
        result = msvcrt.getwch()
    else:
        import termios
        fd = sys.stdin.fileno()

        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)

        try:
            result = sys.stdin.read(1)
        except IOError:
            pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

    return result

def instructions():
    clear()
    title()
    print()
    print("This should be a two player game")
    print("The board is as follows:")
    print("1 1|1 2|1 3")
    print("-----------")
    print("2 1|2 2|2 3")
    print("-----------")
    print("3 1|3 2|3 3")
    print("You will be 'X' and the the other player will be 'O'")
    print("You will be prompted to enter a number from 1 to 9")
    print("The number corresponds to the position on the board")
    print("The game will continue until there is a winner or a draw")
    print("Good luck!")
    print("Press any key when you are ready to start!")
    wait_key()

def title():
  print("Tic Tac Toe")
  print("By Chris Brine (https://github.com/chrisbrine)")
