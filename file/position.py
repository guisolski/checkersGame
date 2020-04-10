#Class define one point in space 2D
class Position():
    #Contructor of class
    def __init__(self, *_args):
        #Recive one list in arguments create position in space
        if len(_args) == 1:
            if len(_args[0]) == 2:
                self.x =  _args[0][0]
                self.y =  _args[0][1]
            else:
                self.x = None
                self.y = None
        #Recive two arguments create position in space
        elif len(_args) == 2:
            self.x = int(_args[0])
            self.y = int(_args[1])
        #Recive another arguments creat Null space 
        else:
            self.x = None
            self.y = None

    #Set value X in space
    def set_x(self,_x):
        self.x =_x
    #Set value Y in space      
    def set_y(self,_y):
        self.y =_y
    #Return value of X in space
    def get_x(self):
        return self.x
    #Return value of Y in space
    def get_y(self):
        return self.y
    #Simple print positon
    def _print(self):
        print(self.get_x(), ":", self.get_y())