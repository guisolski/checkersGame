class person():
    def __init__(self, *_args):
        #name is name of person
        #alive is amount piece alive of person
        #alive is amount piece dead of person
        self.name, self.alive, self.dead = 0,0,0
        if len(_args) == 3:
            self.name = _args[0]
            self.alive = _args[1]
            self.dead = _args[2]
    
