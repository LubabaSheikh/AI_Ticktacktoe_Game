board = [" ", " ", " ",
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
    else:
        print("Position " + str(position) + " is occupied!")
        position = input("Enter new position: ")
        # Then recursively call insert_letter with letter and new position
        insert_letter_s(position, letter)


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
    insert_letter_m(pos, "o")

def player2_move():
    pos = int(input("Player 2 enter position: "))
    insert_letter_m(pos, "x")

def computer_move():
    pos = int(input("Enter position for 'x': "))
    insert_letter_s(pos, "x")

def player_move_s():
    pos = int(input("Player enter position for 'o': "))
    insert_letter_s(pos, "o")


def main():
    mode = input("Type 's' for Singleplayer and 'm' for Multiplayer: ")
    if (mode == "s"):
        print("Player is 'o'")
        print("Computer is 'x'")
        print_num_board()
        while(check_win != True):
            player_move_s()
            computer_move()
    if (mode == "m"):
        print("Player 1 is 'o'")
        print("Player 2 is 'x'")
        print_num_board()
        while(check_win != True):
            player1_move()
            player2_move()

main()