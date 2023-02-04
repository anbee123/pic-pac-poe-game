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
    self.current_board = {
      "a1":None,
      "a2": None,
      "a3": None, 
      "b1": None,
      "b2": None,
      "b3": None,
      "c1": None,
      "c2": None,
      "c3": None
    }

  #display a welcome message
  def display_welcome_message(self):
      print('''
      ---------------------
      Let's play Py-Pac-Poe
      ---------------------
            ''')   
  
  def display_board(self):
      print(f'''
          A   B   C

       1) {self.current_board['a1']}  | {self.current_board['b1']}  | {self.current_board['c1']}
        -----------
       2) {self.current_board['a2']}  | {self.current_board['b2']}  | {self.current_board['c2']}
        -----------
       3) {self.current_board['a3']}  | {self.current_board['b3']}  | {self.current_board['c3']} 
       ''')
  def display_turn(self):
      print(f"Player {self.current_player} Move(exapmle B2):")

  def switch_player(self):
      if self.current_player == "X":
          self.current_player = "O" 
      else:
          self.current_player = "X" 


  def get_player_move(self):
      player_move = input("enter your move: ").lower()
      while not player_move in self.current_board:
        player_move = input("that's not a valid move, try again: ").lower()

      while self.current_board[player_move] != None:
        player_move = input("This space istaken, try again: ").lower()
        self.current_board[player_move] = self.current_player

  def check_for_win(self):
  

  def display_winner(self):
       print(f"Player {self.current_player} has won the game!")

  def display_tie(self):
       print("It was a tie game!")
    

    
      

new_game = PyPacPoe()
# new_game.display_welcome_message() 
# new_game.display_board()    
# new_game.display_turn() 
# new_game.get_player_move()
print(new_game.current_player)
new_game.switch_player()
