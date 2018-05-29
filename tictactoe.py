import random

class Player():
    def __init__(self, name, symbol, score=0, turn=False):
        self.name = name
        self.symbol = symbol
        self.score = score
        self.turn = turn

    # Function to return all player data in a dict. 
    # Data is more organized, and can be retrevied quicker.
    def player_data(self):
        return {"Name": self.name, "Symbol": self.symbol, "Score": self.score,
        "Turn": self.turn}

class Board():
    # Creates an empty board, for when a new game starts.
    def __init__(self):
        self.position = [
                        ["0", "0", "0"],
                        ["0", "0", "0"],
                        ["0", "0", "0"],
                        ]
    # Board class function, that displays a nice graphical board, whenever a position is entered.
    def print_board(self):
        s, i = "-" * 9,  "/"
        pos_index = self.position
        print pos_index[0][0], i, pos_index[0][1], i, pos_index[0][2]
        print s
        print pos_index[1][3], i, pos_index[1][4], i, pos_index[1][5]
        print s
        print pos_index[2][6], i, pos_index[2][7], i, pos_index[2][8]

# A custom exception, derived from Exception class.
class CustomError(Exception):
    pass

# Function where the player enters their name, and selects a char/symbol.
# Function validates the data, so it doesn't contain numerical characters / spaces.
def player():
    while True:
        try:
            new_name = raw_input("> Name: ").capitalize()
            for i in new_name:
                if i.isdigit():
                    raise ValueError
            if new_name == "" or new_name.isspace():
                raise TypeError
            break
        except ValueError:
            print("Console: No numeric, or alphanumeric characters! You've entered " "( " + new_name + " )")
        except TypeError:
            print("Console: Enter a name!")
    while True:
        try:
            new_symbol = raw_input("> Symbol: ").capitalize()
            for i in new_symbol:
                if i.isdigit():
                    raise ValueError
            if new_symbol == "" or new_symbol.isspace():
                raise TypeError
            elif new_symbol != "X" and new_symbol != "O":
                raise CustomError
            break
        except ValueError:
            print("Console: No numeric, or alphanumeric characters! You've entered ( " + new_symbol + " )")
        except TypeError:
            print("Console: No empty spaces!")
        except CustomError:
            print("Console: You must pick either, x or o")
    player = Player(new_name, new_symbol)
    return player.player_data()
new_player = player()
board = Board()

# A function to check whether the chosen position is available.
def position_available(position_input):
    #if position in range(0,2): 
    #elif position in range (3,5):
    #elif position in range (6,8):
    pass


def position_input():
    while True:
        try:
            new_position = int(raw_input("> Position(0-8): "))
            if new_position not in range(0,8):
                raise CustomError
            elif new_position in range(0,8):
                board.position.insert(new_position, new_player.get('Symbol'))
                board.print_board()
        except ValueError:
            print("Console: Choose positions from 0 - 8")
        except CustomError:
            print("Console: Your chosen position is out of range!")
    return new_position
position_input()
