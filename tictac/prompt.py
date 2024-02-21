from typing import Tuple

def goodbye() -> None:
  print()
  print("Goodbye!")
  exit()

def prompt(turn: str) -> Tuple[int, int]:
  print(f"Player \"{turn}\", it's your turn!")
  print("Or enter \"exit\" to quit the game.")
  promptString = f"Enter the coordinates for \"{turn}\" (separated by a space, eg. \"1 3\"): "

  while True:
    try:
      result = input(promptString)
      if result == "exit":
        raise KeyboardInterrupt
      x, y = map(int, result.split())
      if 1 <= x <= 3 and 1 <= y <= 3:
        return (x - 1, y - 1)
      else:
        print("Coordinates should be from 1 to 3!")
    except ValueError:
      print("You should enter numbers!")
    except IndexError:
      print("You should enter two numbers!")
    except KeyboardInterrupt:
      goodbye()
    except:
      print("Invalid input!")
