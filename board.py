import numpy as np
class Board():
    def __init__(self, *_args):
        self.board =  None
        if len(_args) == 2:
            self.board = np.zeros((_args[0], _args[1]))
        else:
            self.board = np.zeros((10,10))
    def get_board(self):
        return self.board
    def set_obj_pos_board(self,_obj, _x,_y):
        self.board[_x][_y] = _obj
    def reset_pos_board(self,_x,_y):
        self.board[_x][_y] = 0


