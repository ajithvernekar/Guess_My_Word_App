# Description:
# You are responsible for writing a program that plays a word guessing game with a user.
# Your program will provide a category of words to the user and a string of dashes “-----” that
# represent the length of the word. The user will guess the word and with each incorrect guess,
# your program will reveal a letter at random, “-a---”.
# Upon guessing the word correctly, your program will then inform the user how many guesses they took.

import random
print("Welcome to the Guess My Word App")

# Create a dictionary called game_dict that has a minimum of four keys.
game_dict = {"sports":['basketball', 'baseball', 'soccer', 'football',  'tennis', 'curling'],
             "colors":['orange', 'yellow', 'purple', 'aquamarine', 'violet', 'gold'],
             "fruits":['apple', 'banana', 'watermelon', 'peach', 'mango', 'strawberry'],
             "classes":['english', 'history', 'science', 'mathematics', 'art', 'health'],
             }

# Create a list called game_keys with all keys in game_dict.
game_keys = [key for key in game_dict]

# Create an active flag variable to control a while loop and set it to True.
play = True

#The main game loop
while(play):
        # Randomly pick a key from the list game_keys
        game_category = random.choice(game_keys)
        # Randomly pick a value from the dictionary that corresponds to that key
        game_word = random.choice(game_dict[game_category])
        blank_word = ["_"]*len(game_word)

        print("Guess a {} letter word from the following category: {}".format(len(game_word), game_category))
        print('' .join(blank_word))

        # Create an empty string called guess that will eventually hold the users guess.
        guess = ''
        # Create a variable guess_count and set it equal to zero.
        guess_count = 0

        # A single round loop
        while(guess != game_word):
            guess = input("\nEnter your guess: ")
            guess_count += 1
            if guess == game_word:
                print("Correct! You guessed the word in {} guesses." .format(guess_count))
                break
            else:
                print("That is not correct. Let us reveal a letter to help you!")
                reveal = True
                while(reveal):
                    letter_index = random.randint(0,len(game_word)-1)
                    if blank_word[letter_index] == "_":
                        blank_word[letter_index] = game_word[letter_index]
                        reveal = False
                print('' .join(blank_word))
            if guess_count == len(game_word):
                print("\nYou Lost the game as you exceeded the guess count limit.")
                break

        # Ask the user to play again
        choice = input("Would you like to play again (y/n): ").lower()
        if choice == 'n':
            play = False
        print("Thank you for playing our game.")


