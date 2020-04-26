import os
from msvcrt import getch
#---------------------------------------------------------------------------
def input_validation_list(_text,_type,_list):
    v = input(_text)
    try:
        if v in _list:
            return _type(v)
    except:
        return input_validation_list(_text,_type,_list)
#---------------------------------------------------------------------------
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
#---------------------------------------------------------------------------
def getKey():
    #get key press and elimate trash of return
    return str(getch()).replace("b","").replace("'","").replace("\n"," ").replace(" ","").strip()
#---------------------------------------------------------------------------
def easy_print(game):
    clear()
    game.print_board()
#---------------------------------------------------------------------------
def dic_keys(dic):
    #flat_list = list(dic.keys())
    #flatten = lambda l: [item for sublist in l for item in sublist]
    return list(dic.keys())
#---------------------------------------------------------------------------
def dic_values(dic):
    flat_list = list(dic.values())
    flatten = lambda l: [item for sublist in l for item in sublist]
    return flatten(flat_list)


def origin_piece(moviment,piece_move):
    #index the move
    index_m = 0
    #this is value of move, inicialize them first element of dic
    before =  next(iter(piece_move))
    for i in piece_move:
        if moviment in piece_move[i]:
            index_m = piece_move[i].index(moviment)
            before = i
            return before, index_m
    return None