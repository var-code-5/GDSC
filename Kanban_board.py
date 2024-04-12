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
        self.add_task_win = curses.newwin(3,int(section_size/2),curses.LINES-3,10+(self.sec_len)*section_size)
        self.sort_sections_win = curses.newwin(3,int(section_size/2),curses.LINES-3,10+(self.sec_len)*section_size+int(section_size/2))
        self.add_task_win.addstr(1,0," + Add task")
        self.sort_sections_win.addstr(1,0," ^   Sort ")
        self.task_count = 0
        self.add_section_win = curses.newwin(3,5,6,10+(self.sec_len)*section_size)
        self.add_section_win.addstr(1,2,"+",curses.color_pair(1))
        draw_border(self.add_section_win)
        draw_border(self.add_task_win)
        draw_border(self.sort_sections_win)
        if(self.sec_len==0):
            self.heading_win.addstr(0,0,"TODO")
            self.section_win.refresh()
            self.heading_win.refresh()
            self.add_task_win.refresh()
            self.sort_sections_win.refresh()
            self.add_section_win.mvwin(6,10+(self.sec_len+1)*section_size)
            self.add_section_win.refresh()
        elif(self.sec_len==1):
            self.heading_win.addstr(0,0,"IN PROGRESS")
            self.section_win.refresh()
            self.heading_win.refresh()
            self.add_task_win.refresh()
            self.sort_sections_win.refresh()
            self.add_section_win.mvwin(6,10+(self.sec_len+1)*section_size)
            self.add_section_win.refresh()
        elif(self.sec_len==2):
            self.heading_win.addstr(0,0,"DONE")
            self.section_win.refresh()
            self.heading_win.refresh()
            self.add_task_win.refresh()
            self.sort_sections_win.refresh()
            self.add_section_win.mvwin(6,10+(self.sec_len+1)*section_size)
            self.add_section_win.refresh()
        else:
            self.heading = curses.textpad.Textbox(self.heading_win)
            self.section_win.refresh()
            self.heading.edit()
            self.heading_win.refresh()
            self.add_task_win.refresh()
            self.sort_sections_win.refresh()
            self.add_section_win.mvwin(6,10+(self.sec_len+1)*section_size)
            self.add_section_win.refresh()

    def sort_sections(self):
        for i in range(len(sections)):
            if sections[i] == self:
                section = i
        tasks[section].sort(key=lambda x: x.task_priority_value)
        for i in range(self.task_count):
            tasks[section][i].task_win.mvwin(10+i*task_row_size,11+section*section_size)
            tasks[section][i].task_win.refresh()


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
        # task priority
        self.task_priority = self.task_win.derwin(1,2,0,section_size-6)
        self.priority_text = curses.textpad.Textbox(self.task_priority)
        self.priority_text.edit()
        self.task_priority.refresh()
        self.priority = self.priority_text.gather()
        self.task_priority.clear()
        if self.priority == 'Hq':
             self.task_win.addstr(0,section_size-6,"H",curses.color_pair(3))
             self.task_priority_value = 1
        elif self.priority == 'Mq':
             self.task_win.addstr(0,section_size-6,"M",curses.color_pair(2))
             self.task_priority_value = 2
        elif self.priority == 'Lq':
             self.task_win.addstr(0,section_size-6,"L",curses.color_pair(1))
             self.task_priority_value = 3
        else:
             self.task_win.addstr(0,section_size-6,self.priority[0])
             self.task_priority_value = 4
        # assignee and repotee
        self.task_win.addstr(3,1,"Assigned to: ",curses.color_pair(4))
        self.task_win.addstr(4,1,"Report to  : ",curses.color_pair(2))
        self.task_win.refresh()
        # task description
        self.description_win = self.task_win.derwin(2,section_size-4,1,1)
        self.description = curses.textpad.Textbox(self.description_win)
        self.description.edit()
        self.description_win.refresh()
        self.description_win.refresh()
        #assigned and reported tasks
        self.assigned_task_win = self.task_win.derwin(1,section_size-17,3,14)
        self.assigned_task = curses.textpad.Textbox(self.assigned_task_win)
        self.assigned_task.edit()
        self.assigned_task_win.refresh()
        self.reported_task_win = self.task_win.derwin(1,section_size-17,4,14)
        self.reported_task = curses.textpad.Textbox(self.reported_task_win)
        self.reported_task.edit()
        self.reported_task_win.refresh()
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
    for i in range(len(sections)):
        if(x>=10+i*section_size and x<=10+int(section_size/2)+i*section_size) and (y>max_lines-4 and y<= max_lines):
            add_task(i,max_lines)

    # sorting the sections
    for i in range(len(sections)):
        if(x>=10+int(section_size/2)+i*section_size and x<=10+section_size+i*section_size) and (y>max_lines-4 and y<= max_lines):
            sections[i].sort_sections()

    if y>=6 and y<= 9 and x>=10+(len(sections))*section_size and x<=10+(len(sections))*section_size+4:
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
    curses.init_pair(4,curses.COLOR_CYAN,curses.COLOR_BLACK)
    curses.init_pair(5,curses.COLOR_MAGENTA,curses.COLOR_BLACK)
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
