from Move import Move 
class Player:
    
    def __init__(self, color, board):
        self.move = Move()
        self.color = color
        self.board = board
        
    def askMove(self,otherPlayer):
        self.move.makeMove(self.color, self.board)
        otherPlayer.askMove(self)
        

        

    