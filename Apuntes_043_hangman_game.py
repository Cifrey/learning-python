# Hangman in Python
import random

possible_words = ("bastet", "solanum", "rance", "beatrice", "umineko", "tonto", 
                  "dostoyevski", "tolstoi", "nietzsche", "python", "javascript",
                  "asimov", "software", "developer", "cybersecurity", "hacker")

hangman_art = {
    0: ("   ",
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
        "/ \\ ")
}

def chosen_word():
    return random.choice(possible_words)

def print_invisible_word(word):
    return " ".join("_" for _ in word)

def progress(word, correct_letters):
    return " ".join([letter if letter in correct_letters else "_" for letter in word])

def main():
    while True:
        print("*" * 30)
        print("Welcome to the Hangman Game!".center(30))
        for row in hangman_art[6]:
            print(row.center(30))
        print("*" * 30)

        word = chosen_word()

        print("Word to guess:", print_invisible_word(word))
        print()

        mistakes = 0
        correct_letters = []
        all_guesses = []

        while mistakes <= 5:
            guess = input("\nPlease, enter your guess: \n").lower()

            if not guess.isalpha() or len(guess) != 1:
                print("\nPlease, enter a single letter\n")
                continue

            if guess in all_guesses:
                print("\nYou already guessed that letter!\n")
                continue

            all_guesses.append(guess)

            if guess in word and guess not in correct_letters:
                correct_letters.append(guess)
                print(f"\nYes! '{guess}' is in the word\n")
                print(progress(word, correct_letters))
            else:
                mistakes += 1
                print(f"\nNo, '{guess}' is not in the word\n")
                print(progress(word, correct_letters))
                print()
                for row in hangman_art[mistakes]:
                    print(row.center(30))

            if "_" not in progress(word, correct_letters):
                print(f"\nCongratulations! You guessed the word: '{word}'\n")
                break

            if mistakes == 6:
                print(f"\nGame over! The word was: '{word}'\n")
                break

        play_again = input("\nDo you want to play again? (Y/N): \n").lower()
        if play_again != "y":
            break

if __name__ == "__main__":
    main()
