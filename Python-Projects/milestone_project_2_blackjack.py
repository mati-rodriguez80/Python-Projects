'''MILESTONE PROYECT 2 - BLACKJACK'''

# Import section
import random
import os

# Outside global variables
suits = ('Hearts','Diamonds','Clubs','Spades')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,
          'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

# Class definitions
class Card:
    '''Class that defines the characteristics of a card like its rank, suit, or value.'''

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
        
    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
    def __format__(self,format_spec):         # Learn more about this PEP 3101
        return format(str(self),format_spec)

    def set_ace(self,number):
        '''Specific method for Blackjack game which allows the player set the Ace value according to their convenience.'''
        self.value = number

class Deck:
    '''Class that generates a new deck which is french for Blackjack. Here shuffle, deal, and return cards methods are defined.'''

    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(rank,suit))
    
    def shuffle_deck(self):
        '''Method that shuffle the created deck.'''
        random.shuffle(self.all_cards)
    
    # Deal cards from the top
    def deal_one(self):
        '''Method that permits deal cards from the top of the deck.'''
        return self.all_cards.pop(0)
    
    # Return cards to the bottom
    def return_cards(self,new_cards):
        '''Method that permits returning cards to the deck for both alone or multiple cards.'''
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

class Player:
    '''Class dedicated to create instances of the different players. As attributes, they can have name and a bankroll.'''

    def __init__(self,name,bankroll):
        self.name = name
        self.bankroll = bankroll

# Functions definitions
def clear():
    '''Just a function used to clear the output displayed.'''

    os.system('cls')

def welcome_message():
    '''Function that gives the player a welcome message and the instructions for this Blackjack version.'''
    
    print('''
                                 BLACKJACK GAME!

First of all,, thanks for playing at our Casino! Your visit is a pleasure for us!
                    In this Casino, Blackjack is paid 3 to 2.
               Also, dealer must stand on 17 and must draw to 16.

 For this text-based version of Blackjack, the player will be able to hit, stand
 double down, or split, and situations like push and blackjack are defined, too.
 It is also important to mention that only one 52 cards french deck is used here.

                    That's all!! Have fun and best of luck!!
          ''')

def board_game():
    '''Function that displays the board or table where the cards are going to be dealt.
       Furthermore, it shows the player information and the sum of the cards.
    '''

    clear()
    
    print(f'''
               BLACKJACK PAYS 3 TO 2
     DEALER MUST STAND ON 17 AND MUST DRAW TO 16
MOVES: Hit(H) - Stand(S) - Doble Down (DD) - Split(SP)

                        DEALER
=======================================================
|{dealer_hand[0]:^53}|   Dealer hand = {dealer_hand_result}''')
    
    if not player_turn:
        print(f'|{dealer_hand[1]:^53}|')
    else:
        print('|                  <Card face down>                   |')

    print(f'''|{dealer_hand[2]:^53}|
|{dealer_hand[3]:^53}|
|{dealer_hand[4]:^53}|
|                                                     |
|                                                     |
|{player_hand[4]:^53}|
|{player_hand[3]:^53}|
|{player_hand[2]:^53}|
|{player_hand[1]:^53}|
|{player_hand[0]:^53}|   Player hand = {player_hand_result}
=======================================================
 PLAYER: {player_one.name}
 BANKROLL: {player_one.bankroll}
 BET: {bet}
           ''')

