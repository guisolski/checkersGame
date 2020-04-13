from position import Position 

#Class define one piece
class Piece():
    #Contructor of class
    def __init__(self,*_args):
        #inialize varibles
        self.type = None
        self.pos = Position()
        self.lady = False
        #Recive on argument, set pieace in Null space
        if len(_args) == 1:
            self.type = _args[0]
        #Recive on argument, set pieace in space
        elif len(_args) >= 2:
            self.type = _args[0]
            self.pos = _args[1]
    #Set value of position base in x and y
    def set_pos_XY(self,_x,_y):
        self.pos.x = _x
        self.pos.y = _y
 
   
    