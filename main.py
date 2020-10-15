import os
import random


class HangMan:
    def __init__(self):
        os.system("cls")
        self.file = open("dict_words", "r")
        self.word_dict = [i.replace("\n", "") for i in self.file]
        self.file.close()

        self.random_input = random.sample(self.word_dict, 1)
        self.inpt = self.random_input[0]
        self.lst = [i for i in self.inpt]
        self.lst2 = ["_" for i in self.inpt]
        self.hangman(self.lst[0])
        self.hangman(self.lst[-1])
        self.tries = 0

        while "_" in self.lst2:
            if self.tries != 5:
                print(f"Hangman\n-Mistakes: {self.tries}")
                self.beautify()
                self.newletter = input("-: ")
                self.hangman(self.newletter)
                os.system("cls")
            else:
                print("You lost!!")
                break

        if "_" in self.lst2:
            print(f"The word was: {self.inpt}")
        else:
            if self.tries == 1:
                print(f"You won with {self.tries} try!!")
            else:
                print(f"You won with {self.tries} tries!!")

    def hangman(self, letter):
        if letter in self.lst:
            while letter in self.lst:
                ind = self.lst.index(letter)
                self.lst[ind] = "/"
                self.lst2[ind] = letter
        else:
            self.tries += 1

    def beautify(self):
        word = ""
        for i in self.lst2:
            word += i
        print(f"    {word}")


if __name__ == "__main__":
    HangMan()
