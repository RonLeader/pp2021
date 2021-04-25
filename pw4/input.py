# packages
import math
import numpy
import curses
from domains.Student import *
from domains.Course import *
from domains.Mark import *


class InputModule:
    @staticmethod
    def student_num():
        print("---- TOTAL NUMBER OF STUDENTS----")
        student = int(input("Total number of student:"))
        return studentt

    @staticmethod
    def add_student():
        print("=-----ADD A STUDENT-----")
        id = input("Student ID: ")
        name = input("Student name: ")
        dob = input("Student DoB: ")
        st_u = {
            'id': id,
            'name': name,
            'dob': dob
        }
        Student.append(st_u)
        StudentID.append(id)

    @staticmethod
    def course_num():
        print("---- ADD NUMBER OF COURSE----")
        course = int(input("Total number of course: "))
        return ()

    @staticmethod
    def add_course():
        print("---- ADD A COURSE ----")
        Cid = input("Course  ID: ")
        Cname = input("Course name: ")
        CC = input("Course credit: ")
        Cr_o = {
            'cid': cid,
            'cname': cname,
            'cc': cc
        }
        Course.append(Cr_o)
        CourseID.append(Cid)

    @staticmethod
    def create_mark():
        g = 1
        tu = len(Student)
        while g <= tu:
            g += 1
            x = input("Student ID: ")
            if x in Student:
                for i in range(0, len(CourseID)):
                    y = input("Course ID: ")
                    if y in CourseID:
                        mark = float(input("Student mark: "))
                        kk = {
                            'mid': x,
                            'nid': y,
                            'mark': mark
                        }
                    else:
                        print("Student ID is not found !!")
                        break
                    Mark.append(kk)
            else:
                print("Course ID is not found !!")
                break

    def mark_gpa():
        null = numpy.array([self._ccredit])
        strace.addstr("Student ID:")
        id = strace.getstr().decode()
        if id in StudentID:
            for i in range(0, len(Student)):
                marktotal = numpy.sum(null)
                gpatotal = numpy.sum(numpy.multiply(int, null))
                strace.refresh()
                gpa = gpatotal / marktotal
                strace.refresh()

        else:
            return 0
        print(gpa)

        MarkGPA.append(gpa)
        strace.refresh()
        for point in Mark:
            strace.clear()
            strace.refresh()
            strace.addstr(" [Mark: ] %s   [GPA: ]%s \n" % (mark.get_id(), gpa))

            break
