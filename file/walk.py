from msvcrt import kbhit
from util import getKey,easy_print
from piece import Piece
from position import Position 
import time
#---------------------------------------------------------------------------
#print mensage of intruction
#---------------------------------------------------------------------------
def intruction():
    #print("Walk in W,A,S,D")
    print("Select to piece press F")
#---------------------------------------------------------------------------
def walk(_pos,game):
    old_pos = Position(_pos.x,_pos.y)    
    piece =  game.get_piece(old_pos)
    key = ""
    while key != "F":
        #verify if any key press
        if kbhit():
            key = getKey().upper()
            print(key)
            if key == 'A':
                _pos.x = _pos.x-1 if _pos.x >= 1 else _pos.x
            elif key == 'D':
                _pos.x = _pos.x+1 if _pos.x < game.line_size-1 else _pos.x
            elif key == 'W':
                _pos.y = _pos.y-1 if _pos.y >= 1 else _pos.y
            elif key == 'S':
                _pos.y = _pos.y+1 if _pos.y < game.line_size-1 else _pos.y
        if old_pos != _pos:
            game.set_piece(piece)
            old_pos.x = _pos.x
            old_pos.y = _pos.y
            piece = game.get_piece(_pos)
            game.set_piece(Piece(u"\u25AE"+u"\u25AE"+u"\u25AE"+u"\u25AE"+u"\u25AE",_pos))
        easy_print(game)
        intruction()
        time.sleep(0.2)
    game.set_piece(piece)
    easy_print(game)
    return _pos
#---------------------------------------------------------------------------