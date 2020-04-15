#-------------------------------------------------------------------------------
#Import function and class use in start variables
#-------------------------------------------------------------------------------
from util import clear,input_validation_list
from checker import Checker
from position import Position
#-------------------------------------------------------------------------------
#Start all variables use in main
#-------------------------------------------------------------------------------
def start():
    start = input_validation_list(
            str("Choice side " +  u"\u25CF" + " (1) or "+ u"\u25CB" + " (2) : "),
            int,
            ["1","2"])
    type_of_player = {}
    number_of_piece = {"human": 20, "machine": 20}
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
#-------------------------------------------------------------------------------