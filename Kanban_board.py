import curses
import curses.textpad


sections = []
tasks = [[],[],[],[],[],]
section_size = 30
task_row_size = 6


def draw_border(win):
        win.border('|', '|', '-', '-', '+', '+', '+', '+')

class section:
    def __init__(self):
        self.sec_len = len(sections)
        self.section_win = curses.newwin(curses.LINES - 6,section_size,6,10+(self.sec_len)*section_size)
        draw_border(self.section_win)
        self.heading_win = curses.newwin(2,28,7,11+(self.sec_len)*section_size)
        self.heading_win.border('|', '|', ' ', '-', ' ', ' ', '+', '+')
        self.add_task_win = curses.newwin(3,section_size,curses.LINES-3,10+(self.sec_len)*section_size)
        self.add_task_win.addstr(1,0," + Add task")
        self.task_count = 0
        self.add_section_win = curses.newwin(3,5,6,10+(self.sec_len)*section_size)
        self.add_section_win.addstr(1,2,"+",curses.color_pair(1))
        draw_border(self.add_section_win)
        draw_border(self.add_task_win)
        if(self.sec_len==0):
            self.heading_win.addstr(0,0,"TODO")
            self.section_win.refresh()
            self.heading_win.refresh()
            self.add_task_win.refresh()
            self.add_section_win.mvwin(6,10+(self.sec_len+1)*section_size)
            self.add_section_win.refresh()
        elif(self.sec_len==1):
            self.heading_win.addstr(0,0,"IN PROGRESS")
            self.section_win.refresh()
            self.heading_win.refresh()
            self.add_task_win.refresh()
            self.add_section_win.mvwin(6,10+(self.sec_len+1)*section_size)
            self.add_section_win.refresh()
        elif(self.sec_len==2):
            self.heading_win.addstr(0,0,"DONE")
            self.section_win.refresh()
            self.heading_win.refresh()
            self.add_task_win.refresh()
            self.add_section_win.mvwin(6,10+(self.sec_len+1)*section_size)
            self.add_section_win.refresh()
        else:
            self.heading = curses.textpad.Textbox(self.heading_win)
            self.section_win.refresh()
            self.heading.edit()
            self.heading_win.refresh()
            self.add_task_win.refresh()
            self.add_section_win.mvwin(6,10+(self.sec_len+1)*section_size)
            self.add_section_win.refresh()


class task:
    def __init__(self,row:int,column) -> None:
        # task window
        self.task_win = curses.newwin(task_row_size,section_size-2,10+row*task_row_size,11+column*section_size)
        self.task_win.box()
        sections[column].task_count += 1
        # adds color to the task
        if(column == 0):
            self.task_win.addstr(0,0,"Task :",curses.color_pair(3))
        elif(column == 1):
            self.task_win.addstr(0,0,"Task :",curses.color_pair(2))
        elif(column == 2):
            self.task_win.addstr(0,0,"Task :",curses.color_pair(1))
        else:
            self.task_win.addstr(0,0,"Task :")
        #del_task
        self.task_win.addstr(0,section_size-3,"x",curses.color_pair(3))
        self.task_win.refresh()
        # task description
        self.description_win = self.task_win.derwin(2,section_size-4,1,1)
        self.description = curses.textpad.Textbox(self.description_win)
        self.description.edit()
        self.description_win.refresh()
        self.task_win.refresh()
        pass

    def __del__(self):
        self.task_win.clear()
        self.task_win.refresh()

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
        self.sect = "TODO"
        sections.append(section())
        sections.append(section())
        sections.append(section())
        window.refresh()

def initialize(window):
    window.clear()
    text = "<> GDSC"
    window.addstr(1,(int(curses.COLS/2)-int(len(text)/2)),text)


def add_task(section:int,max_lines)->None:
    inital_point = 11
    row = sections[section].task_count
    if(max_lines-3 > inital_point+row*task_row_size):
        tasks[section].append(task(row,section))
    else:
        curses.beep() 

def del_task(section_id,task_id)->None:
    tasks[section_id].pop(task_id)
    sections[section_id].task_count -= 1
    for i in range(task_id,len(tasks[section_id])):
        y,x = tasks[section_id][i].task_win.getbegyx()
        blank_win = curses.newwin(task_row_size,section_size-2,y,x)
        blank_win.refresh()
        tasks[section_id][i].task_win.mvwin(y-task_row_size,x)
        tasks[section_id][i].task_win.refresh()

def mouse_event(x,y,max_lines,max_cols):
    # adding the tasks
    if x>=10 and x<=40 and y>= max_lines-3 and y<= max_lines:
        add_task(0,max_lines)
    elif x>=40 and x<=70 and y>= max_lines-3 and y<= max_lines:
        add_task(1,max_lines)
    elif x>=70 and x<=100 and y>= max_lines-3 and y<= max_lines:
        add_task(2,max_lines)
    elif x>=100 and x<=130 and y>= max_lines-3 and y<= max_lines and len(sections)>=4:
        add_task(3,max_lines)
    elif x>=130 and x<=160 and y>= max_lines-3 and y<= max_lines and len(sections)>=5:
        add_task(3,max_lines)


    if y>=6 and y<= 9 and x>=10+(len(sections))*section_size and x<=10+(len(sections))*section_size+4:
        print("pressed")
        if(10+(len(sections)+1)*section_size+4 < max_cols):
            sections.append(section())
        else:
            curses.beep()
    # removing the tasks

    inital_x = 38
    inital_y = 10
    for i in range(len(sections)):
        for j in range(sections[i].task_count):
            if x==inital_x+i*section_size and y==inital_y+j*task_row_size:
                del_task(i,j)


def c_main(stdscr:'curses._CursesWindow'):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_YELLOW ,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(4,curses.COLOR_WHITE,curses.COLOR_RED)
    curses.mousemask(-1)
    initialize(stdscr)
    boards = []
    boards.append(kanban(stdscr))
    stdscr.refresh()
    while True:
        c = stdscr.getch()
        if c == ord('q'):    
            return 0
        elif c == curses.KEY_MOUSE:
            _,x,y,_,bitstate = curses.getmouse()
            if bitstate & curses.BUTTON1_CLICKED:
                mouse_event(x,y,curses.LINES,curses.COLS)
                

def main()->int:
    return curses.wrapper(c_main)

if __name__ == "__main__":
    main()