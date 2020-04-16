#-----------------------------------------------------------------------
#Import all function and class use in main
#-----------------------------------------------------------------------
from util import dic_keys, dic_values,easy_print
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
#---------------------------------------------------------------------------
#Draw squares to eating
#---------------------------------------------------------------------------
def draw_eat(_game,_list):
    if isinstance(_list, list):
        values = _list
    else:
        values = dic_values(_list)
    for i in range(len(_list)):
        values[i].type = u"\u25E4 "+str(i)+u" \u25E5"
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
        show_mensage("Select another piece")
        return recursion_move_piece(game,turn,type_of_player)
    #------------------------------------------------------------    
    return before,pieces_move
#-------------------------------------------------------------------------------
def select_eat(_list):
    if isinstance(_list, list):
        values = _list
    else:
        values = dic_values(_list)
    try:
        eat = int(input("Select eat: "))
    except:
        select_eat(_list)
    if eat >=0 and eat < len(_list):
        set_blank(values)
        return eat
    return select_eat(_list)
#-------------------------------------------------------------------------------
def select_move(piece__move):
    mesage = "Try Again"
    try:
        move = int(input("Select move: "))
    except:
        show_mensage(mesage)
        select_move(pieces_move)
    if move >= 0 and move < len(pieces_move):
        set_blank(pieces_move)
        return move
    show_mensage(mesage)
    return select_move(pieces_move)
#-------------------------------------------------------------------------------
def piece_delete(before,after):
    #----------------------------
    x_delete = before.pos.x
    if after.pos.x > before.pos.x:
        x_delete += 1
    elif after.pos.x < before.pos.x:
        x_delete -= 1
    elif after.pos.x == before.pos.x:
        if after.pos.x == 1:
            x_delete -= 1
        elif after.pos.x == 8:
            x_delete += 1
    #----------------------------
    y_delete = before.pos.y
    if after.pos.y > before.pos.y:
        y_delete += 1
    elif after.pos.y < before.pos.y:
        y_delete -= 1 
    return game.get_piece(Position(x_delete,y_delete))
#-------------------------------------------------------------------------------
def eat_again (piece,game):
    pieces_eat  = game.verify_diagonal_eating(piece)
    if len(pieces_eat) > 0:
        easy_print(game)
        print(piece.type)
        piece.pos._print()
        draw_eat(game,pieces_eat)
        eat = select_eat(pieces_eat)
        delete = piece_delete(piece,pieces_eat[eat])
        delete.type = "blank"
        number_of_piece["machine"] = number_of_piece["machine"]-1
        game.move(piece,pieces_eat[eat])
        easy_print(game)
        return eat_again(piece,game)
#-------------------------------------------------------------------------------
#Verify if this instace is main thered 
#-------------------------------------------------------------------------------
if __name__ == "__main__":
    #---------------------------------------------------------------------------
    #Incializa varibles
    #---------------------------------------------------------------------------
    type_of_player, turn, loop, game,number_of_piece = start_variables.start()
    game.move(game.get_piece(Position(2,3)),game.get_piece(Position(0,5)))
    game.move(game.get_piece(Position(1,2)),game.get_piece(Position(2,3)))
    #---------------------------------------------------------------------------
    #Print the board incialize
    #easy_print(game)
    #---------------------------------------------------------------------------
    #Loop of the game
    #---------------------------------------------------------------------------
    while loop:
        #human trun play
        if turn == "human" :
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
                draw_eat(game,pieces_eating)
                eat = select_eat(pieces_eating)
                keys = dic_keys(pieces_eating)
                values = dic_values(pieces_eating)
                before,after = keys[0], values[0]
                delete = piece_delete(before,after)
                delete.type = "blank"
                number_of_piece["machine"] = number_of_piece["machine"]-1
                game.move(keys[eat],values[eat])
                eat_again(keys[eat],game)
                #---------------------------------------------------------------
            #-------------------------------------------------------------------
            #If not select one piace to move
            #-------------------------------------------------------------------
            else:
                #-------------------------------------------------------------------
                before, pieces_move = recursion_move_piece(game,turn,type_of_player)
                #-------------------------------------------------------------------
                #Dray possiblity to move
                #-------------------------------------------------------------------
                draw_move(game,pieces_move)
                #-------------------------------------------------------------------
                move = select_move(pieces_move)
                game.move(before,pieces_move[move])
                #-------------------------------------------------------------------
            #-------------------------------------------------------------------
            #Change turn to machine
            #-------------------------------------------------------------------
            turn = "machine"
            #-------------------------------------------------------------------
        #machine player
        else:
            turn = "human"
        #-----------------------------------------------------------------------
        #Print board
        #-----------------------------------------------------------------------
        easy_print(game)
        #-----------------------------------------------------------------------
        #sys.exit(1)
#-------------------------------------------------------------------------------