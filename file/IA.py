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

def l(piece):
    if piece.lady == True:
        return 5
    if piece.type == "white":
        return piece.pos.y
    return 9 - piece.pos.y 
def p(piece):
    return 1
def heuristic(piece):
    return l(piece) * p(piece)


def make_tree(_list):
    tree = []
    heuristic_piece = {}
    for i in _list:
        for a in _list[i]:
            if isinstance(a,list):
                for j in a:
                    h = heuristic(j)
                    heuristic_piece[h] =  j
                    tree.append(h)
            else:
                h = heuristic(a)
                heuristic_piece[h] =  a
                tree.append(h)
    return tree,heuristic_piece
    