def board_game_split():
    '''Function that displays the board or table where the cards are going to be dealt when the player decides to split.
       Furthermore, it shows the player information and the sum of the cards.
    '''

    clear()
    
    print(f'''
               BLACKJACK PAYS 3 TO 2
     DEALER MUST STAND ON 17 AND MUST DRAW TO 16
MOVES: Hit(H) - Stand(S) - Doble Down (DD) - Split(SP)

                        DEALER
=======================================================
|{dealer_hand[0]:^53}|   Dealer hand = {dealer_hand_result}''')
    
    if not player_turn:
        print(f'|{dealer_hand[1]:^53}|')
    else:
        print('|                  <Card face down>                   |')

    print(f'''|{dealer_hand[2]:^53}|
|{dealer_hand[3]:^53}|
|{dealer_hand[4]:^53}|
|                                                     |
|                                                     |
|{player_hand_1[4]:^26}{player_hand_2[4]:^26} |
|{player_hand_1[3]:^26}{player_hand_2[3]:^26} |
|{player_hand_1[2]:^26}{player_hand_2[2]:^26} |
|{player_hand_1[1]:^26}{player_hand_2[1]:^26} |   Player hand: 1 = {player_hand_result_1}
|{player_hand_1[0]:^26}{player_hand_2[0]:^26} |   Player hand: 2 = {player_hand_result_2}
=======================================================
 PLAYER: {player_one.name}
 BANKROLL: {player_one.bankroll}
 BET: {bet}
           ''')

def bets():
    '''Function that ask you to pick a chip. Then, it checks if the chosen chip is available, and if you have enough money.'''
    
    print("Chips available: 5 - 25 - 50 - 100 - 500 - 2500")
    
    while True:
        try:
            money = int(input('Place your bets: '))
        except ValueError:
            print("Error: Please choose some of the chips available.")
            continue
        else:
            if money not in [5,25,50,100,500,2500]:
                print("You did not enter an available chip value. Please try again.")
                continue
            elif money > player_one.bankroll:
                print("Sorry but you don't have enough money in your bankroll. Please choose another chip.")
                continue
            else:
                player_one.bankroll -= money
                print("Bet accepted.")
                break
    
    return money

def moves(num_cards_player):
    '''Function that returns which will be your next move while you are playing.
       It takes in the number of cards the player have in that moment.
    '''
    
    while True:

        # This function in this version doesn't take account of split. So, it's neccesary that the function
        # takes in whether split is True or False in order to allow the player only hit or stand when split.
        if num_cards_player == 2:
            move = input("Which will be your next move? ").lower()
            
            if move not in ['h','s','dd','sp']:
                print("That's not a posible move. Please try again.")
                continue
            else:
                break
        elif num_cards_player >= 3:
            move = input("Which will be your next move? ").lower()
            
            if move in ['dd','sp']:
                print("You can only hit or stand at this point of the game. Please try again.")
                continue
            elif move not in ['h','s']:
                print("That's not a posible move. Please try again.")
                continue
            else:
                break
        else:
            print('Error. Please try again.')
            break
    
    return move

def player_info():
    '''Function that asks the player their name and bankroll.'''
    
    name = input("Please enter your name: ")
    
    while True:
        try:
            bankroll = float(input("How much money do you have for play? "))
        except ValueError:
            print("Error: That's not a posible value. Please try again.")
            continue
        else:
            print("Perfect!")
            break
    
    return (name,bankroll)

def sum_hand(cards_list,num_cards):
    '''Function that takes in the player or dealer hand, and the number of cards they have in that moment.
       Then, it returns the sum of the values of their cards.
    '''
    
    result = 0
    
    for i in range(num_cards):
        result += cards_list[i].value
    
    return result

def ace_check(cards_list,num_cards):
    '''Function that takes in the player or dealer hand, and the number of cards they have in that moment.
       Then, it asks the player to decide which value is going to consider for the Ace/s they have in their hand.
    '''
    
    for i in range(num_cards):
        if cards_list[i].rank == 'Ace':
            while True:
                ace_value = input("What value do you want for the Ace? 1 or 11? ")
                if ace_value not in ['1','11']:
                    print("Error: That's not a posible value. Please try again.")
                    continue
                else:
                    cards_list[i].set_ace(int(ace_value))
                    break
        else:
            pass

