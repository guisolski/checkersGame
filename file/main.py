import checker
import util
import position
import start_variables
if __name__ == "__main__":
    type_of_player, turn, loop, game = start_variables.start()
    game.print_board()
    while loop:
        #human trun play
        if turn == "human":
            before = util.input_split_validation_type("input position of piece (x,y):",",",position.Position)
            after  = util.input_split_validation_type("input position to go (x,y):",",",position.Position)
        #machine player
        else:
            pass
        
        
        util.clear()
        game.print_board()