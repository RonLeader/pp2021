from domains import Student, Course, StudentMark
import math

from pw4.output import calculateAvg


def add_student(students):
    id = input("Student's ID: ")
    name = input("Student's name: ")
    dOB = input("Student's DOB: ")
    student = Student.Student(id, name, dOB)
    students.append(student)

def add_course(courses):
    id = input("Course's ID: ")
    name = input("Course's name: ")
    etc = input("Course's etc: ")
    course = Course.Course(id, name, etc)
    courses.append(course)


def add_mark(courses, students, studentMarks):
    courseName = input("Input course's name to input marks: ")
    for c in courses:
        if c.get_Name() == courseName:
            for s in students:
                mark = math.floor(float(input("Input " + s.get_Name() + "'s mark: ")))
                studentMark = StudentMark.StudentMark(s, c, mark)
                studentMarks.append(studentMark)
                s.set_Avg(calculateAvg(s.get_ID(), studentMarks))