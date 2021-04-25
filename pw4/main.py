import curses
from output import OutputModule
from input import InputModule
from domains.Student import *
from domains.Course import *
from domains.Mark import *


class MainModule:
#Main
    S = int(student_num())
    L = 1
    while L <= s:
        L += 1
        add_student()
        show_list_student()

    C = int(course_num())
    P = 1
    while P <= c:
        P += 1
        add_course()
        show_list_course()

#mark_gpa
    mark_GPA()

    create_mark()
    for i in range(0, len(Course)):
        ol = int(input("You choose: "))
        if ol == 1:
            print("--STUDENT MARK--")
            show_mark()
            break
        else:
            break
