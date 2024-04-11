import curses

def draw_border(win):
    # Get window dimensions
    height, width = win.getmaxyx()

    # Draw border
    win.border('|', '|', '-', '-', '+', '+', '+', '+')

def main(stdscr):
    # Turn off cursor blinking
    curses.curs_set(0)

    # Get screen dimensions
    height, width = stdscr.getmaxyx()

    # Create a new window
    borderwin = curses.newwin(height-2, width-2, 1, 1)
    borderwin.box()

    # Draw a border around the window
    draw_border(borderwin)

    # Refresh the screen to see changes
    stdscr.refresh()
    borderwin.refresh()

    # Wait for user input
    stdscr.getch()

# Initialize curses and run the main function
curses.wrapper(main)
