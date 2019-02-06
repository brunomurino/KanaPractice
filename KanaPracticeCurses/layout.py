import curses
import sys

def drawFrame(window, start_y, start_x, width=0, height=0):

    for i in range(height):
        window.addstr(start_y+i, start_x, ' '*width, curses.color_pair(1))

def drawTitle(window, appFrame, appTitle):

    (window.addstr(
        appFrame['start_y']+1,
        appFrame['start_x']+int((appFrame['width']-len(appTitle))/2),
        appTitle,
        curses.color_pair(1)
    ))

def drawMenu(window, appFrame, options):

    for i, opt in enumerate(list(options.items())):

        (window.addstr(
            appFrame['start_y'] + 3 + i,
            appFrame['start_x'] + 2,
            "\t{:d}. {:s}".format(opt[0], opt[1][0]), 
            curses.color_pair(1)
        ))

def drawApp(window, options):

    appTitle = 'Kana Practice'

    appFrame = {
        'start_y' : 2,
        'start_x' : 5,
        'width' : 50,
        'height' : 23,
    }

    drawFrame(window, **appFrame)

    drawTitle(window, appFrame, appTitle)

    drawMenu(window, appFrame, options)

    window.move(0, 0)
    window.refresh()
