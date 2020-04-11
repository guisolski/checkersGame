import position 

#Class define one board
class Board():
    #Contructor of class
    def __init__(self, *_args):
        self.board =  None
        if len(_args) == 2:
            self.board = [[0]*_args[0],]*_args[1]
        elif len(_args) == 3:
            '''
               don't use the short cut to creat matrix, nor the numpy, because te _agars is a 
               new object necessary lock new space in memory for then.
            '''
            self.board = []
            for line in range(_args[1]):
                _append = []
                for col in range(_args[2]):
                    _append.append(_args[0])
                self.board.append(_append)
    
    #Return board matrix 
    def get_board(self):
        return self.board
    #Return value in positon(x,y)
    def get_pos(self,_pos):
        return self.board[_pos.get_y()][_pos.get_x()]
    #Return value in x,y
    def get_pos_XY(self,_x,_y):
        return self.board[_x][_y]
    #Setter value/object in pos 
    def set_value_pos(self,_obj, _pos):
        self.board[_pos.get_y()][_pos.get_x()] = _obj
    '''
        I did not consider the value how piece, beacause i wanted to make more abstract.
        So is necessary pass value of position too
    '''
    def set_piece(self,_obj):
        self.board[_obj.get_pos().get_y()][_obj.get_pos().get_x()] = _obj
    #Simple print of board
    def _print(self):
        for i in self.board:
            for a in i:
                print(a.get(),end=",")
            print("")

