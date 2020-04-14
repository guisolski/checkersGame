from piece import Piece 
from board import Board 
from position import Position 

#Class define one board of cheacker and verify moviments possible
class Checker():
    #---------------------------------------------------------------------------
    #Contructor of class
    #---------------------------------------------------------------------------
    def __init__(self): 
        #length of board
        #-----------------
        self.line_size = 10
        self.col_size = 10
        #------------------
        #math conversion more easy, * -1
        #--------------------------------------------
        self.conversion = {"white" : 1, "black" : -1}
        #--------------------------------------------
        #inicialize board
        #-----------------------------------
        self.board = self.inicialize_board()
        #-----------------------------------
    #---------------------------------------------------------------------------   
    #Inicialize piece in board
    #---------------------------------------------------------------------------
    def inicialize_board(self):
        p = Piece()
        board = Board(p,self.line_size,self.col_size)
        for line in range(self.line_size):
            for col in range(self.col_size):
                pos = Position(col,line)
                if (line == 0 or line == 2) and col%2 != 0:
                    board.set_piece(Piece("black",pos))
                elif (line == 1 or line == 3) and col%2 == 0:
                    board.set_piece(Piece("black",pos))
                elif (line == 9 or line == 7) and col%2 == 0:
                    board.set_piece(Piece("white",pos))
                elif (line == 8 or line == 6) and col%2 != 0:
                    board.set_piece(Piece("white",pos))
                else:
                    board.set_piece(Piece("blank",pos))
        return board
    #---------------------------------------------------------------------------
    #move piece based in positions
    #---------------------------------------------------------------------------
    def move(self,pos_before,pos_after):
        #Get piece in pos changing
        obj_in_pos_before = self.board.get_pos(pos_before)
        obj_in_pos_after  = self.board.get_pos(pos_after)
        #Set new pos in piece
        obj_in_pos_before.pos = pos_after
        obj_in_pos_after.pos = pos_before
        #Changing piece of places
        self.board.set_value_pos(obj_in_pos_after,pos_before)
        self.board.set_value_pos(obj_in_pos_before,pos_after)
    #---------------------------------------------------------------------------
    #checks if the received piece eats any enemy pieces diagonally
    #---------------------------------------------------------------------------
    def verify_diagonal_eating(self,_piece):
        pos = _piece.pos
        _type = self.conversion[_piece.type] * -1
        blank = "blank"
        return_eat = []
        #---------------------------------------------------------------
        #one horizantal direction (-y)
        #---------------------------------------------------------------
        if self.get_type_of_pos(Position(pos.x+1, pos.y-1)) == _type:
            if self.get_type_of_pos(Position(pos.x+2, pos.y-2)) == blank:
                return_eat.append(Position(pos.x+2, pos.y-2))
        if self.get_type_of_pos(Position(pos.x-1, pos.y-1)) == _type:
            if self.get_type_of_pos(Position(pos.x-2, pos.y-2)) == blank:
                return_eat.append(Position(pos.x-2, pos.y-2))
        #---------------------------------------------------------------
        #one horizantal direction (+y)
        #---------------------------------------------------------------
        if self.get_type_of_pos(Position(pos.x+1, pos.y+1)) == _type:
            if self.get_type_of_pos(Position(pos.x+2, pos.y+2)) == blank:
                return_eat.append(Position(pos.x+2, pos.y+1))
        if self.get_type_of_pos(Position(pos.x-1, pos.y+1)) == _type:
            if self.get_type_of_pos(Position(pos.x-2, pos.y+2)) == blank:
                return_eat.append(Position(pos.x-2, pos.y+1))
        #---------------------------------------------------------------                 
        return return_eat
    #---------------------------------------------------------------------------
    #checks if the stride piece moves on any diagonal
    #---------------------------------------------------------------------------
    def verify_diagonal_move(self,_piece):
        pos = _piece.pos
        blank = "blank"
        return_move = []
        if _piece.type == "white" or _piece.lady == True:
            #------------------------------------------------------------
            #one horizantal direction (-y)
            #------------------------------------------------------------
            if self.get_type_of_pos(Position(pos.x+1, pos.y-1)) == blank:
                return_move.append(Position(pos.x+1, pos.y-1))
            if self.get_type_of_pos(Position(pos.x-1, pos.y-1)) == blank:
                return_move.append(Position(pos.x-1, pos.y-1))
            #------------------------------------------------------------
        if _piece.type == "black" or _piece.lady == True:
            #------------------------------------------------------------
            #one horizantal direction (+y)
            #------------------------------------------------------------
            if self.get_type_of_pos(Position(pos.x+1, pos.y+1)) == blank:
                return_move.append(Position(pos.x+1, pos.y+1))
            if self.get_type_of_pos(Position(pos.x-1, pos.y+1)) == blank:
                return_move.append(Position(pos.x-1, pos.y+1))
            #------------------------------------------------------------
        return return_move
    #---------------------------------------------------------------------------
    #very all piece by past type
    #---------------------------------------------------------------------------
    def verify_any_piece_eating(self,_type):
        _board = self.board.board
        pieces_eating = {}
        for line in range(len(_board)):
            for col in range(len(_board[line])):
                piece = _board[line][col]
                eating = self.verify_diagonal_eating(piece)
                if len(eating) > 0: 
                    pieces_eating[piece] = eating
    #---------------------------------------------------------------------------
    #set one piece in board
    #---------------------------------------------------------------------------
    def set_piece(self,_piece):
        self.board.set_piece(_piece)
    #---------------------------------------------------------------------------            
    #return piece of pos(x,y)
    #---------------------------------------------------------------------------
    def get_piece(self,_pos):
        return self.board.get_pos(_pos)
    #---------------------------------------------------------------------------    
    #Return type of piece of pos(x,y) 
    #---------------------------------------------------------------------------
    def get_type_of_pos(self,_pos):
        return self.board.get_pos(_pos).type
    #---------------------------------------------------------------------------
    #Return type of piece of x,y 
    #---------------------------------------------------------------------------
    def get_type_of_pos_XY(self,_x,_y):
        return self.board.get_pos_XY(_x,_y).type
    #---------------------------------------------------------------------------
    #Draw board game based in type and pos of piece matrix 
    #---------------------------------------------------------------------------
    def print_board(self):
        _board = self.board.board
        print("-"+"-"*4*self.col_size)
        for line in range(len(_board)):
            for col in range(len(_board[line])):
                if col == 0:
                    print("|",end="")
                _type = _board[line][col].type
                if _type == "white":
                    print("_"+u"\u25CF"+"_", end="|")
                elif _type == "black":
                    print("_"+u"\u25CB"+"_", end="|")  
                elif _type == "blank":
                    print("_"+"__",end="|")
                else:
                    print(_type,end="|")

            print("")
        print("-"+"-"*4*self.col_size)
    #---------------------------------------------------------------------------