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

board = """
 {s1:^3} | {s2:^3} | {s3:^3}
-----+-----+-----
 {s4:^3} | {s5:^3} | {s6:^3}
-----+-----+-----      123
 {s7:^3} | {s8:^3} | {s9:^3}       456
                       789  
"""

def initialize_board(play):
    for n in range(9):
        play["s{}".format(n+1)] = ""

def show_board(play):
    """ display the playing board.  We take a dictionary with the current state of the board
    We rely on the board string to be a global variable"""
    print(board.format(**play))
    
def get_move(n, play):
    """ ask the current player, n, to make a move -- make sure the square was not 
        already played.  xo is a string of the character (x or o) we will place in
        the desired square """
    valid_move = False
    while not valid_move:
        idx = input("player {}, enter your move (1-9)".format(n))
        if play["s{}".format(idx)] == "":
            valid_move = True
        else:
            print("invalid: {}".format(play["s{}".format(idx)]))

    xo = "x" if n==1 else "o"            
    play["s{}".format(idx)] = xo

def play_game():
    """ play a game of tic-tac-toe """
    
    nturns = 0
    play ={}
    initialize_board(play)
    show_board(play)
    nex = -0.5
    while not ((play['s1']==play['s2']==play['s3'] and play['s1']!="") or
               (play['s4']==play['s5']==play['s6'] and play['s4']!="") or
               (play['s7']==play['s8']==play['s9'] and play['s7']!="") or
               (play['s1']==play['s4']==play['s7'] and play['s1']!="") or
               (play['s2']==play['s5']==play['s8'] and play['s2']!="") or
               (play['s3']==play['s6']==play['s9'] and play['s3']!="") or
               (play['s1']==play['s5']==play['s9'] and play['s1']!="") or
               (play['s3']==play['s5']==play['s7'] and play['s3']!="")):
      nturns += 1
      if nturns == 10:
        print("No one won :(")
        return
      get_move(int(1.5+nex), play)
      nex *= -1
      show_board(play)
    print("The winner is player", int(1.5-nex), "!")
    return

play_game()
