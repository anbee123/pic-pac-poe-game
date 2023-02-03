# How to play 

# display welcome message
# render empty board
# Decide who moves first X or O 
# player X takes a turn 
# check for a winner - func 
# player O takes a turn - func
# check for winner
# after win - display winner - func
# if no winner - display tie - func


# potential state
# whose turn it is - x/o
# winner - true/false

# create a start func: 
# game.takeTurn()
# game.checkforWin()
# game.diplayWin()

class PyPacPoe():
  def __init__(self):
    self.current_player = "X"
    self.player_selection = ""
    self.game_over = False
    self.turns = 0
    self.current_board = {'a1': " ", 
                          'b1': " ", 
                          'c1': " ",
                          'a2': " ", 
                          'b2': " ", 
                          'c2': " ",
                          'a3': " ", 
                          'b3': " ", 
                          'c3': " ",
                         }

    self.winning_lists = [
      ['a1','b1','c1'],
      ['a2','b2','c2'],
      ['a3','b3','c3'],
      ['a1','a2','a3'],
      ['b1','b2','b3'],
      ['c1','c2','c3'],
      ['a1','b2','c3'],
      ['a3','b2','c1']
    ]
                     