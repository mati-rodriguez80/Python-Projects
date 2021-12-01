'''MILESTONE PROYECT 1: TIC TAC TOE GAME'''

import os

def clear():
    '''
    Just a function used to clear the output displayed
    '''

    os.system('cls')

# Outside global variables
marks = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def welcome_message():
    '''
    Give to the player a welcome message and tell them how to play.
    '''    
    
    print('Welcome to Tic Tac Toe Game!')
    print('This is a 2 players game where we will find out who wins more times after several Epic rounds!')
    print('Once the game starts, the players are going to take turns automatically between each match.')
    print("To control where you want your mark, you have to use the computer's number pad, that is:\n")
    print('    7    |    8    |    9    ')
    print('-----------------------------')
    print('    4    |    5    |    6    ')
    print('-----------------------------')
    print('    1    |    2    |    3    ')
    print("\nThat's all! Best of luck and Have Fun!")

def symbol_choice():
    '''
    The players decide who is going to be 'X' and 'O', and who goes first.
    '''
        
    symbol1 = 'wrong'
    
    while symbol1 not in ['X','x','O','o']:
        
        symbol1 = input('Who goes first? X or O? ')
        
        if symbol1 not in ['X','x','O','o']:
            clear()
            print("I couldn't understand what you have written. Please enter 'X' or 'O'.")
    
    return symbol1.upper()

def board_game(marks):
    '''
    The main function here is only show the board and keep it updated.
    '''
        
    clear()
    
    print('Tic Tac Toe Game!\n')
    print('         |         |         ')
    print(f'{marks[6]:^9}|{marks[7]:^9}|{marks[8]:^9}')
    print('         |         |         ')
    print('-----------------------------')
    print('         |         |         ')
    print(f'{marks[3]:^9}|{marks[4]:^9}|{marks[5]:^9}')
    print('         |         |         ')
    print('-----------------------------')
    print('         |         |         ')
    print(f'{marks[0]:^9}|{marks[1]:^9}|{marks[2]:^9}')
    print('         |         |         ')

def mark_position(symbol2,marks):
    '''
    The main purpose of this function is to inform which player goes next, and update the board with the chosen mark.
    '''
    
    if symbol2 == 'X':
        print("It's 'X' turn!")
    elif symbol2 == 'O':
        print("It's 'O' turn!")    
    
    # I could've done it differently, but I wanted to emphasize that this is a game
    # where the player can only do one move, and then it's player 2 turn.
    turn = 1
    
    while turn == 1:

        move = input('Where do you want the mark (1-9)? ')
        
        # Here I validate that the players haven't chosen letters or other symbols,
        # and if the chosen position is inside the board (1-9)
        if move.isdigit() == False:
            print("That's not a number. Please enter somewhere in between 1 to 9.")
            continue
        elif int(move) not in range(1,10):
            print("That's not a valid position. Please enter somewhere in between 1 to 9.")
            continue
        
        # Here I validate that the chosen position hasn't been chosen before
        if marks[int(move)-1] == ' ':
            marks[int(move)-1] = symbol2
        else:
            print("There is already a mark in there. Please choose another position.")
            continue
            
        turn += 1

def winner_check(marks):
    '''
    This function evaluates if the match ended. In that case, it's going to return True if someone won. Otherwise,
    if there's a tie, it's going to return None.
    '''
    
    win = False
    
    if marks[0] == marks[1] and marks[1] == marks[2] and marks[0] != ' ':
        win = True
    elif marks[3] == marks[4] and marks[4] == marks[5] and marks[3] != ' ':
        win = True
    elif marks[6] == marks[7] and marks[7] == marks[8] and marks[6] != ' ':
        win = True
    elif marks[0] == marks[3] and marks[3] == marks[6] and marks[0] != ' ':
        win = True
    elif marks[1] == marks[4] and marks[4] == marks[7] and marks[1] != ' ':
        win = True
    elif marks[2] == marks[5] and marks[5] == marks[8] and marks[2] != ' ':
        win = True
    elif marks[2] == marks[4] and marks[4] == marks[6] and marks[2] != ' ':
        win = True
    elif marks[0] == marks[4] and marks[4] == marks[8] and marks[0] != ' ':
        win = True
    elif ' ' not in marks:
        win = None
        
    return win

