#game board function
board = {'1': ' ', '2': ' ', '3': ' ',
   '4': ' ', '5': ' ', '6': ' ',
   '7': ' ', '8': ' ', '9': ' '}
board_blank = {'1': ' ', '2': ' ', '3': ' ',
'4': ' ', '5': ' ', '6': ' ',
'7': ' ', '8': ' ', '9': ' '}

#the game
def game():
  #start game function
  player1 = input("Enter player one's name: ")
  player2 = input("Enter player two's name: ")
  print(player1 + ", your piece is X. " + player2 + ", your piece is O.")
  print("\nPlayers will take turns placing their pieces on the board. When it is your turn, select a number between 1 and 9 to move. The board below shows where your piece will appear depending on the number you choose. The first player to get 3 of their pieces in a row wins!")
  print("\nOkay, let's begin!")

  #setting key variable
  turn = player1
  piece = 'X'
  count = 0

  #entering turns
  while True:
    print_board(board)
    move = input(turn + ", where do you want to move? Enter a square number from 1 to 9.")
    if move in board:
      if board[move] == " ":
        board[move] = piece
        count += 1
      else:
        print("That square is already filled. Please choose an empty square: ")
        continue
    else:
      print("That was an invalid input. Please enter another square number from 1 to 9.")
      continue

    #check for winner
    if count >= 5:
        if board["7"] == board["8"] == board["9"] != " ": #across the top
            declare_winner(turn, piece)
            break
        elif board["4"] == board["5"] == board["6"] != " ":  #across the middle
            declare_winner(turn, piece)
            break
        elif board["1"] == board["2"] == board["3"] != " ":  #across the bottom
            declare_winner(turn, piece)
            break
        elif board["1"] == board["4"] == board["7"] != " ":  #down the left
            declare_winner(turn, piece)
            break
        elif board["2"] == board["5"] == board["8"] != " ":  #down the middle
            declare_winner(turn, piece)
            break
        elif board["3"] == board["6"] == board["9"] != " ":  #down the right
            declare_winner(turn, piece)
            break
        elif board["7"] == board["5"] == board["3"] != " ":  #diagonal
            declare_winner(turn, piece)
            break
        elif board["1"] == board["5"] == board["9"] != " ":  #diagonal
            declare_winner(turn, piece)
            break
    if count == 9:
      print("It's a tie!")
      break
    if piece == "X":
      piece = "O"
      turn = player2
    else:
      piece = "X"
      turn = player1
def print_board(board):
  print(board["1"] + "|" + board["2"] + "|" + board["3"])
  print("-+-+-")
  print(board["4"] + "|" + board["5"] + "|" + board["6"])
  print("-+-+-")
  print(board["7"] + "|" + board["8"] + "|" + board["9"])

#declaring winner
def declare_winner(turn, piece):
  print_board(board)
  print("\n GAME OVER \n")
  if piece == "X":
    print(turn + "wins! Congratulations!")
  else:
    print(turn + "wins! Congratulations!")

game()

restart = input("Do you want to play again? (y/n) ")
if restart == "y" or restart == "Y":
    board = board_blank
    game()
else:
    print("Thanks for playing!")