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