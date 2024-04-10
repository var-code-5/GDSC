import curses
import curses.textpad


sections = []
section_size = 30

def draw_border(win):
        win.border('|', '|', '-', '-', '+', '+', '+', '+')

class section:
    def __init__(self):
        self.sec_len = len(sections)
        self.section_win = curses.newwin(curses.LINES - 6,section_size,6,10+(self.sec_len)*section_size)
        draw_border(self.section_win)
        self.heading_win = curses.newwin(2,28,7,11+(self.sec_len)*section_size)
        self.heading_win.border('|', '|', ' ', '-', ' ', ' ', '+', '+')
        self.heading = curses.textpad.Textbox(self.heading_win)
        self.section_win.refresh()
        self.heading.edit()
        self.heading_win.refresh()

class task:
    pass

class kanban:
    def __init__(self,window: 'curses._CursesWindow')->None:
        window.addstr(2,10,"Title  : ")                      # Title
        title_win = curses.newwin(1,curses.COLS-20,2,19)
        self.title = curses.textpad.Textbox(title_win)
        window.addstr(3,10,"Author : ")                      # Author
        author_win = curses.newwin(1,curses.COLS-20,3,19)
        self.author = curses.textpad.Textbox(author_win)
        window.addstr(4,10,"Date   : ")                      # Date
        date_win = curses.newwin(1,curses.COLS-20,4,19)
        self.date = curses.textpad.Textbox(date_win)
        window.refresh()
        self.title.edit()
        self.author.edit()
        self.date.edit()
        #making the board
        self.board1 =curses.newwin(curses.LINES - 6,curses.COLS-20,5,10)      
        #making the default sections
        sections.append(section())
        sections.append(section())
        sections.append(section())
        window.refresh()
        

def initialize(window):
    window.clear()
    text = "<> GDSC"
    window.addstr(1,(int(curses.COLS/2)-int(len(text)/2)),text)
    segment_1 = curses.newwin(curses.LINES - 6,30,5,10)
    segment_1.box()
    segment_1.addstr(0,0,"+")
    segment_1.addstr(0,29,"+")
    segment_1.addstr(curses.LINES-7,0,"+")
    segment_1.refresh()

def c_main(stdscr:'curses._CursesWindow'):
    initialize(stdscr)
    boards = []
    boards.append(kanban(stdscr))
    stdscr.refresh()
    stdscr.getch()
    return 0

def main()->int:
    return curses.wrapper(c_main)

if __name__ == "__main__":
    main()