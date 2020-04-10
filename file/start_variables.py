import checker
import util
import position

def start():
    start = util.input_validation_list(
            str("Choice side " +  u"\u25CF" + " (1) or "+ u"\u25CB" + " (2) : "),
            int,
            ["1","2"])
    type_of_player = {}
    if start == 1:
        turn = "human"
        type_of_player["white"] = "human"
        type_of_player["black"] = "machine"
    else:
        turn = "machine"
        type_of_player["white"] = "machine"
        type_of_player["black"] = "human"
    util.clear()
    loop = True
        
    game = checker.Checker()


    return type_of_player, turn, loop, game