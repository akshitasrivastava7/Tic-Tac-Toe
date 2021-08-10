b = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
game_still_going = True
Curr = 'X'
winner = None


def display():
    print(b[0] + " | " + b[1] + " | " + b[2] + "    1 | 2 | 3  ")
    print(b[3] + " | " + b[4] + " | " + b[5] + "    4 | 5 | 6  ")
    print(b[6] + " | " + b[7] + " | " + b[8] + "    7 | 8 | 9  ")


def play():
    display()
    while game_still_going:
      handle(Curr)
      checki()
      flip()

    if winner=='X' or winner=="0":
      print(winner+" won")
    elif winner==None:
      print("TIE")



def handle(player):
  print("RIGHT NOW PLAYER  " + player +"  IS PLAYING")
  pos=input("ENTER WHERE YOU WANT TO LIVE \n")
  valid=False
  while not valid:
    # Make sure the input is valid
    while pos not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      pos = input("Choose a position from 1-9: ")

    pos=int(pos)-1
    # Then also make sure the spot is available on the board
    if b[pos] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")
  b[pos]=player
  display()

def checki():

    check_win()
    check_tie()





def check_win():
    # Set global variables
    global winner
    # Check if there was a winner anywhere
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    # Get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():
    # Set global variables
    global game_still_going
    # Check if any of the rows have all the same value (and is not empty)
    row_1 = b[0] == b[1] == b[2] != "-"
    row_2 = b[3] == b[4] == b[5] != "-"
    row_3 = b[6] == b[7] == b[8] != "-"
    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return the winner
    if row_1:
        return b[0]
    elif row_2:
        return b[3]
    elif row_3:
        return b[6]
    # Or return None if there was no winner
    else:
        return None


def check_columns():
    # Set global variables
    global game_still_going
    # Check if any of the rows have all the same value (and is not empty)
    col_1 = b[0] == b[3] == b[6] != "-"
    col_2 = b[1] == b[4] == b[7] != "-"
    col_3 = b[2] == b[5] == b[8] != "-"
    # If any row does have a match, flag that there is a win
    if col_1 or col_2 or col_3:
        game_still_going = False
    # Return the winner
    if col_1:
        return b[0]
    elif col_2:
        return b[1]
    elif col_3:
        return b[2]
    # Or return None if there was no winner
    else:
        return None


def check_diagonals():
    # Set global variables
    global game_still_going
    # Check if any of the rows have all the same value (and is not empty)
    di_1 = b[0] == b[4] == b[8] != "-"
    di_2 = b[2] == b[4] == b[6] != "-"
    
    # If any row does have a match, flag that there is a win
    if di_1 or di_2:
        game_still_going = False
    # Return the winner
    if di_1:
        return b[0]
    elif di_2:
        return b[2]
    # Or return None if there was no winner
    else:
        return None

def check_tie():
  global game_still_going
  if '-' not in b:
    game_still_going=False
    return True
  else:
    return False


def flip():
  global Curr
  if Curr=="X":
    Curr="0"
  else:
    Curr="X"

play()