def replay(num_cards_player,num_cards_dealer):
    '''Function that asks the player if they want to continue playing or not after a round. It returns True or False.
       If the player answer is Y (Yes) and still have enough money to continue,
       the function returns the cards on the table to the deck.
    '''

    answer = 'wrong'

    while answer not in ['y','n']:

        answer = input('Do you want to continue playing (Y - N)? ').lower()

        if answer == 'y':
            if player_one.bankroll >= 5:
                print('Next round!')
                print(f'Number of cards in the deck before returning cards: {len(new_deck.all_cards)}')
                new_deck.return_cards(player_hand[:num_cards_player])
                new_deck.return_cards(dealer_hand[:num_cards_dealer])
                print(f'Number of cards in the deck after returning cards: {len(new_deck.all_cards)}')
                return True
            else:
                print("Sorry but you can't continue since you don't have enough money in your bankroll.")
                print('Thank you for playing in our Casino! We hope you enjoyed it!')
                return False
        elif answer == 'n':
            print('Thank you for playing in our Casino! We hope you enjoyed it!')
            return False
        else:
            print("That's not a posible answer. Please enter 'Y' (Yes) or 'N' (No).")

def replay_split(num_1_cards_player,num_2_cards_player,num_cards_dealer):
    '''Function that asks the player if they want to continue playing or not after a split round. It returns True or False.
       If the player answer is Y (Yes) and still have enough money to continue,
       the function returns the cards on the table to the deck.
    '''

    answer = 'wrong'

    while answer not in ['y','n']:

        answer = input('Do you want to continue playing (Y - N)? ').lower()

        if answer == 'y':
            if player_one.bankroll >= 5:
                print('Next round!')
                print(f'Number of cards in the deck before returning cards: {len(new_deck.all_cards)}')
                new_deck.return_cards(player_hand_1[:num_1_cards_player])
                new_deck.return_cards(player_hand_2[:num_2_cards_player])
                new_deck.return_cards(dealer_hand[:num_cards_dealer])
                print(f'Number of cards in the deck after returning cards: {len(new_deck.all_cards)}')
                return True
            else:
                print("Sorry but you can't continue since you don't have enough money in your bankroll.")
                print('Thank you for playing in our Casino! We hope you enjoyed it!')
                return False
        elif answer == 'n':
            print('Thank you for playing in our Casino! We hope you enjoyed it!')
            return False
        else:
            print("That's not a posible answer. Please enter 'Y' (Yes) or 'N' (No).")

# Main body - Game logic
welcome_message()

player_name,player_bankroll = player_info()
player_one = Player(player_name,player_bankroll)

new_deck = Deck()
new_deck.shuffle_deck()

input("Please press the enter key to start the game!")

game_on = True

