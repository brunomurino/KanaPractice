"""source /anaconda3/bin/activate & conda activate envTF"""

import sys
import random
import curses
from curses import wrapper

import layout
from layout import drawApp

import hiragana
from hiragana import Hiragana

import katakana
from katakana import Katakana

def getMenuChoice(window, menuLength):

    while True:
        try:
            curses.echo()
            window.addstr(9, 8, 'Press option number: ', curses.color_pair(1))
            window.addstr(9, 8+len('Press option number: '),\
                ' '*1, curses.color_pair(1))
            menuInput = window.getstr(9, 8+len('Press option number: '), 1)
            curses.noecho()

            inp = int(menuInput)
            if inp > 0 and inp <= menuLength:
                window.addstr(10, 8,\
                    " "*len("Only numbers allowed."), curses.color_pair(1))
                window.addstr(9, 8+len('Press option number: '),\
                    str(inp), curses.color_pair(1))
                return inp
            window.addstr(10, 8,\
                " "*len("Only numbers allowed."), curses.color_pair(1))
            window.addstr(10, 8, "Invalid choice.", curses.color_pair(1))
        except:
            window.addstr(10, 8, "Only numbers allowed.", curses.color_pair(1))

def play(window, options, choice):

    window.addstr(11, 30 - int(len("Practice Hiragana")/2),\
        "Practice Hiragana", curses.color_pair(1))

    if choice == 1:
        kana = Hiragana().hiragana
        window.addstr(11, 30 - int(len("Practice Hiragana")/2),\
        "Practice Hiragana", curses.color_pair(1))
    elif choice == 2:
        kana = Katakana().katakana
        window.addstr(11, 30 - int(len("Practice Katakana")/2),\
        "Practice Katakana", curses.color_pair(1))

    pair_list = random.sample(list(kana.items()), 3)

    correct_answer_list = [pair[0] for pair in pair_list]
    correct_answer = " ".join(correct_answer_list)

    question = [pair[1] for pair in pair_list]
    question = " ".join(question)

    window.addstr(14, 10, ' '*40, curses.color_pair(1))
    window.addstr(15, 10, ' '*40, curses.color_pair(1))
    window.addstr(16, 10, ' '*40, curses.color_pair(1))
    window.addstr(17, 10, ' '*40, curses.color_pair(1))
    window.addstr(19, 10, ' '*40, curses.color_pair(1))
    window.addstr(21, 10, ' '*40, curses.color_pair(1))

    window.addstr(14, 10, question, curses.color_pair(1))

    curses.echo()
    answers = window.getstr(15, 10, 11).decode("utf-8")
    curses.noecho()

    if answers == "q":
        main(window)
    window.addstr(15, 10, answers, curses.color_pair(1))
    
    window.addstr(17, 10, correct_answer, curses.color_pair(1))

    answers_list = answers.split()
    score_list = [ str(int(ans == corr)) for ans, corr in\
            zip(answers_list, correct_answer_list)]
    total = str(sum([ int(ans == corr) for ans, corr in\
            zip(answers_list, correct_answer_list)]))

    window.addstr(19, 10, "   ".join(score_list), curses.color_pair(1))
    window.addstr(21, 40, "Total: {}".format(total), curses.color_pair(1))

    curses.curs_set(False)
    window.getch()
    curses.curs_set(True)

def main(stdscr):

    # Clear screen
    stdscr.clear()

    # Initialize color pair
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)

    options = {
        1: ['Practice Hiragana', play],
        2: ['Practice Katakana', play],
        3: ['Quit', sys.exit]
    }

    drawApp(stdscr, options)

    choice = getMenuChoice(stdscr, 3)

    while True:
        options[choice][1](stdscr, options, choice)

stdscr = curses.initscr()

wrapper(main)
