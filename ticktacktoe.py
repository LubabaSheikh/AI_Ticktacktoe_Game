board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

test_board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]


def print_num_board():
    print ("1" + "|" + "2" + "|" + "3")
    print("_ _ _ ")
    print ("4"+ "|" + "5" + "|" + "6")
    print("_ _ _ ")
    print ("7" + "|" + "8" + "|" + "9")



def print_board(bo):
    print (bo[0] + "|" + bo[1] + "|" + bo[2])
    print("_ _ _ ")
    print (bo[3] + "|" + bo[4] + "|" + bo[5])
    print("_ _ _ ")
    print (bo[6] + "|" + bo[7] + "|" + bo[8])

def empty_spot(position):
    if board[position-1] == " ":
        return True
    else:
        return False

def insert_letter_m(position, letter):
    if empty_spot(position) == True:
        board[position-1] = letter
        print_board(board)

        # After inserting letter, you check for win, lose or draw!
        if check_draw() == True:
            print("Draw!")
            exit()
        if check_win(letter) == True:
            if letter == "x":
                print("Player 2 is the Winner!")
                exit()
            else:
                print("Player 1 is the Winner!")
                exit()
    else:
        print("Position " + str(position) + " is occupied!")
        position = int(input("Enter new position: "))
        # Then recursively call insert_letter with letter and new position
        insert_letter_m(position, letter)


def insert_letter_s(position, letter):
    if empty_spot(position) == True:
        board[position-1] = letter
        print_board(board)

        # After inserting letter, you check for win, lose or draw!
        if check_draw() == True:
            print("Draw!")
            exit()
        if check_win(letter) == True:
            if letter == "x":
                print("Computer wins!")
                exit()
            else:
                print("You win!")
                exit()

def insert_letter_c(position, letter):
    if empty_spot(position) == True:
        board[position-1] = letter
        print("Computer entered x at position " + str(position))
        print_board(board)

        # After inserting letter, you check for win, lose or draw!
        if check_draw() == True:
            print("Draw!")
            exit()
        if check_win(letter) == True:
            if letter == "x":
                print("Computer wins!")
                exit()
            else:
                print("You win!")
                exit()


def check_draw():
    for row in range(9):
        if board[row] == " ":
            return False
    return True

def check_win(letter):
    if board[0] == letter and board[1] == letter and board[2] == letter: 
        return True
    if board[3] == letter and board[4] == letter and board[5] == letter: 
        return True
    if board[6] == letter and board[7] == letter and board[8] == letter: 
        return True

    if board[0] == letter and board[3] == letter and board[6] == letter: 
        return True
    if board[1] == letter and board[4] == letter and board[7] == letter: 
        return True
    if board[2] == letter and board[5] == letter and board[8] == letter: 
        return True

    if board[0] == letter and board[4] == letter and board[8] == letter: 
        return True
    if board[2] == letter and board[4] == letter and board[6] == letter: 
        return True

    return False


def player1_move():
    pos = int(input("Player 1 enter position: "))
    insert_letter_m(pos, "x")

def player2_move():
    pos = int(input("Player 2 enter position: "))
    insert_letter_m(pos, "o")


# x is AI
# o is player
def computer_move():
    bestScore = -100  ## doesnt matter what it is cause it will change after we find best score
    bestMove = 0  ## this will hold the position that is best for the computer to play
    test_board = board

    for row in range(9):
        if (test_board[row] == " "):
            test_board[row] = "x" # Place x in one possible place

            score = minimax(test_board, False) # check the score/ outcome when you place x in this particular position above
            # Here the isMaximizing variable is False because when minimax is called, its going to go to the else statement first cause it is o's turn to pick after we have placed an x in the board above

            test_board[row] = " "  # set this back to blank so the for_loop can iterate through all the possible positions of x in this board

            # Now check if the score is greater than bestScore because if score is greater then that means the position related to this score is the best so 
            # bestMove should be the position related to this score which is the variable row in this case
            if (score > bestScore):
                bestScore = score  # set bestScore equal to score so that the next score of the new position can be compared with this bestScore
                bestMove = row

    # Now the bestMove has been determined so now place x on the bestMove position (play computer's move)
    insert_letter_c(bestMove+1, "x") # send bestMove+1 to inser_letter_s() because insert_letter_s() does position+1 so we need to calibrate row to fit that




# Score 1: AI Wins
# Score -1: Player wins
# Score 0: Draw
def minimax(current_board, isMaximizing):

# We need to check if anyone won after a letter was placed to test play this game before actually applying minimax again to the new current_board recursively occuring
    if (check_win("x")):  # check if computer won
        return 1  # return 1 if AI won to let computer_move() know that this is a good position

    elif (check_win("o")): # check is player won
        return -1  # return -1 if player won to let computer_move() know that this is a bad position

    elif (check_draw()): # check if draw
        return 0  # return 0 if draw to let computer_move() know that this is a neutral position


     # If we are maximizing then we want highest score
    if (isMaximizing):
        # Then we just do what is in computer_move() but we just want to return the score, we dont need bestMove cause we want to play the move in computer_move()
        bestScore = -100  # Still need bestScore to check if the new score is better when minimaxis recursively called and return the bestScore
        for row in range(9):
            if (current_board[row] == " "):
                current_board[row] = "x" # Place x in one possible place

                score = minimax(current_board, False) # check the score/ outcome when you place x in this particular position above
                # Here the isMaximizing variable is False because 

                current_board[row] = " "  # set this back to blank so the for_loop can iterate through all the possible positions of x in this board

                # Now check if the score is greater than bestScore because if score is greater then that means the position related to this score is the best so 
                # bestMove should be the position related to this score which is the variable row in this case
                if (score > bestScore):
                    bestScore = score  # set bestScore equal to score so that the next score of the new position can be compared with this bestScore
        
        # Now return the bestScore after loop is over
        return bestScore

    # If we are are not maximizing we are minimizing
    else:
        bestScore = 100  # is positive because here we need the lowest score cause we are minimizing which is compared down below
        for row in range(9):
            if (current_board[row] == " "):
                current_board[row] = "o" # Place o in one possible place cause we are minimizing

                score = minimax(current_board, True) # check the score/ outcome when you place o in this particular position above
                # Here the isMaximizing variable is True because now it is x's turn to decide and pick the position

                current_board[row] = " "  # set this back to blank so the for_loop can iterate through all the possible positions of o in this board

                # Now check if the score is less than bestScore because if score is less then that means the position related to this score is the best for o so 
                # bestScore should be the new score
                if (score < bestScore):
                    bestScore = score  
        
        # Now return the bestScore after loop is over
        return bestScore

## So in minimax() function the True and False just play with each other to figure out what is the best move for the computer


    

def player_move_s():
    pos = int(input("Player enter position for 'o': "))
    insert_letter_s(pos, "o")


def main():
    mode = input("Type 's' for Singleplayer and 'm' for Multiplayer: ")
    if (mode == "s"):
        print("Player is 'o'")
        print("Computer is 'x'")
        print_num_board()
        while(check_win("x") != True or check_win("o") != True):
            player_move_s()
            computer_move()
            
    if (mode == "m"):
        print("Player 1 is 'o'")
        print("Player 2 is 'x'")
        print_num_board()
        while(check_win("x") != True or check_win("o") != True):
            player1_move()
            player2_move()

main()