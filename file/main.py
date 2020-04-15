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
def show_mensage(text):
    print(text)
    time.sleep(1)
#---------------------------------------------------------------------------
#Check piece of type of player turn
#---------------------------------------------------------------------------
def select_piece(position,_game,_turn,_type_of_player):
    #------------------------------
    #walk return one point in space
    #------------------------------
    position = walk(position,_game)
    type_piece = _game.get_type_of_pos(position)
    if type_piece == _type_of_player[_turn]:
        return _game.get_piece(position)
    show_mensage("Invalid Input")
    return select_piece(position,_game,_turn,_type_of_player)
#---------------------------------------------------------------------------
#Draw squares to move
#---------------------------------------------------------------------------
def draw_move(_game,_list):
    for i in range(len(_list)):
        _list[i].type = u"\u25E4 "+str(i)+u" \u25E5"
    easy_print(game)    
#-------------------------------------------------------------------------------
#Set piece blank based in list
#-------------------------------------------------------------------------------
def set_blank(_list):
    for i in range(len(_list)):
        _list[i].type = "blank"
#-------------------------------------------------------------------------------    
#-------------------------------------------------------------------------------
def recursion_move_piece(game,turn,type_of_player):
    #------------------------------------------------------------
    #Get piece select of player
    #------------------------------------------------------------
    before = select_piece(Position(0,0),game,turn,type_of_player)
    #------------------------------------------------------------
    #Get pos to move
    #------------------------------------------------------------
    pieces_move = game.verify_diagonal_move(before)
    #------------------------------------------------------------
    #verify piece exixte move
    #------------------------------------------------------------
    if len(pieces_move) == 0:
        show_mensage("S'elect another piece")
        return recursion_move_piece(game,turn,type_of_player)
    #------------------------------------------------------------    
    return before,pieces_move
#-------------------------------------------------------------------------------
def select_move(piece__move, before):
    mesage = "Try Again"
    try:
        move = int(input("Select move: "))
    except:
        show_mensage(mesage)
        select_move(pieces_move,before)
    if move >= 0 and move < len(pieces_move):
        set_blank(pieces_move)
        game.move(before,pieces_move[move])
        return True
    show_mensage(mesage)
    return select_move(pieces_move,before)
#-------------------------------------------------------------------------------
#Verify if this instace is main thered 
#-------------------------------------------------------------------------------
if __name__ == "__main__":
    #---------------------------------------------------------------------------
    #Incializa varibles
    #---------------------------------------------------------------------------
    type_of_player, turn, loop, game,number_of_piece = start_variables.start()
    #---------------------------------------------------------------------------
    #Print the board incialize
    easy_print(game)
    #---------------------------------------------------------------------------
    #Loop of the game
    #---------------------------------------------------------------------------
    while loop:
        #human trun play
        if turn == "human":
            #-------------------------------------------------------------------
            #Get any piece possibility eating 
            #-------------------------------------------------------------------
            pieces_eating  = game.verify_any_piece_eating(type_of_player[turn])
            #-------------------------------------------------------------------
            #If exist any piece to eating, eat
            #-------------------------------------------------------------------
            if len(pieces_eating) > 0:
                #---------------------------------------------------------------
                #Dray possiblity to eat
                #---------------------------------------------------------------
                draw_move(game,pieces_eating)
                #---------------------------------------------------------------
            #-------------------------------------------------------------------
            #If not select one piace to move
            #-------------------------------------------------------------------
            else:
                before, pieces_move = recursion_move_piece(game,turn,type_of_player)
                #Dray possiblity to move
                #---------------------------------------------------------------
                draw_move(game,pieces_move)
                #---------------------------------------------------------------
                select_move(pieces_move,before)

            #-------------------------------------------------------------------
            #Change turn to machine
            #-------------------------------------------------------------------
            turn = "machine"
            #-------------------------------------------------------------------
        #machine player
        else:
            turn = "human"
            pass
        #-----------------------------------------------------------------------
        #Print board
        #-----------------------------------------------------------------------
        easy_print(game)
        #-----------------------------------------------------------------------
        #sys.exit(1)
#-------------------------------------------------------------------------------