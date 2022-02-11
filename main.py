import random
 
 
def guess_number_input(valid_numbers):
    guess_number_raw = input("Guess the number: ")
    if guess_number_raw.isnumeric():
        guess_number = int(guess_number_raw)
        if guess_number in valid_numbers:
            return guess_number
        else:
            print("your guess number isn't in valid numbers, please try again!")
            return -1
    else:
        print("wrong number, please try again!")
        return -1
 
 
def guess_game(turn_total):
    valid_numbers = [_ for _ in range(0, 11)]
    number_game_master = random.choice(valid_numbers)
     
    turn_counter = 0
    while turn_counter < turn_total:
        guess_number_player = guess_number_input(valid_numbers)
        if guess_number_player == -1:
            print("retry guess the number")
        elif number_game_master == guess_number_player:
            print(f"Hurray!!! You guessed the number right, it's {guess_number_player}")
            break
        else:
            print("Sorry! Your guess number is incorrect")
            turn_counter += 1
    else:
        print(f"All your guess number is incorrect, the number of game master is {number_game_master}")

 
 def suggest_number(guess_number_player, number_game_master):
    if guess_number_player < number_game_master:
        print("Your guess number is less than my number")
    else:
        print("Your guess number is great than my number")

if __name__ == "main":
    guess_game()
        
