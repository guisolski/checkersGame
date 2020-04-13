import checker
import util
import position
import start_variables
import walk
import sys
import time

def invalid_mensage():
    print("Invalid")
    time.sleep(3)

def select_piece(_game,_player,_type_of_player):
    #walk return one point in space
    before = walk.walk(0,0,_game)
    type_piece = _game.get_type_of_pos(before)
    if type_piece == _type_of_player[_player]:
        return _game.get_piece(before)
    invalid_mensage()

    return select_piece(_game,_player,_type_of_player)



if __name__ == "__main__":
    type_of_player, turn, loop, game = start_variables.start()
    print(game.get_type_of_pos_XY(0,0))
    util.easy_print(game)
    while loop:
        #human trun play
        if turn == "human":
            
            select_piece(game,turn,type_of_player)
            print("")
            
            turn = "machine"
        #machine player
        else:
            pass
       
        util.easy_print(game)
        sys.exit(1)