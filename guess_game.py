import random


game_state = True
random_number = random.randint(1,10)

def play_game():
    if game_state:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == random_number:
            win()
        elif guess < random_number:
            print("Too low, try again!")
            play_game()
        elif guess > random_number:
            print("Too high, try again!")
            play_game()

def win():
    print("You guessed it! You won!")
    repeat = input("Do you want to keep playing? ")
    if repeat[0].lower() == 'y':
        play_game()
    elif repeat[0].lower() == 'n':
        print("Thanks for playing. Bye!")
        game_state = False

play_game()





	
	