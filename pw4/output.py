import numpy
import curses
from domains.Student import *
from domains.Course import *
from domains.Mark import *


class OutputModule:
    @staticmethod
    def show_list_student():
        def show_list_student():
            print("----Student list----")
            for i in range(0, len(Student)):
                print(f"ID:{Student[i]['id']} name:{Student[i]['name']} DoB:{Student[i]['dob']}")

    @staticmethod
    def show_list_course():
        print("----Course list----")
        for i in range(0, len(Course)):
            print(f"ID:{Course[i]['id']}  name : {Course[i]['name']}")

    @staticmethod
    def show_mark():
        print("----Student mark list----")
        for i in range(0, len(Mark)):
            print(f"ID-course: {Mark[i]['b']} ID-Student: {Mark[i]['a']}  mark:{Mark[i]['mark']}")
