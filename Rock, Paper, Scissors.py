import random 

print("Rock, Paper, Scissors")
print()
print("ULTIMATE EDITION")
print()
mode = input("""Which mode do you want to play?
1. Human vs Human
2. Human vs Computer
:""")
if mode == "2":
  # list of possible moves
  moves = ["rock", "paper", "scissors"]

  # get player's move
  player_move = input("What is your move? (rock, paper, scissors): ").lower()

  # check if player's move is valid
  if player_move not in moves:
    print("Invalid move. Please choose rock, paper, or scissors.")
  else:
    computer_move = random.choice(moves)
    print("Computer chose " + computer_move)

# determine the winner
  if player_move == computer_move:
    print("It's a tie!")
  elif player_move == "rock" and computer_move == "scissors":
    print("You win!")
  elif player_move == "paper" and computer_move == "rock":
    print("You win!")
  elif player_move == "scissors" and computer_move == "paper":
    print("You win!")
  else:
    print("Computer wins.")
if mode == "1":
  print("Select your move R, P or S")
  print()
  player1Move = input("Player 1 > ") 
  print()
  player2Move = input("Player 2 > ")
  if player1Move=="R":
    if player2Move=="R":
      print("You both picked Rock,draw!")
    elif player2Move=="S":
      print("Player1 smashed Player2's Scissors into dust with their Rock!")
    elif player2Move=="P":
      print("Player1's Rock is destroyed by Player2's Paper!")
    else:
      print("Invalid Move Player 2!")
  elif player1Move=="P":
    if player2Move=="R":
      print("Player2's Rock is destroyed by Player1's Paper!")
    elif player2Move=="S":
      print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
    elif player2Move=="P":
      print("Two bits of paper flap at each other. Dissapointing. Draw.")
    else:
      print("Invalid Move Player 2!")
  elif player1Move=="S":
    if player2Move=="R":
      print("Player 2's Rock makes metal-dust out of Player1's Scissors")
    elif player2Move=="S":
      print("Ka-Shing! Scissors bounce off each other like a sword fight! Draw.")
    elif player2Move=="P":
      print("Player1's Scissors make confetti out of Player2's paper!")
    else:
      print("Invalid Move Player 2!")
  else:
    print("Invalid Move Player 1!")