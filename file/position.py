#-------------------------------------------------------------------------------
#Class define one point in space 2D
#-------------------------------------------------------------------------------
class Position():
    #---------------------------------------------------------------------------
    #Contructor of class
    #---------------------------------------------------------------------------
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
            '''
                I can't accept negative because python when receiving
                -1 in the array returns the last position
            '''
            self.x = int(_args[0]) if _args[0] >= 0 else None
            self.y = int(_args[1]) if _args[1] >= 0 else None
        #Recive another arguments creat Null space 
        else:
            self.x = None
            self.y = None
    #---------------------------------------------------------------------------
    #Simple print positon
    #---------------------------------------------------------------------------
    def _print(self):
        print(self.x, ":", self.y)
    #---------------------------------------------------------------------------