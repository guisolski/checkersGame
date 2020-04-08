class Piece():
    def __init__(self,*_args):
        self.type = None
        self.x = None
        self.y = None
        if(len(_args) == 1):
            self.type = _args[0]
        elif (len(_args) == 3):
            self.type = _args[0]
            self.x = _args[1]
            self.y = _args[2]
    def set_type(self, _type):
        self.type = _type
    def set_x(self,_x):
        self.x =_x
    def set_y(self,_y):
        self.y =_y
    def get_type(self):
        return self.type
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    
    
    
