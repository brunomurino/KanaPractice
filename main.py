import random
import os
import sys

import hiragana
from hiragana import Hiragana

def play_round(difficulty = 3):

    hira = Hiragana().hiragana

    pair_list = random.sample(list(hira.items()), difficulty)

    question = []
    correct_answer_list = []
    for pair in pair_list:
        correct_answer_list.append(pair[0])
        question.append(pair[1])

    question = " ".join(question)
    correct_answer = " ".join(correct_answer_list)

    answers = input("\n\t{}\n\t".format(question))
    if answers == 'quit' or answers == 'q':
        sys.exit()
    answers_list = answers.split()

    score_list = [ int(ans == corr) for ans, corr in\
        zip(answers_list, correct_answer_list)]

    print("Truth:\n\t{}\t".format(correct_answer))
    print("Score:\n\t{}\nTotal:\t{}".format(score_list, sum(score_list)))

if __name__ == "__main__":

    os.system('clear')

    while True:
        play_round(difficulty = 3)
