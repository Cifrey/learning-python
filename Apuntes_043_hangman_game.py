# Hangman in Python
import random

possible_words = ("apple", "algomuylargoequisdejaja")

# dictionary of key:()
hangman_art = {0: ("   ",
                   "   ",
                   "   "), 
               1: (" O ",
                   "   ",
                   "   "), 
               2: (" O ",
                   " | ",
                   "   "), 
               3: (" O ",
                   "/| ",
                   "   "), 
               4: (" O ",
                   "/|\\",
                   "   "), 
               5: (" O ",
                   "/|\\",
                   "/  "), 
               6: (" O ",
                   "/|\\",
                   "/ \\ ")}

def chosen_word():
    return (random.choice(possible_words)) 

def print_invisible_word(word):
    return " ".join("_" for _ in word)

def word_progress():
    pass

def main():
    while True: 
        print("*" * 30)
        print("Welcome to the Hangman Game!".center(30))
        for row in hangman_art[6]:
            print(row.center(30))
        print("*" * 30)

        word = chosen_word()

        print("Word to guess: ", print_invisible_word(word))
        print()

        mistakes = 0
        letters = []
        answer = ""

        while mistakes <= 5:
            guess = input("\nPlease, enter your guess: \n")
            if not guess.isalpha():
                print("Please, enter a letter")
                continue

            if guess in word:
                print(f"Yes! '{guess}' is in ", print_invisible_word(word), ".")
                letters.append(guess)
                answer = "".join(letters)
                # Mostrar aquí la palabra actualizada con la letra
                print(answer)
                
            else:
                mistakes += 1
                print(f"No, '{guess}' is not in ", print_invisible_word(word))
                # Mostrar aquí la palabra otra vez, actualizada

                for row in hangman_art[mistakes]:
                    print(row.center(30))

            if answer == word or mistakes == 6:
                print(f"Yes! {answer} is the correct answer!")
                play_again = input("Game over! Dou you want to play again? (Y/N): ").lower()
                if play_again != "y":
                    break

            print(mistakes)


if __name__ == "__main__":
    main()