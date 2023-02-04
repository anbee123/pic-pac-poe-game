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
    return
  #display a welcome message
  def display_welcome_message(self):
      print('''
      ---------------------
      Let's play Py-Pac-Poe
      ---------------------
            ''')   
  
  def display_board(self):
      print('''
          A   B   C

       1)   |   | 
        -----------
       2)   |   |  
        -----------
       3)   |   |   
       ''')

new_game = PyPacPoe()
new_game.display_welcome_message() 
new_game.display_board()     
