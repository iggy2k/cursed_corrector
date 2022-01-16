import curses
from curses.textpad import Textbox, rectangle
import textwrap
TITLE = "\n                     _                           _        \n" +\
        "    ___ _ __ ___  __| |   ___ ___  _ __ _ __ ___| |_ _ __ \n" +\
        "   / __| '__/ __|/ _` |  / __/ _ \| '__| '__/ __| __| '__|\n" +\
        "  | (__| |  \__ \ (_| | | (_| (_) | |  | | | (__| |_| |   \n" +\
        "   \___|_|  |___/\__,_|  \___\___/|_|  |_|  \___|\__|_|   \n"
SUBTITLE = "A PyJac project by"
SUBTITLE2 = "Alex and Ali"
SUBTITLE3 = "Press ESC to exit. Press CTRL + G to process your text."
INPUT = "Enter a text to autocorrect:"
OUTPUT = "Autocorrected output:"


def main(stdscr):
    text = ''
    key = 0
    # Exit by pressing escape
    while (key != 27):

        stdscr.clear()
        stdscr.refresh()
        curses.start_color()

        # Lime on black
        curses.init_pair(1, 10, 0)
        # Magenta on black
        curses.init_pair(2, 5, 0)
        # Gray on black
        curses.init_pair(3, 8, 0)

        # Get window dimensions
        rows, cols = stdscr.getmaxyx()

        # Center coordinates for titles
        title_x = int((cols // 2) - (len(TITLE) // 10) - len(TITLE) % 2)
        subtitle_x = int(
            (cols // 2) - (len(SUBTITLE) // 2) - len(SUBTITLE) % 2)
        subtitle2_x = int(
            (cols // 2) - (len(SUBTITLE2) // 2) - len(SUBTITLE2) % 2)
        subtitle3_x = int(
            (cols // 2) - (len(SUBTITLE3) // 2) - len(SUBTITLE3) % 2)
        input_x = int(
            (cols // 2) - (len(INPUT) // 2) - len(INPUT) % 2)
        output_x = int(
            (cols // 2) - (len(OUTPUT) // 2) - len(OUTPUT) % 2)
        subtitle_y = rows // 2

        # Title
        stdscr.attron(curses.color_pair(2))
        for y, line in enumerate(TITLE.splitlines()):
            stdscr.addstr(y, title_x, line)
        stdscr.attron(curses.color_pair(1))

        # Properly display processed text
        for i, line in enumerate(textwrap.wrap(text, 30)):
            stdscr.addstr(subtitle_y // 2 + 10 + i, (input_x) +
                          input_x // 2, line)

        # PyJac
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(subtitle_y // 2 + 2, subtitle_x, SUBTITLE)

        # Authors
        stdscr.attron(curses.color_pair(2))
        stdscr.addstr(subtitle_y // 2 + 4, subtitle2_x, SUBTITLE2)

        # Exit
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(subtitle_y // 2 + 6, subtitle3_x, SUBTITLE3)

        # Input
        stdscr.attron(curses.color_pair(2))
        stdscr.addstr(subtitle_y // 2 + 8, input_x // 2 - 1, INPUT)

        # Output
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(subtitle_y // 2 + 8, (input_x) + input_x // 2, OUTPUT)

        # Input window zone
        stdscr.attron(curses.color_pair(2))
        editwin = curses.newwin(5, 30, subtitle_y // 2 + 10, input_x // 2)
        rectangle(stdscr, subtitle_y // 2 + 9, input_x // 2 - 1,
                  subtitle_y + 7, (input_x // 2) + 31)

        # Output window zone
        stdscr.attron(curses.color_pair(1))
        rectangle(stdscr, subtitle_y // 2 + 9, (input_x) + input_x//2,
                  subtitle_y + 7, (input_x) + input_x//2 + 31)
        outwin = curses.newwin(5, 30, subtitle_y // 2 + 10, input_x +
                               input_x // 2)
        stdscr.refresh()

        # Textbox magic
        textbox = Textbox(editwin)
        textbox.edit()
        text = textbox.gather()

        stdscr.refresh()

    def input(stdscr):
        return


curses.wrapper(main)
