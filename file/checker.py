import piece as class_piece
import board as class_board
import position 

#Class define one board of cheacker and verify moviments possible
class Checker():
    #Contructor of class
    def __init__(self): 
        self.line_size = 10
        self.col_size = 10
        self.board = self.inicialize_board()
    
    #Inicialize piece in board
    def inicialize_board(self):
        p = class_piece.Piece()
        board = class_board.Board(p,self.line_size,self.col_size)
        for line in range(self.line_size):
            for col in range(self.col_size):
                pos = position.Position(col,line)
                if (line == 0 or line == 2) and col%2 != 0:
                    board.set_piece(class_piece.Piece("black",pos))
                elif (line == 1 or line == 3) and col%2 == 0:
                    board.set_piece(class_piece.Piece("black",pos))
                elif (line == 9 or line == 7) and col%2 == 0:
                    board.set_piece(class_piece.Piece("white",pos))
                elif (line == 8 or line == 6) and col%2 != 0:
                    board.set_piece(class_piece.Piece("white",pos))
                else:
                    board.set_piece(class_piece.Piece("__",pos))
        return board

    #move piece based in positions
    def move(self,pos_before,pos_after):
        #Get piece in pos changing
        obj_in_pos_before = self.board.get_pos(pos_before)
        obj_in_pos_after  = self.board.get_pos(pos_after)
        #Set new pos in piece
        obj_in_pos_before.set_pos(pos_after)
        obj_in_pos_after.set_pos(pos_before)
        #Changing piece of places
        self.board.set_value_pos(obj_in_pos_after,pos_before)
        self.board.set_value_pos(obj_in_pos_before,pos_after)
    #return action  possibilities of piece in determine position
    def possibility_action(self, _pos):
        return self.verify_diagonal(self.board.get_pos(_pos))
    #return possivility action of piece
    def verify_diagonal(self,_piece):
        pos = _piece.get_pos()
        possibility = []
        if _piece.get_king() == False:
            if _piece.get_type() == "white": 
                '''
                    Try test if the next postion not of board
                '''
                try:
                    #type diagonal left of piece
                    type_left = self.get_type_of_pos(position.Position(
                        pos.get_x()-1, pos.get_y()-1))
                except:
                    type_left = ""
                try:
                    #type diagonal rigth of piece
                    type_rigth = self.get_type_of_pos(position.Position(
                        pos.get_x()+1, pos.get_y()-1))
                except:
                    type_rigth = ""
                #verify move to diagonal left    
                if type_left == "_":
                        possibility.append("move left")
                elif type_left == "black":
                        possibility.append("eat left")
                #verify move to diagonal rigth
                if type_rigth == "_":
                        possibility.append("move rigth")
                elif type_rigth == "black":
                        possibility.append("eat rigth")

            elif _piece.get_type() == "black":
                '''
                    Try test if the next postion not of board
                '''
                try:
                    #type diagonal left of piece
                    type_left = self.get_type_of_pos(position.Position(
                    pos.get_x()+1, pos.get_y()-1))
                except:
                    type_left = ""
                try:
                    #type diagonal rigth of piece
                    type_rigth = self.get_type_of_pos(position.Position(
                        pos.get_x()+1, pos.get_y()+1))
                except:
                    type_rigth = ""
                #verify move to diagonal left  
                if type_left == "_":
                        possibility.append("move left")
                elif type_left == "white":
                        possibility.append("eat left")
                #verify move to diagonal rigth
                if type_rigth == "_":
                        possibility.append("move rigth")
                elif type_rigth == "white":
                        possibility.append("eat rigth")
            return possibility      
        else:
            #in construction
            pass
    #Return type of piece of pos(x,y) 
    def get_type_of_pos(self,_pos):
        return self.board.get_pos(_pos).get_type()
    #Return type of piece of x,y 
    def get_type_of_pos_XY(self,_x,_y):
        return self.board.get_pos_XY(_x,_y).get_type()
    #Draw board game based in type and pos of piece matrix 
    def print_board(self):
        _board = self.board.get_board()
        print("-"+"-"*4*self.col_size)
        for line in range(len(_board)):
            for col in range(len(_board[line])):
                if col == 0:
                    print("|",end="")
                _type = _board[line][col].get_type() 
                if _type == "white":
                    print("_"+u"\u25CF"+"_", end="|")
                elif _type == "black":
                    print("_"+u"\u25CB"+"_", end="|")  
                else:
                    print("_"+_type,end="|")
            print("")
        print("-"+"-"*4*self.col_size)

