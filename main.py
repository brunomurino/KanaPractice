import random
import os
import sys
from pyfiglet import figlet_format

import hiragana
from hiragana import Hiragana

import katakana
from katakana import Katakana

def getMenuChoice(menuLength):

    while True:
        try:
            inp = int(input("Choose number from menu: "))
            if inp > 0 and inp <= menuLength:
                return inp
            print("Invalid choice.")
        except:
            print("Only numbers allowed.")

def printMenu(options):

    print(figlet_format('Kana Practice'))

    print("")
    for opt in list(options.items()):
        print("\t{:d}. {:s}".format(opt[0], opt[1][0]))
    print("")

def play(choice):

    if choice == 1:
        kana = Hiragana().hiragana
    elif choice == 2:
        kana = Katakana().katakana

    pair_list = random.sample(list(kana.items()), 3)

    correct_answer_list = [pair[0] for pair in pair_list]
    correct_answer = " ".join(correct_answer_list)

    question = [pair[1] for pair in pair_list]
    question = " ".join(question)

    answers = input("\n\t{}\n\n\t".format(question))
    if answers == 'quit' or answers == 'q':
        main()
    answers_list = answers.split()

    score_list = [ int(ans == corr) for ans, corr in\
        zip(answers_list, correct_answer_list)]

    print("\nTruth:\t{}\t\n".format(correct_answer))
    print("Score:\t{}\n\nTotal:\t{}".format(score_list, sum(score_list)))
    input("\nPress anything to move on...")

def main():

    os.system('clear')

    options = {
        1: ['Practice Hiragana', play],
        2: ['Practice Katakana', play],
        3: ['Quit', sys.exit]
    }

    printMenu(options)
    choice = getMenuChoice(len(options))

    if choice != 3:
        while True:
            os.system('clear')
            printMenu(options)
            print("Choose number from menu: {}".format(choice))
            print("\n\t{}\n\t\tEnter 'q' or 'quit' to go back to the menu."\
            .format(options[choice][0]))
            options[choice][1](choice)

    options[choice][1]()    

if __name__ == "__main__":

    while True:
        main()