'''Using while loop create a guess word game.
Program should use a list of predefined words
User should have options to choose to guess letter or the whole word.
If user decide to guess word and fails then game is over.
If user decide to guess a letter in word then program says if this letter occurs in the word.
User can guess any amount of letters.'''

# Program should use a list of predefined words.
import random

# Program should choose a random word and ask user to guess it
list_of_words = ["banana", "apple", "tomato"]
random_word = random.choice(list_of_words)
signal = None
while True:

    input_word = input("Choose what you want to guess the whole word (w)  or a letter (l)?:  ")
    # If user decide to guess word and fails then game is over.
    if input_word == "w":
        input_guess_word = input("Guess a word: ")
        if input_guess_word == random_word:
            print("You win!")
            break
        else:
            play_again = input("It sucks :( Game OVER!\nDo you want to play again? Yes/No: ")
            if play_again == "No":
                print("See you, Loser!")
                break
            elif play_again == "Yes":
                print("Let's try again!")
                random_word = random.choice(list_of_words)
                continue
            else:
                while True:
                    play_again_valid = input("Enter a valid Yes/No.\nPlay again? ")
                    if play_again_valid == "No":
                        print("See you, Loser!")
                        signal = "End"
                        break
                    elif play_again_valid == "Yes":
                        break
                    else:
                        continue
            if signal == "End":
                break

    # If user decide to guess a letter in word then program says
    # if this letter occurs in the word.
    elif input_word == "l":
        input_guess_letter = input("Guess a letter: ")
        if input_guess_letter in random_word:
            print("The letter is in the word!")
        else:
            print("The letter is not in the word.")


