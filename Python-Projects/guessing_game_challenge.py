'''GUESSING GAME CHALLENGE'''

print("WELCOME TO THE GUESSING GAME CHALLENGE!")
print("There's a number out there between 1 and 100 and you have to find it as fast as possible!")
print("If in your first attempt your guess is more than 10 away from the number, I'll tell you you're COLD")
print("However, if your guess is within 10 of the number, I'll tell you you're WARM")
print("Then, if your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("And, if your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S FIND THAT NAUGHTY NUMBER!")

from random import randint

winner_num = randint(1,100)
player_num = 0
result_abs = 0
attempts = 0

while winner_num != player_num:
    if attempts == 0:
        player_num = float(input('Guess the secret number! It has to be a number between 1 and 100 (it does not have decimal point): '))
    else:
        player_num = float(input('Try Again! You can do it! '))
        
    if player_num < 1 or player_num > 100:
        print('OUT OF BOUNDS. Please remember it has to be a number between 1 and 100.')
        continue
    elif winner_num == player_num:
        if attempts == 0:
            print("You've guessed correctly on your first attempt!!! CONGRATS CRACK!!!")
            break
        else:
            attempts += 1
            print(f"You've guessed correctly after {attempts} times!!! CONGRATS!!!")
            break
    else:
        attempts += 1
        if attempts == 1:
            if abs(winner_num - player_num) <= 10:
                print('WARM!')
                result_abs = abs(winner_num - player_num)
                continue
            else:
                print('COLD!')
                result_abs = abs(winner_num - player_num)
                continue
        else:
            if abs(winner_num - player_num) <= result_abs:
                print('WARMER!')
                result_abs = abs(winner_num - player_num)
                continue
            else:
                print('COLDER!')
                result_abs = abs(winner_num - player_num)
                continue
