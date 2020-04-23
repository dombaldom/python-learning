# Tic, Tac, Toe play.
# 2020/04/23
# Author Domingo Balderas
import random

# Print the board of the play
def display_board(board):
    # Print 11 lines, the bord[0] keep the turn of the Player 'O' or 'X'
    controlCaracteres = 11
    # board keep the 9 options to choose plus the mark of first player
    temp = board[1:]
    temp.reverse()

    while controlCaracteres != 0:
        if controlCaracteres%2 != 0:
            print("     |     |     ")
        elif controlCaracteres%4 == 0:
            print("-----------------")
        else:
            print(f'  {temp.pop()}  |  {temp.pop()}  |  {temp.pop()}  ')
        controlCaracteres -= 1

# Player choose their market
def player_input():
    # Ask for the marker to play:
    marker1 = input("Player 1 chose a marker: 'X' or 'O': ").upper()

    # if type error
    while marker1 != 'X' and marker1 != 'O':
        marker1 = input("Just a marker: 'X' or 'O': ").upper()

    return marker1


# Receives board, marker choseen by user, and position of the turn, position was
def place_marker(board, marker, position):
    # Replace new position with marker
    board[position] = marker
    display_board(board)


# Check who is the winner
def win_check(mark, board):
    # there are 8 ways to win
    w1 = [1,2,3]
    w2 = [4,5,6]
    w3 = [7,8,9]
    w4 = [1,4,7]
    w5 = [2,5,8]
    w6 = [3,6,9]
    w7 = [1,5,9]
    w8 = [3,5,7]

    # compare each
    if board[w1[0]] + board[w1[1]] + board[w1[2]] == mark+mark+mark or  board[w2[0]] + board[w2[1]] + board[w2[2]] == mark+mark+mark  or board[w3[0]] + board[w3[1]] + board[w3[2]] == mark+mark+mark or board[w4[0]] + board[w4[1]] + board[w4[2]] == mark+mark+mark or board[w5[0]] + board[w5[1]] + board[w5[2]] == mark+mark+mark or board[w6[0]] + board[w6[1]] + board[w6[2]] == mark+mark+mark or board[w7[0]] + board[w7[1]] + board[w7[2]] == mark+mark+mark or board[w8[0]] + board[w8[1]] + board[w8[2]] == mark+mark+mark:
        return True        
    else:
        return False

# Choose the player who has the first turn to play
def choose_first():
    return random.randint(1,2)

# If the position in the board is free return true
def is_free_position(board, position):
    return board[position] == ' '

# If the board is full return true 
def full_board_check(board):
    full = ' ' not in board
    if full:
        print('The game is drow!!!!!!!')
        return True

# Ask the player to choose a position to play
def player_choice(board):
    print(f'It is your turn Player {board[0]}')
    new_position = int(input('Insert your next position (1,9): '))
    # check the number in 1 to 9
    while new_position not in range(1,10):
        new_position = int(input('just insert (1,9): '))
    
    #check if there is a free position, if there is change into int and return the new position
    while not is_free_position(board, new_position):
        new_position = int(input('this postition is not available chosse position (1,9): '))
        # check again if the number in 1 to 9
        while new_position not in range(1,10):
            new_position = int(input('just insert (1,9): '))
    return new_position

# just ask for the replay
def replay():
    play = input("Are you ready to play enter yes or not?:").upper()

    # check a right enter
    while play != 'NOT' and play != 'YES':
        play = input("Just write yes or not:").upper()
    if play == 'YES':
        return True
    else:
        return False


#### Main function
def start():
    print('Welcome to Tic Tac Toe!')
    # ask to the player if want to choose 'X' or 'O' to play
    mark = player_input()
    print(f'Player 1 chossed {mark} ')
    # ask who would play first
    player = choose_first()
    print(f'Player {player} will go first')
    # Select mark for the first player
    if player != 1:
        if mark == 'X':
            mark = 'O'
        else:
            mark = 'X'

    while replay():
        # Reset the board, mark for the first player keep
        board = [mark, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        display_board(board)

        while not full_board_check(board):
            # select the new position
            new_position = player_choice(board)
            # set the new position
            place_marker(board, board[0], new_position)
            
            # check if someone win in the last turn
            if win_check(board[0], board):
                print(f'{board[0]} Won!!!!!!')
                break

            # Change marker of next player
            if board[0] == 'X':
                board[0] = 'O'
            else:
                board[0] = 'X'
# let's Go!
start()

