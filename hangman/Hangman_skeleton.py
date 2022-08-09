import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for x in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_letters = []
        print(f"The mystery word has {len(self.word)} characters")
        print(' '.join(self.word_guessed))

    def check_letter(self, letter) -> None:
        if (letter.lower() in self.word):
            index = 0
            for x in self.word:
                if x == letter.lower():
                    self.word_guessed[index] = letter.lower()
                index += 1
            self.num_letters -= 1
            print("Nice! " + letter.lower() + " is in the word!")
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print("Sorry, " + letter.lower() + " is not in the word.")
            print("You have " + str(self.num_lives) + " lives left.")
        pass

    def ask_letter(self):
        while True:
            letter = input("Enter a letter you would like to guess: ")
            if not len(letter) == 1 and letter.isalpha():
                 print("Please, enter just one character")
            elif letter in self.list_letters:
                print(f"{letter} was already tried")
            else:
                break
        self.list_letters.append(letter)
        self.check_letter(letter)   
        pass

def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    while game.num_lives > 0 and game.num_letters > 0:
        game.ask_letter()
        print(f"Your guesses so far: {' '.join(game.word_guessed)}")
        print(f"You have {game.num_lives} lives remaining, and you've got {game.num_letters} letters left to guess.")
    if game.num_letters == 0:
        print("Congratulations you won!")
    else:
        print("You ran out of lives. The word was " + game.word)
    pass

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)