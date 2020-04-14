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