import curses
import curses.textpad

def initialize(window):
    window.clear()
    text = "<> GDSC"
    window.addstr(1,(int(curses.COLS/2)-int(len(text)/2)),text)
    window.addstr(2,10,"Title  : ")
    title_win = curses.newwin(1,curses.COLS-20,2,19)
    title = curses.textpad.Textbox(title_win)
    window.addstr(3,10,"Author : ")
    author_win = curses.newwin(1,curses.COLS-20,3,19)
    author = curses.textpad.Textbox(author_win)
    window.addstr(4,10,"Date   : ")
    date_win = curses.newwin(1,curses.COLS-20,4,19)
    date = curses.textpad.Textbox(date_win)
    window.refresh()
    segment_1 = curses.newwin(curses.LINES - 6,30,5,10)
    segment_1.box()
    segment_1.addstr(0,0,"+")
    segment_1.addstr(0,29,"+")
    segment_1.addstr(curses.LINES-7,0,"+")
    segment_1.refresh()
    title.edit()
    author.edit()
    date.edit()
    window.getch()

def c_main(stdscr:'curses._CursesWindow'):
    initialize(stdscr);
    
    return 0;

def main()->int:
    return curses.wrapper(c_main)

if __name__ == "__main__":
    main()