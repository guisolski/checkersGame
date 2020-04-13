from util import clear,input_validation_list
from checker import Checker
from position import Position
from person import Person

def start():
    start = input_validation_list(
            str("Choice side " +  u"\u25CF" + " (1) or "+ u"\u25CB" + " (2) : "),
            int,
            ["1","2"])
    type_of_player = {}
    number_of_piece = {"white": 20, "black": 20}
    if start == 1:
        turn = "human"
        type_of_player["human"] = "white"
        type_of_player["machine"] = "black"
    else:
        turn = "machine"
        type_of_player["machine"] = "white"
        type_of_player["human"] = "black"
    clear()
    loop = True
    game = Checker()
    return type_of_player, turn, loop, game, number_of_piece