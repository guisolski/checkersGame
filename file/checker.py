#-------------------------------------------------------------------------------
#Import all function and class use in cheacker
#-------------------------------------------------------------------------------
from piece import Piece 
from board import Board 
from position import Position 
#-------------------------------------------------------------------------------
#Class define one board of cheacker and verify moviments possible
#-------------------------------------------------------------------------------
class Checker():
    #---------------------------------------------------------------------------
    #Contructor of class
    #---------------------------------------------------------------------------
    def __init__(self): 
        #-----------------
        #length of board
        #-----------------
        self.line_size = 10
        self.col_size = 10
        #------------------
        #math conversion more easy, * -1
        #--------------------------------------------
        self.conversion = {"white" : 1, "black" : -1}
        self.white_piece,self.black_piece =[],[]
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
                if (((line == 0 or line == 2) and col%2 != 0)
                    or
                    ((line == 1 or line == 3) and col%2 == 0)
                    ):
                    piece = Piece("black",pos)
                    board.set_piece(piece)
                    self.black_piece.append(piece)
                elif (((line == 9 or line == 7) and col%2 == 0)
                    or
                    ((line == 8 or line == 6) and col%2 != 0)
                    ):
                    piece =  Piece("white",pos)
                    board.set_piece(piece)
                    self.white_piece.append(piece)
                else:
                    board.set_piece(Piece("blank",pos))
        return board
    #---------------------------------------------------------------------------
    #Change places of pieces
    #---------------------------------------------------------------------------
    def move(self,before,after):
        #Set new pos in piece
        before.pos,after.pos = after.pos , before.pos
        #Changing piece of places
        self.board.set_piece(before)
        self.board.set_piece(after)
        if before.type == "white":
            if after.pos.y == 0:
                before.lady = True
        else:
            if after.pos.y == 9:
                before.lady = True

    #---------------------------------------------------------------------------
    #checks if the received piece eats any enemy pieces diagonally
    #---------------------------------------------------------------------------
    def verify_diagonal_eating(self,_piece):
        if _piece.type != "blank":
            pos = _piece.pos        
            _type = self.conversion[_piece.type] * -1
            print()
            blank = "blank"
            return_eat = []
            #---------------------------------------------------------------
            #one horizantal direction (-y)
            #---------------------------------------------------------------
            try:
                pos_after = Position(pos.x+1, pos.y-1)
                _int_type = self.conversion[self.get_type_of_pos(pos_after)]
                if _int_type == _type:
                    if pos_after.x +1 <= self.col_size:
                        pos_after.x = pos_after.x +1
                    else:
                        pos_after.x = pos_after.x -1
                    pos_after.y = pos_after.y -1
                    if self.get_type_of_pos(pos_after) == blank:
                        return_eat.append(pos_after)
            except:
                pass
            
            try:
                pos_after = Position(pos.x-1, pos.y-1)
                _int_type = self.conversion[self.get_type_of_pos(pos_after)]
                if _int_type == _type:
                    if pos_after.x -1 >= 0:
                        pos_after.x = pos_after.x -1
                    else:
                        pos_after.x = pos_after.x +1
                    pos_after.y = pos_after.y -1
                    if self.get_type_of_pos(pos_after) == blank:
                        return_eat.append(pos_after)
            except:
                pass
            #---------------------------------------------------------------
            #one horizantal direction (+y)
            #---------------------------------------------------------------
            try:
                pos_after = Position(pos.x+1, pos.y+1)
                _int_type = self.conversion[self.get_type_of_pos(pos_after)]
                if _int_type == _type:
                    if pos_after.x +1 <= self.col_size:
                        pos_after.x = pos_after.x +1
                    else:
                        pos_after.x = pos_after.x -1
                    pos_after.y = pos_after.y +1
                    if self.get_type_of_pos(pos_after) == blank:
                        return_eat.append(pos_after)
            except:
                pass
            try:
                pos_after = Position(pos.x-1, pos.y+1)
                _int_type = self.conversion[self.get_type_of_pos(pos_after)]
                if _int_type == _type:
                    if pos_after.x -1 >= 0:
                        pos_after.x = pos_after.x -1
                    else:
                        pos_after.x = pos_after.x +1
                    pos_after.y = pos_after.y +1
                    if self.get_type_of_pos(pos_after) == blank:
                        return_eat.append(pos_after)
            except:
                pass
            #---------------------------------------------------------------                 
            return self.pos_to_piece(return_eat)
        return None
    #---------------------------------------------------------------------------
    #Conver list of position to list of piece
    #---------------------------------------------------------------------------
    def pos_to_piece(self, _list):
        pieces = []
        for i in _list:
            pieces.append(self.get_piece(i))
        return pieces
    #---------------------------------------------------------------------------
    def recursion_lady(self,_list,_pos,_diagonal):
        _list.append(self.get_piece(_pos))
        _pos.x += _diagonal[0]
        _pos.y += _diagonal[1]
        if _pos.x >= 0 and _pos.x < self.col_size: 
            if _pos.y >=0 and _pos.y < self.line_size-1:
                _pos._print()
                _type_pos = self.get_type_of_pos(_pos)
                if _type_pos == "blank":
                    self.recursion_lady(_list,_pos,_diagonal)
        return _list
    #---------------------------------------------------------------------------
    def lady_move(self,_move,_diagonal):
        _return = []
        for i in range(len(_move)):
            _return.append(self.recursion_lady([],_move[i],_diagonal[i]))
        return _return 
    #---------------------------------------------------------------------------
    #checks if the stride piece moves on any diagonal
    #---------------------------------------------------------------------------
    def verify_diagonal_move(self,_piece):
        pos = _piece.pos
        blank = "blank"
        move = []
        _diagonal = []
        if _piece.type == "white" or _piece.lady == True:
            #------------------------------------------------------------
            #one horizantal direction (-y)
            #------------------------------------------------------------
            try:
                pos_after = Position(pos.x+1, pos.y-1)
                if self.get_type_of_pos(pos_after) == blank:
                    move.append(pos_after)
                    _diagonal.append([1,-1])
            except: pass
            try:
                pos_after = Position(pos.x-1, pos.y-1)
                if self.get_type_of_pos(pos_after) == blank:
                    move.append(pos_after)
                    _diagonal.append([-1,-1])
            except: pass
            #------------------------------------------------------------
        if _piece.type == "black" or _piece.lady == True:
            #------------------------------------------------------------
            #one horizantal direction (+y)
            #------------------------------------------------------------
            try:
                pos_after = Position(pos.x+1, pos.y+1)
                if self.get_type_of_pos(pos_after) == blank:
                    move.append(pos_after)
                    _diagonal.append([1,1])
            except: pass
            try:
                pos_after = Position(pos.x-1, pos.y+1)
                if self.get_type_of_pos(pos_after) == blank:
                    move.append(pos_after)
                    _diagonal.append([-1,+1])
            except: pass
            #------------------------------------------------------------
        if _piece.lady == True:
            return self.lady_move(move,_diagonal)
        return self.pos_to_piece(move)
    #---------------------------------------------------------------------------
    #very all piece by past type
    #---------------------------------------------------------------------------
    def verify_any_piece_eating(self,_type):
        pieces_eating = {}
        for y in range(self.line_size):
            for x in range(self.col_size):
                piece = self.get_piece(Position(x,y))
                if piece.type == _type:
                    eating = self.verify_diagonal_eating(piece)
                    if eating != None: 
                        if len(eating) > 0:
                            pieces_eating[piece] =  eating
        return pieces_eating
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
        print("-"+"-"*8*self.col_size)
        for line in range(len(_board)):
            for col in range(len(_board[line])):
                if col == 0:
                    print("|",end="")
                _type = _board[line][col].type
                if _type == "white":
                    print("___"+u"\u25CF"+"___", end="|")
                elif _type == "black":
                    print("___"+u"\u25CB"+"___", end="|")  
                elif _type == "blank":
                    print("_______",end="|")
                else:
                    print(_type,end="|")

            print("")
        print("-"+"-"*8*self.col_size)
    #---------------------------------------------------------------------------


