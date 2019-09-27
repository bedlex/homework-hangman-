#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint
import re
class hangman():
    def __init__(self,word,guess_word):
        self.word = word
        self.guess_word = guess_word
        self.mistakes = 0
        self.point = 0

    def letter_check(self):
        while self.word != self.guess_word:
            answer = input("enter a guessing letter: ")
            mistake_check = False
            for i in range(len(self.word)):
                if answer.lower() == self.word[i]:
                    self.guess_word[i] = self.word[i]
                    mistake_check = True
            if mistake_check == False:
                self.mistakes += 1
            if self.word == self.guess_word:
                self.point +=1

            print(self.guess_word)
            print("you have {} mistakes".format(self.mistakes))
            print("you have {} pionts".format(self.point))
            if self.mistakes >= 9:
                print("You lose")
                print("You got {} points".format(self.point))
                self.mistakes = 0
                self.point = 0
                break



    def word_inicial(self):
        self.word = []
        self.guess_word = []
        with open("words.txt") as f:
            data = f.readlines()

        format_world = re.compile('[\W_]+')

        words_dict = {}
        i = 0
        for word in data:
            a_list = []
            p = re.split(r"L%9", word)

            a_list.append(p[0])
            a_list.append((str(format_world.sub(" ", p[1]))).strip().lower())
            words_dict[i] = a_list
            i += 1

        nums = randint(0, len(words_dict) - 1)



        print(words_dict[nums][0])
        word_import = words_dict[nums][1]
        for i in range(len(word_import)):
            self.word.append(word_import[i])
            self.guess_word.append("-")

        print(self.guess_word)
        print("you have {} mistakes".format(self.mistakes))
        print("you have {} pionts".format(self.point))

def main():
    while True:
        start = hangman([], [])
        quit_hang = input("Do you want to quit y/n: ")
        if quit_hang.lower() == "n":
            while True:

                answer = input("Next word? y/n: ")
                if answer.lower() == "y":
                    start.word_inicial()
                    start.letter_check()
                elif answer.lower() =="n":
                    break
                else:
                    print("Wrong input")
        elif quit_hang.lower() =="y":
            break
        else:
            print("Wrong input")

main()



# dict = {"word":"quations","summer":"quation2"}
#
# for word in dict:
#     print (dict[word])
#     answer = input("Enter a letter from word")
#     for letter in dict[word]:
#         print(letter)
#         if answer == letter:
#             letter_check = True
#

"""
Created on Fri Sep 27 15:35:58 2019

@author: bedlex
"""

n