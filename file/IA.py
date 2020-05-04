from position import Position
from util import origin_piece 
import sys
def get_piece_move(game,type_of_player):
    piece_move = {}

    if type_of_player["machine"] == "white":
        for i in game.white_piece:
            move = game.verify_diagonal_move(i)
            if len(move) > 0:
                piece_move[i] = move
        return piece_move
    else:
        for i in game.black_piece:
            move = game.verify_diagonal_move(i)
            if len(move) > 0:
                piece_move [i] = move
        return piece_move
#distance of to changing to lady
def l(piece,_type):
    if piece.lady == True:
        return 5
    if _type == "white":
        return piece.pos.y
    return 9 - piece.pos.y
#protection 
def p(_game,_piece,_type,_piece_move):
    pos =  _piece.pos
    value = 1
    left = Position()
    rigth = Position()
    if _type == "white":
        left = Position(pos.x-1, pos.y+1)
        rigth = Position(pos.x+1, pos.y+1)
    elif _type == "black":
        left = Position(pos.x-1, pos.y-1)
        rigth = Position(pos.x+1, pos.y-1)

    try:
        if _game.get_piece(left).type == _type:
            before,index_m = origin_piece(_piece,_piece_move)
            if left.x != before.pos.x:
                value += 1
    except:
        pass
    try:
        if _game.get_piece(rigth).type == _type:
            before,index_m = origin_piece(_piece,_piece_move)
            if rigth.x != before.pos.x:
                    value += 1
    except:
        pass
    return value
#enemy close
def e(_game,_piece,_type,_type2,_piece_move):
    pos =  _piece.pos
    value = 1
    left = Position()
    rigth = Position()
    if _type == "white":
        left = Position(pos.x-1, pos.y+1)
        rigth = Position(pos.x+1, pos.y+1)
    elif _type == "black":
        left = Position(pos.x-1, pos.y-1)
        rigth = Position(pos.x+1, pos.y-1)

    try:
        if _game.get_piece(left).type == _type2:
            before,index_m = origin_piece(_piece,_piece_move)
            if left.x != before.pos.x:
                value += 1
    except:
        pass
    try:
        if _game.get_piece(rigth).type == _type2:
            before,index_m = origin_piece(_piece,_piece_move)
            if rigth.x != before.pos.x:
                    value += 1
    except:
        pass
    return value
def heuristic(_game,_piece,_type,_piece_move):
    _type2 = "white" if _type == "black" else "black"
    val = l(_piece,_type) + p(_game,_piece,_type,_piece_move) - e(_game,_piece,_type,_type2,_piece_move)
    return val

def make_tree(_game,_list,_type,_piece_move):
    tree = []
    heuristic_piece = {}
    for i in _list:
        for a in _list[i]:
            if isinstance(a,list):
                for j in a:
                    h = heuristic(_game,j,_type,_piece_move)
                    heuristic_piece[h] =  j
                    tree.append(h)
            else:
                h = heuristic(_game,a,_type,_piece_move)
                heuristic_piece[h] =  a
                tree.append(h)
    return tree,heuristic_piece
    