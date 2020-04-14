#-----------------------------------------------------------------------
#Import all function and class use in main
#-----------------------------------------------------------------------
from util import easy_print
import start_variables
from walk import walk
from position import Position 
import sys
import time
from piece import Piece
#---------------------------------------------------------------------------
#Print invalid mensage
#---------------------------------------------------------------------------
def invalid_mensage():
    print("Invalid Input")
    time.sleep(1)
#---------------------------------------------------------------------------
#Check piece of type of player turn
#---------------------------------------------------------------------------
def select_piece(position,_game,_turn,_type_of_player):
    #walk return one point in space
    position = walk(position,_game)
    type_piece = _game.get_type_of_pos(position)
    if type_piece == _type_of_player[_turn]:
        return _game.get_piece(position)
    invalid_mensage()

    return select_piece(position,_game,_turn,_type_of_player)
#-------------------------------------------------------------------------------
#Verify if this instace is main thered 
#-------------------------------------------------------------------------------
if __name__ == "__main__":
    #---------------------------------------------------------------------------
    #Incializa varibles
    #---------------------------------------------------------------------------
    type_of_player, turn, loop, game,number_of_piece = start_variables.start()
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
    #Print the board incialize
    easy_print(game)
    #---------------------------------------------------------------------------
    #Loop of the game
    #---------------------------------------------------------------------------
    while loop:
        #human trun play
        if turn == "human":
            pieces_eating  = game.verify_any_piece_eating(type_of_player[turn])
            if len(pieces_eating) > 0:
                print("eating")
                pass
            else:
                #---------------------------------------------------------------
                #Get piece select of player
                #---------------------------------------------------------------
                before = select_piece(Position(0,0),game,turn,type_of_player)
                #---------------------------------------------------------------
                #Get pos to move
                #---------------------------------------------------------------
                pieces_move = game.verify_diagonal_move(before)
                print(pieces_move)
            #-------------------------------------------------------------------
            #Change turn to machine
            #-------------------------------------------------------------------
            turn = "machine"
            #-------------------------------------------------------------------
        #machine player
        else:
            pass
        #-----------------------------------------------------------------------
        #Print board
        #-----------------------------------------------------------------------
        #easy_print(game)
        #-----------------------------------------------------------------------
        sys.exit(1)
#-------------------------------------------------------------------------------