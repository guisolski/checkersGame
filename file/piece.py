import position 

#Class define one piece
class Piece():
    #Contructor of class
    def __init__(self,*_args):
        #inialize varibles
        self.type = None
        self.pos = position.Position()
        self.king = False
        #Recive on argument, set pieace in Null space
        if len(_args) == 1:
            self.type = _args[0]
        #Recive on argument, set pieace in space
        elif len(_args) >= 2:
            self.type = _args[0]
            self.pos = _args[1]

    #Set value of type
    def set_type(self, _type):
        self.type = _type
    #Set value of position
    def set_pos(self, _pos):
        self.pos = _pos
    #Set value of position base in x and y
    def set_pos_XY(self,_x,_y):
        self.pos.set_x(_x)
        self.pos.set_x(_y)
    #Set value of king variable
    def set_king(self, _king):
        self.king = _king
    #Return value of type   
    def get_type(self):
        return self.type
    #Return value of position   
    def get_pos(self):
        return self.pos
    #Return value of king    
    def get_king(self):
        return self.king
    