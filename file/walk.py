import msvcrt
import util
import piece as class_piece
import position 
import time

def intruction():
    print("Select to piece press F")

def walk(x,y,game):
    old_x, old_y = x,y    
    key = ""
    piece =  game.get_piece(position.Position(0,0))
 
    while key != "f":
        if msvcrt.kbhit():
            key = util.getKey()
            print(key)
            if key == 'a':
                x = x-1 if x >= 1 else x
            elif key == 'd':
                x = x+1 if x <= game.get_line_size()-2 else x
            elif key == 'w':
                y = y-1 if y >= 1 else y
            elif key == 's':
                y = y+1 if y <= game.get_line_size()-2 else y
        if old_x != x or old_y != y:
            game.set_piece(piece)
            old_x = x
            old_y = y
            pos = position.Position(x,y)
            piece = game.get_piece(pos)
            game.set_piece(class_piece.Piece(u"\u25AE"+u"\u25AE"+u"\u25AE",pos))
        util.easy_print(game)
        intruction()
        time.sleep(0.1)
    game.set_piece(piece)
    util.easy_print(game)
    return position.Position(x,y)
    