def replay(winner,symbol3,marks):
    '''
    The main objective here is check whether the players want to continue playing or not, returning 'Y' or 'N'.
    Before that, it's going to show the final board game and the result in case the match has ended.
    '''
    
    continue_playing = 'wrong'
    
    if winner == True:
        
        board_game(marks)
        print(f"The {symbol3} player won! CONGRATS!")
        
        while continue_playing not in ['Y','y','N','n']:
            
            continue_playing = input('Do you want to continue playing (Y-N)? ')
            
            if continue_playing not in ['Y','y','N','n']:
                print("I'm sorry, I couldn't understand. Please enter 'Y' for Yes or 'N' for No.")
                
    elif winner == None:
        
        board_game(marks)
        print("This is a tie!")
        
        while continue_playing not in ['Y','y','N','n']:
            
            continue_playing = input('Do you want to continue playing (Y-N)? ')
            
            if continue_playing not in ['Y','y','N','n']:
                print("I'm sorry, I couldn't understand. Please enter 'Y' for Yes or 'N' for No.")
    
    return continue_playing.upper()

def matches_counter(winner,symbol4,winner_x_o_tie):
    '''
    The purpose here is update the list that is making a tally of each time the X player or O player win,
    or when there's a tie.
    '''
    
    if winner == True:
        
        if symbol4 == 'X':
            winner_x_o_tie[0] += 1
        elif symbol4 == 'O':
            winner_x_o_tie[1] += 1
    
    elif winner == None:
        
        winner_x_o_tie[2] += 1

def main_body_game(symbol5,marks):
    '''
    Here are almost every function created. The objective of this final function is generate the final logic
    in order to make the game works properly.
    '''
    
    # Initial values
    
    # Make a tally of turns in each match. It's not very useful, but lets grab if X or O start first.
    rounds = 1
    # Lets know which player started first and which one started in the last match in order to maintain
    # the alternation between the matches.
    track_symbol = None
    # This list make a tally of how many times each player won, and how many times there was a tie.
    # index[0] == Player X, index [1] == Player O, index[2] == Tie.
    winner_x_o_tie = [0,0,0]
    #The only goal for this value is to maintain the game on.
    game_on = True
    
    while game_on == True:
        
        # Store who goes first or who started in the last match
        if symbol5 == 'X' and rounds == 1:
            track_symbol = True
        elif symbol5 == 'O' and rounds == 1:
            track_symbol = False
        
        # Show the board
        board_game(marks)
        
        # Choose a position for the mark
        mark_position(symbol5,marks)
        
        # Check if the match ended
        winner = winner_check(marks)
        
        # Make statistics of the results of the matches
        matches_counter(winner,symbol5,winner_x_o_tie)
        
        # Inform the final result when the match ended and store if the players want to continue playing or not
        play_again = replay(winner,symbol5,marks)
        
        # Change the player turn to maintain the alternation while the match continues
        if symbol5 == 'X':
            symbol5 = 'O'
        elif symbol5 == 'O':
            symbol5 = 'X'
        
        # Count how many times the players have played in the current match
        rounds += 1
        
        # Continue the game or not based on the previous players decision
        if play_again == 'Y':            
            # Restart the board game
            marks = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
            # Guarantee the second player is going to start in the next match
            if track_symbol == True:
                symbol5 = 'O'
            elif track_symbol == False:
                symbol5 = 'X'
            # Restart this value in order to accomplish the previous statement
            rounds = 1
            
        elif play_again == 'N':
            print('\nFinal statistics:')
            print(f'The X player won {winner_x_o_tie[0]} times.')
            print(f'The O player won {winner_x_o_tie[1]} times.')
            print(f'There was a tie {winner_x_o_tie[2]} times.')
            print('\nThanks for playing! See you next time!')
            game_on = False

# Welcome message and instructions
welcome_message()

# Choice of mark for player 1
symbol = symbol_choice()

# Initialize the game
main_body_game(symbol,marks)
