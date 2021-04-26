"""
:Author: Dao Trong Le Thai
:ID: BA9-055
:Lab work: 3
"""

import math
import numpy


# ------------------------------ Lists -------------------------------------

students = []
courses = []
studentMarks = []


# ------------------------------ Student -------------------------------------
class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob

    def describe(self):
        print(self.__id + " " + self.__name + " " + self.__dob)

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getAvg(self):
        return self.__avg

    def setAvg(self, avg):
        return self.__avg

# ------------------------------ Course -------------------------------------
class Course:
    def __init__(self, id, name, credit):
        self.__c_ID = id
        self.__c_Name = name
        self.__credit = credit

    def describe(self):
        print("ID: " + self.__c_ID + " Course name: " + self.__c_Name + " credit: " + self.__credit)

    def getName(self):
        return self.__c_Name

# ------------------------------ Marks -------------------------------------
class StudentMark:
    def __init__(self, student, course, mark):
        self.__student = student
        self.__course = course
        self.__mark = mark

    def getStudent(self):
        return self.__student

    def getCourse(self):
        return self.__course

    def getMark(self):
        return self.__mark

    def describe(self):
        print(self.__student.getId() + " " + self.__student.getName() + " "
              + self.__course.getName() + " " + str(self.__mark))

# ------------------------------ Add Student -------------------------------------
def add_student():
    print("-----ADD A STUDENT-----")

    id = input("Student ID: ")
    name = input("Student name: ")
    dob = input("Student DoB: ")
    student = Student(id, name, dob)
    students.append(student)

# ------------------------------ Add Course -------------------------------------
def add_course():
    print("---- ADD A COURSE ----")

    id = input("Course  ID: ")
    name = input("Course name: ")
    credit = input("Course credit: ")
    course = Course(id, name, credit)
    courses.append(course)

# ------------------------------ Mark -------------------------------------
def add_mark():
    courseName = input("Input course's name to input marks: ")
    for c in courses:
        if c.getName() == courseName:
            for s in students:
                mark = math.floor(float(input("Input " + s.getName() + "'s mark: ")))
                studentMark = StudentMark(s, c, mark)
                studentMarks.append(studentMark)
                s.setAvg(calculateAvg(s.getId()))

# ------------------------------ Display Course -------------------------------------
def display_course():
    print("Course List:")
    for c in courses:
        c.describe()

# ------------------------------ Display Student -------------------------------------
def display_student():
    print("Student List:")
    for s in students:
        s.describe()

# ------------------------------ Display Mark -------------------------------------
def display_mark():
    courseName = input("Enter course's name to show marks: ")
    print("Student Marks for " + courseName)
    for studentMark in studentMarks:
        if courseName == studentMark.getCourse().getName():
            studentMark.describe()


# ------------------------------ Calculate Average score -------------------------------------

def calculateAvg(id):
    marks = []
    for studentMark in studentMarks:
        if (studentMark.getStudent().getId() == id):
            marks.append(studentMark.getMark())
    return numpy.average(marks)


# ------------------------------  Display Average score -------------------------------------
def display_Avarage():
    id = input("Input student id: ")
    for s in students:
        if id == s.getId():
            print("Name: " + s.getName() + " Avg: " + str(s.getAvg()))

def sortbyAvg():
    sortedList = sorted(students, key=lambda x: x.gpa, reverse=True)
    for s in sortedList:
        s.describe()

#------------------------------ Calculate WeightedSum -------------------------------------
def calculateWeightedSum(id):
    sum = 0
    for c in courses:
        smark = []
        warray = []
        for studentMark in studentMarks:
            if (studentMark.getStudent().getId == id):
                smark.append(studentMark.getMark())
                warray.append(c.etc)
        weights = numpy.array(warray)
        amark = numpy.array(smark)
        sum = sum + numpy.sum(numpy.dot(amark, weights))
    return sum

# ------------------------------ Display WeightedSum -------------------------------------
def display_WeightedSum():
    id = input("Input student id: ")
    print("Weighted sum: " + str(calculateWeightedSum(id)))

#------------------------------ MENU -------------------------------------
def menu_option():
    option = "-1";
    while (option != "0"):
        print("1. Add students \n"
              "2. Add courses  \n"
              "3. Add marks   \n"
              "4. Show student list \n"
              "5. Show course list \n"
              "6. Show mark list \n"
              "7. Calculate average score \n"
              "8. Calculate weighted sum \n"
              "9. Sort student list \n"
              "0. Exit ")
        option = input("Enter your option: ")
        if (option == "1"):
            add_student()
        elif (option == "2"):
            add_course()
        elif (option == "3"):
            add_mark()
        elif (option == "4"):
            display_student()
        elif (option == "5"):
            display_course()
        elif (option == "6"):
            display_mark()
        elif (option == "7"):
            display_Avarage()
        elif (option == "8"):
            display_WeightedSum();
        elif (option == "9"):
            sortbyAvg();

menu_option()
print("The program has ended")