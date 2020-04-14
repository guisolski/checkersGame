from util import easy_print
import start_variables
from walk import walk
from position import Position 
import sys
import time

def invalid_mensage():
    print("Invalid Input")
    time.sleep(1)

def select_piece(position,_game,_turn,_type_of_player):
    #walk return one point in space
    position = walk(position,_game)
    type_piece = _game.get_type_of_pos(position)
    if type_piece == _type_of_player[_turn]:
        return _game.get_piece(position)
    invalid_mensage()

    return select_piece(position,_game,_turn,_type_of_player)



if __name__ == "__main__":
    type_of_player, turn, loop, game,number_of_piece = start_variables.start()
    print(game.get_type_of_pos_XY(0,0))
    easy_print(game)
    while loop:
        #human trun play
        if turn == "human":
            before = select_piece(Position(0,0),game,turn,type_of_player)
            print("")
            
            turn = "machine"
        #machine player
        else:
            pass
       
        easy_print(game)
        sys.exit(1)