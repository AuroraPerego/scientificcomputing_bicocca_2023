'''
Q7: tic-tac-toe

### Your task

Using the functions defined above,
  * `initialize_board()`
  * `show_board()`
  * `get_move()`

fill in the function `play_game()` below to complete the game, 
asking for the moves one at a time, alternating between player 1 and 2
'''

class TicTacToe:
    def __init__(self):
        self.board = """
 {s1:^3} | {s2:^3} | {s3:^3}
-----+-----+-----
 {s4:^3} | {s5:^3} | {s6:^3}
-----+-----+-----      123
 {s7:^3} | {s8:^3} | {s9:^3}       456
                       789  
"""
        self.play = {}

    def initialize_board(self):
        for n in range(9):
            self.play["s{}".format(n+1)] = ""

    def show_board(self):
        """ display the playing board.  We take a dictionary with the current state of the board
        We rely on the board string to be a global variable"""
        print(self.board.format(**self.play))

    def get_move(self, n):
        """ ask the current player, n, to make a move -- make sure the square was not 
            already played.  xo is a string of the character (x or o) we will place in
            the desired square """
        valid_move = False
        while not valid_move:
            idx = input("player {}, enter your move (1-9)".format(n))
            if self.play["s{}".format(idx)] == "":
                valid_move = True
            else:
                print("invalid: {}".format(self.play["s{}".format(idx)]))

        xo = "x" if n==1 else "o"            
        self.play["s{}".format(idx)] = xo

    def play_game(self):
        """ play a game of tic-tac-toe """

        nturns = 0
        self.initialize_board()
        self.show_board()
        nex = -0.5
        while not ((self.play['s1']==self.play['s2']==self.play['s3'] and self.play['s1']!="") or
                   (self.play['s4']==self.play['s5']==self.play['s6'] and self.play['s4']!="") or
                   (self.play['s7']==self.play['s8']==self.play['s9'] and self.play['s7']!="") or
                   (self.play['s1']==self.play['s4']==self.play['s7'] and self.play['s1']!="") or
                   (self.play['s2']==self.play['s5']==self.play['s8'] and self.play['s2']!="") or
                   (self.play['s3']==self.play['s6']==self.play['s9'] and self.play['s3']!="") or
                   (self.play['s1']==self.play['s5']==self.play['s9'] and self.play['s1']!="") or
                   (self.play['s3']==self.play['s5']==self.play['s7'] and self.play['s3']!="")):
            nturns += 1
            if nturns == 10:
                print("No one won :(")
                return
            self.get_move(int(1.5+nex))
            nex *= -1
            self.show_board()
        print("The winner is player", int(1.5-nex), "!")
        return

game = TicTacToe()
game.play_game()