while game_on:
    
    player_turn = True # The player goes first
    split = False # It's going to be True when the player decides to split their hand
    blackjack_1 = False # It's going to be True when split is the case and the player has Blackjack with one of their hands
    blackjack_2 = False # It's going to be True when split is the case and the player has Blackjack with one of their hands
    double_blackjack = False # It's going to be True when split is the case and the player has Blackjack with their both hands
    double_bust = False # It's going to be True when split is the case and the player gets bust with their both hands
    # These two variables next are going to store the sum (an integer) of both the dealer and the player's cards
    # At first, they are an empty string only for showing purposes in the board
    player_hand_result = ' '
    dealer_hand_result = ' '
    
    bet = bets()
    
    # Players can only have up to five cards in their hand
    player_hand = [' ',' ',' ',' ',' ']
    dealer_hand = [' ',' ',' ',' ',' ']
    
    for x in range(2):
        player_hand[x] = new_deck.deal_one()
        dealer_hand[x] = new_deck.deal_one()
    
    # count_player_cards stores how many cards have the player
    count_player_cards = 2
    board_game()
    ace_check(player_hand,count_player_cards)
    player_hand_result = sum_hand(player_hand,count_player_cards)
    board_game()
    # Check for Blackjack
    if player_hand_result == 21:
        print('Blackjack for the player!')
        input("Please press the enter key to continue")
        player_turn = False  # Dealer turn
        board_game()
        ace_check(dealer_hand,2)
        dealer_hand_result = sum_hand(dealer_hand,2)
        board_game()

        if dealer_hand_result == 21:
            player_one.bankroll += bet
            board_game()
            print('Blackjack for the dealer! This is a Push!')
            game_on = replay(count_player_cards,2)
            continue
        else:
            player_one.bankroll += bet*(2.5)
            board_game()
            print('The player win!')
            game_on = replay(count_player_cards,2)
            continue
    
    # Player turn
    while player_turn:
        
        while count_player_cards <= 5:
            player_move = moves(count_player_cards)
            # Hit
            if player_move == 'h' and count_player_cards <= 4:
                player_hand[count_player_cards] = new_deck.deal_one()
                count_player_cards += 1
                board_game()
                ace_check(player_hand,count_player_cards)
                player_hand_result = sum_hand(player_hand,count_player_cards)
                board_game()
                if player_hand_result > 21:
                    print('Bust! The player lose!')
                    game_on = replay(count_player_cards,2)
                    player_turn = False
                    break
                else:
                    pass
            elif player_move == 'h' and count_player_cards == 5:
                print("You have 5 cards already. You can only stand at this point of the game.")
                player_turn = False
                break
            # Stand
            elif player_move == 's':
                player_turn = False
                break
            # Double Down
            elif player_move == 'dd':
                # The game has already taken the bet from the player's bankroll, so it's only necessary to check
                # whether the game can again take the same amount of money or not from the player's bankroll
                if bet > player_one.bankroll:
                    print("Sorry but you don't have enough money in your bankroll. Please choose another move.")
                    continue
                else:
                    player_one.bankroll -= bet
                    bet += bet
                    player_hand[count_player_cards] = new_deck.deal_one() # 3 cards
                    count_player_cards += 1
                    board_game()
                    ace_check(player_hand,count_player_cards)
                    player_hand_result = sum_hand(player_hand,count_player_cards)
                    board_game()
                    if player_hand_result > 21:
                        print('Bust! The player lose!')
                        game_on = replay(count_player_cards,2)
                        player_turn = False
                        break
                    else:
                        player_turn = False
                        break
            # Split
            elif player_move == 'sp':
                if player_hand[0].value == player_hand[1].value:
                    if bet > player_one.bankroll:
                        print("Sorry but you don't have enough money in your bankroll. Please choose another move.")
                        continue
                    else:
                        split = True # Variable that is used in the dealer turn
                        player_one.bankroll -= bet
                        bet += bet
                        # From this point, now everything is going to be doubled
                        player_hand_result_1 = ' '
                        player_hand_result_2 = ' '
                        player_hand_1 = [' ',' ',' ',' ',' ']
                        player_hand_2 = [' ',' ',' ',' ',' ']
                        # Two cards for both hands. First, split those which been in the original hand. Then, two new cards from the deck
                        player_hand_1[0] = player_hand[0]
                        player_hand_2[0] = player_hand[1]
                        player_hand_1[1] = new_deck.deal_one()
                        player_hand_2[1] = new_deck.deal_one()

                        count_player_cards_1 = count_player_cards
                        count_player_cards_2 = count_player_cards
                        board_game_split()
                        ace_check(player_hand_1,count_player_cards_1)
                        ace_check(player_hand_2,count_player_cards_2)
                        player_hand_result_1 = sum_hand(player_hand_1,count_player_cards_1)
                        player_hand_result_2 = sum_hand(player_hand_2,count_player_cards_2)
                        board_game_split()
                        # Check for Blackjack
                        if player_hand_result_1 == 21 and player_hand_result_2 == 21:
                            double_blackjack = True
                            print('Blackjack for the player with both hands!')
                            input("Please press the enter key to continue")
                            player_turn = False  # Dealer turn
                            board_game_split()
                            ace_check(dealer_hand,2)
                            dealer_hand_result = sum_hand(dealer_hand,2)
                            board_game_split()

                            if dealer_hand_result == 21:
                                player_one.bankroll += bet
                                board_game_split()
                                print('Blackjack for the dealer! This is a Push!')
                                game_on = replay_split(count_player_cards_1,count_player_cards_2,2)
                                break
                            else:
                                player_one.bankroll += bet*(2.5)
                                board_game_split()
                                print('The player win!')
                                game_on = replay_split(count_player_cards_1,count_player_cards_2,2)
                                player_turn = False
                                break
                        elif player_hand_result_1 == 21:
                            blackjack_1 = True
                            print('Blackjack for the player with the first hand!')
                            input("Please press the enter key to continue")

                            while count_player_cards_2 <= 5:
                                player_move = moves(count_player_cards_2)
                                # Hit
                                if player_move == 'h' and count_player_cards_2 <= 4:
                                    player_hand_2[count_player_cards_2] = new_deck.deal_one()
                                    count_player_cards_2 += 1
                                    board_game_split()
                                    ace_check(player_hand_2,count_player_cards_2)
                                    player_hand_result_2 = sum_hand(player_hand_2,count_player_cards_2)
                                    board_game_split()
                                    if player_hand_result_2 > 21:
                                        bet -= bet/2
                                        board_game_split()
                                        print('Bust! The player lose with the second hand!')
                                        player_turn = False
                                        break
                                    else:
                                        pass
                                elif player_move == 'h' and count_player_cards_2 == 5:
                                    print("You have 5 cards already. You can only stand at this point of the game.")
                                    player_turn = False
                                    break
                                # Stand
                                elif player_move == 's':
                                    player_turn = False
                                    break
                        elif player_hand_result_2 == 21:
                            blackjack_2 = True
                            print('Blackjack for the player with the second hand!')
                            input("Please press the enter key to continue")

                            while count_player_cards_1 <= 5:
                                player_move = moves(count_player_cards_1)
                                # Hit
                                if player_move == 'h' and count_player_cards_1 <= 4:
                                    player_hand_1[count_player_cards_1] = new_deck.deal_one()
                                    count_player_cards_1 += 1
                                    board_game_split()
                                    ace_check(player_hand_1,count_player_cards_1)
                                    player_hand_result_1 = sum_hand(player_hand_1,count_player_cards_1)
                                    board_game_split()
                                    if player_hand_result_1 > 21:
                                        bet -= bet/2
                                        board_game_split()
                                        print('Bust! The player lose with the first hand!')
                                        player_turn = False
                                        break
                                    else:
                                        pass
                                elif player_move == 'h' and count_player_cards_1 == 5:
                                    print("You have 5 cards already. You can only stand at this point of the game.")
                                    player_turn = False
                                    break
                                # Stand
                                elif player_move == 's':
                                    player_turn = False
                                    break
                        # Regular game
                        if blackjack_1 or blackjack_2:
                            break
                        else:
                            # First hand
                            while count_player_cards_1 <= 5:
                                player_move = moves(count_player_cards_1)
                                # Hit
                                if player_move == 'h' and count_player_cards_1 <= 4:
                                    player_hand_1[count_player_cards_1] = new_deck.deal_one()
                                    count_player_cards_1 += 1
                                    board_game_split()
                                    ace_check(player_hand_1,count_player_cards_1)
                                    player_hand_result_1 = sum_hand(player_hand_1,count_player_cards_1)
                                    board_game_split()
                                    if player_hand_result_1 > 21:
                                        bet -= bet/2
                                        board_game_split()
                                        print('Bust! The player lose with the first hand!')
                                        break
                                    else:
                                        pass
                                elif player_move == 'h' and count_player_cards_1 == 5:
                                    print("You have 5 cards already. You can only stand at this point of the game.")
                                    break
                                # Stand
                                elif player_move == 's':
                                    break
                            # Second hand
                            while count_player_cards_2 <= 5:
                                player_move = moves(count_player_cards_2)
                                # Hit
                                if player_move == 'h' and count_player_cards_2 <= 4:
                                    player_hand_2[count_player_cards_2] = new_deck.deal_one()
                                    count_player_cards_2 += 1
                                    board_game_split()
                                    ace_check(player_hand_2,count_player_cards_2)
                                    player_hand_result_2 = sum_hand(player_hand_2,count_player_cards_2)
                                    board_game_split()
                                    if player_hand_result_2 > 21:
                                        if player_hand_result_1 > 21:
                                            double_bust = True
                                            print('Bust! The player lose with the second hand!')
                                            game_on = replay_split(count_player_cards_1,count_player_cards_2,2)
                                            count_player_cards = 6 # This is only to break the while loop at the beginning
                                            player_turn = False
                                            break
                                        else:
                                            bet -= bet/2
                                            board_game_split()
                                            print('Bust! The player lose with the second hand!')
                                            count_player_cards = 6 # This is only to break the while loop at the beginning
                                            player_turn = False
                                            break
                                    else:
                                        pass
                                elif player_move == 'h' and count_player_cards_2 == 5:
                                    print("You have 5 cards already. You can only stand at this point of the game.")
                                    count_player_cards = 6 # This is only to break the while loop at the beginning
                                    player_turn = False
                                    break
                                # Stand
                                elif player_move == 's':
                                    count_player_cards = 6 # This is only to break the while loop at the beginning
                                    player_turn = False
                                    break
                else:
                    print("You can't split since your cards don't have the same value. Please choose another move.")
                    continue
    
    if game_on == False:
        break
    
    # Dealer turn
    if split == False:

        while not player_turn and player_hand_result <= 21:
            
            input("Please press the enter key to continue")
            # At this point, now the board is going to show the second card of the dealer
            # count_dealer_cards stores how many cards have the dealer
            count_dealer_cards = 2
            board_game()
            ace_check(dealer_hand,count_dealer_cards)
            dealer_hand_result = sum_hand(dealer_hand,count_dealer_cards)
            board_game()
            
            if dealer_hand_result >= 17:
                if player_hand_result > dealer_hand_result:
                    player_one.bankroll += bet*2
                    board_game()
                    print('The player win!')
                    game_on = replay(count_player_cards,count_dealer_cards)
                    break
                elif player_hand_result < dealer_hand_result:
                    print('The dealer win!')
                    game_on = replay(count_player_cards,count_dealer_cards)
                    break
                else:
                    player_one.bankroll += bet
                    board_game()
                    print('This is a push!')
                    game_on = replay(count_player_cards,count_dealer_cards)
                    break
            else:
                while count_dealer_cards <= 4:
                    dealer_hand[count_dealer_cards] = new_deck.deal_one()
                    count_dealer_cards += 1
                    input("Please press the enter key to continue")
                    board_game()
                    ace_check(dealer_hand,count_dealer_cards)
                    dealer_hand_result = sum_hand(dealer_hand,count_dealer_cards)
                    board_game()
                    if dealer_hand_result > 21:
                        player_one.bankroll += bet*2
                        board_game()
                        print('Bust! The dealer lose!')
                        game_on = replay(count_player_cards,count_dealer_cards)
                        player_turn = True
                        break
                    elif dealer_hand_result >= 17:
                        if player_hand_result > dealer_hand_result:
                            player_one.bankroll += bet*2
                            board_game()
                            print('The player win!')
                            game_on = replay(count_player_cards,count_dealer_cards)
                            player_turn = True
                            break
                        elif player_hand_result < dealer_hand_result:
                            print('The dealer win!')
                            game_on = replay(count_player_cards,count_dealer_cards)
                            player_turn = True
                            break
                        else:
                            player_one.bankroll += bet
                            board_game()
                            print('This is a push!')
                            game_on = replay(count_player_cards,count_dealer_cards)
                            player_turn = True
                            break
                    else:
                        pass
    else:
        while not player_turn and double_blackjack == False and double_bust == False:
            
            input("Please press the enter key to continue")
            # At this point, now the board is going to show the second card of the dealer
            # count_dealer_cards stores how many cards have the dealer
            count_dealer_cards = 2
            board_game_split()
            ace_check(dealer_hand,count_dealer_cards)
            dealer_hand_result = sum_hand(dealer_hand,count_dealer_cards)
            board_game_split()
            
            if dealer_hand_result >= 17:
                board_game_split()
                input("Please press the enter key to continue")
                break
            else:
                while count_dealer_cards <= 4:
                    dealer_hand[count_dealer_cards] = new_deck.deal_one()
                    count_dealer_cards += 1
                    input("Please press the enter key to continue")
                    board_game_split()
                    ace_check(dealer_hand,count_dealer_cards)
                    dealer_hand_result = sum_hand(dealer_hand,count_dealer_cards)
                    board_game_split()
                    if dealer_hand_result > 21:
                        board_game_split()
                        print("Bust! The dealer lose!")
                        input("Please press the enter key to continue")
                        player_turn = True
                        break
                    elif dealer_hand_result >= 17:
                        board_game_split()
                        input("Please press the enter key to continue")
                        player_turn = True
                        break
                    else:
                        pass

        if double_blackjack == False and double_bust == False:
            player_turn = False
            if blackjack_1:
                if player_hand_result_2 > 21:
                    # First hand
                    if player_hand_result_1 == dealer_hand_result:
                        player_one.bankroll += bet
                        board_game_split()
                        print("This is a push with player's first hand!")
                        game_on = replay_split(count_player_cards_1,count_player_cards_2,count_dealer_cards)
                    else:
                        player_one.bankroll += bet*(2.5)
                        board_game_split()
                        print('The player win with the first hand!')
                        game_on = replay_split(count_player_cards_1,count_player_cards_2,count_dealer_cards)
                else:
                    # First hand
                    if player_hand_result_1 == dealer_hand_result:
                        player_one.bankroll += bet/2
                        board_game_split()
                        print("This is a push with player's first hand!")
                    else:
                        player_one.bankroll += (bet/2)*(2.5)
                        board_game_split()
                        print('The player win with the first hand!')
                    # Second hand
                    if dealer_hand_result <= 21:
                        if player_hand_result_2 > dealer_hand_result:
                            player_one.bankroll += (bet/2)*2
                            board_game_split()
                            print('The player win with the second hand!')
                            game_on = replay_split(count_player_cards_1,count_player_cards_2,count_dealer_cards)
                        elif player_hand_result_2 < dealer_hand_result:
                            print("The dealer win against the player's second hand!")
                            game_on = replay_split(count_player_cards_1,count_player_cards_2,count_dealer_cards)
                        else:
                            player_one.bankroll += bet/2
                            board_game_split()
                            print("This is a push with player's second hand!")
                            game_on = replay_split(count_player_cards_1,count_player_cards_2,count_dealer_cards)
                    else:
                        player_one.bankroll += (bet/2)*2
                        board_game_split()
                        print('The player win with the second hand!')
                        game_on = replay_split(count_player_cards_1,count_player_cards_2,count_dealer_cards)

            elif blackjack_2:
                if player_hand_result_1 > 21:
                    # Second hand
                    if player_hand_result_2 == dealer_hand_result:
                        player_one.bankroll += bet
                        board_game_split()
                        print("This is a push with player's second hand!")
                        game_on = replay_split(count_player_cards_1,count_player_cards_2,count_dealer_cards)
                    else:
                        player_one.bankroll += bet*(2.5)
                        board_game_split()
                        print('The player win with the second hand!')
                        game_on = replay_split(count_player_cards_1,count_player_cards_2,count_dealer_cards)
                else:
                    # Second hand
                    if player_hand_result_2 == dealer_hand_result:
                        player_one.bankroll += bet/2
                        board_game_split()
                        print("This is a push with player's second hand!")
                    else:
                        player_one.bankroll += (bet/2)*(2.5)
                        board_game_split()
                        print('The player win with the second hand!')
                    # First hand
                    if dealer_hand_result <= 21:
                        if player_hand_result_1 > dealer_hand_result:
                            player_one.bankroll += (bet/2)*2
                            board_game_split()
                            print('The player win with the first hand!')
                            game_on = replay_split(count_player_cards_1,count_player_cards_2,count_dealer_cards)
                        elif player_hand_result_1 < dealer_hand_result:
                            print("The dealer win against the player's first hand!")
                            game_on = replay_split(count_player_cards_1,count_player_cards_2,count_dealer_cards)
                        else:
                            player_one.bankroll += bet/2
                            board_game_split()
                            print("This is a push with player's first hand!")
                            game_on = replay_split(count_player_cards_1,count_player_cards_2,count_dealer_cards)
                    else:
                        player_one.bankroll += (bet/2)*2
                        board_game_split()
                        print('The player win with the first hand!')
                        game_on = replay_split(count_player_cards_1,count_player_cards_2,count_dealer_cards)

            elif player_hand_result_1 <= 21 and player_hand_result_2 <= 21:

                if dealer_hand_result <= 21:
                    # First hand
                    if player_hand_result_1 > dealer_hand_result:
                        player_one.bankroll += (bet/2)*2
                        board_game_split()
                        print('The player win with the first hand!')
                        input("Please press the enter key to continue")
                    elif player_hand_result_1 < dealer_hand_result:
                        print("The dealer win against the player's first hand!")
                        input("Please press the enter key to continue")
                    else:
                        player_one.bankroll += bet/2
                        board_game_split()
                        print("This is a push with player's first hand!")
                        input("Please press the enter key to continue")
                       
                    # Second hand
                    if player_hand_result_2 > dealer_hand_result:
                        player_one.bankroll += (bet/2)*2
                        board_game_split()
                        print('The player win with the second hand!')
                        game_on = replay_split(count_player_cards_1,count_player_cards_2,count_dealer_cards)
                    elif player_hand_result_2 < dealer_hand_result:
                        print("The dealer win against the player's second hand!")
                        game_on = replay_split(count_player_cards_1,count_player_cards_2,count_dealer_cards)
                    else:
                        player_one.bankroll += bet/2
                        board_game_split()
                        print("This is a push with player's second hand!")
                        game_on = replay_split(count_player_cards_1,count_player_cards_2,count_dealer_cards)
                else:
                    player_one.bankroll += bet*2
                    board_game_split()
                    print('The player win with both hands!')
                    game_on = replay_split(count_player_cards_1,count_player_cards_2,count_dealer_cards)

            elif player_hand_result_1 <= 21 and player_hand_result_2 > 21:

                if dealer_hand_result <= 21:
                    # First hand
                    if player_hand_result_1 > dealer_hand_result:
                        player_one.bankroll += bet*2
                        board_game_split()
                        print('The player win with the first hand!')
                        game_on = replay_split(count_player_cards_1,count_player_cards_2,count_dealer_cards)
                    elif player_hand_result_1 < dealer_hand_result:
                        print("The dealer win against the player's first hand!")
                        game_on = replay_split(count_player_cards_1,count_player_cards_2,count_dealer_cards)
                    else:
                        player_one.bankroll += bet
                        board_game_split()
                        print("This is a push with player's first hand!")
                        game_on = replay_split(count_player_cards_1,count_player_cards_2,count_dealer_cards)
                else:
                    player_one.bankroll += bet*2
                    board_game_split()
                    print('The player win with the first hand!')
                    game_on = replay_split(count_player_cards_1,count_player_cards_2,count_dealer_cards)

            elif player_hand_result_1 > 21 and player_hand_result_2 <= 21:

                if dealer_hand_result <= 21:
                    # Second hand
                    if player_hand_result_2 > dealer_hand_result:
                        player_one.bankroll += bet*2
                        board_game_split()
                        print('The player win with the second hand!')
                        game_on = replay_split(count_player_cards_1,count_player_cards_2,count_dealer_cards)
                    elif player_hand_result_2 < dealer_hand_result:
                        print("The dealer win against the player's second hand!")
                        game_on = replay_split(count_player_cards_1,count_player_cards_2,count_dealer_cards)
                    else:
                        player_one.bankroll += bet
                        board_game_split()
                        print("This is a push with player's second hand!")
                        game_on = replay_split(count_player_cards_1,count_player_cards_2,count_dealer_cards)
                else:
                    player_one.bankroll += bet*2
                    board_game_split()
                    print('The player win with the second hand!')
                    game_on = replay_split(count_player_cards_1,count_player_cards_2,count_dealer_cards)
        else:
            pass
