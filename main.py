import random
import os
import sys

import hiragana
from hiragana import Hiragana

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

    print("")
    for opt in list(options.items()):
        print("\t{:d}. {:s}".format(opt[0], opt[1][0]))
    print("")

def playHiragana(difficulty = 3):

        hira = Hiragana().hiragana

        pair_list = random.sample(list(hira.items()), difficulty)

        correct_answer_list = [pair[0] for pair in pair_list]
        correct_answer = " ".join(correct_answer_list)

        question = [pair[1] for pair in pair_list]
        question = " ".join(question)

        answers = input("\n\t{}\n\n\t".format(question))
        if answers == 'quit' or answers == 'q':
            menu()
        answers_list = answers.split()

        score_list = [ int(ans == corr) for ans, corr in\
            zip(answers_list, correct_answer_list)]

        print("\nTruth:\t{}\t\n".format(correct_answer))
        print("Score:\t{}\n\nTotal:\t{}".format(score_list, sum(score_list)))

def main():

    os.system('clear')

    options = {
        1: ['Practice Hiragana', playHiragana],
        2: ['Practice Katakana', playHiragana],
        3: ['Quit', sys.exit]
    }

    printMenu(options)
    choice = getMenuChoice(len(options))

    if choice != 3:
        print("\n\t{}\n\t\tEnter 'q' or 'quit' to go back to the menu."\
            .format(options[choice][0]))
    while True:
        options[choice][1]()

if __name__ == "__main__":

    while True:
        main()