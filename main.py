import random
import os
import sys

import hiragana
from hiragana import Hiragana

def play_round(difficulty = 3):

    hira = Hiragana().hiragana

    pair_list = random.sample(list(hira.items()), difficulty)

    correct_answer_list = [pair[0] for pair in pair_list]
    correct_answer = " ".join(correct_answer_list)

    question = [pair[1] for pair in pair_list]
    question = " ".join(question)

    answers = input("\n\t{}\n\n\t".format(question))
    if answers == 'quit' or answers == 'q':
        sys.exit()
    answers_list = answers.split()

    score_list = [ int(ans == corr) for ans, corr in\
        zip(answers_list, correct_answer_list)]

    print("\nTruth:\t{}\t\n".format(correct_answer))
    print("Score:\t{}\n\nTotal:\t{}".format(score_list, sum(score_list)))

if __name__ == "__main__":

    os.system('clear')

    while True:
        play_round()
