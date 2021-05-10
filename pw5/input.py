from domains import Student, Course, StudentMark
import math

from pw4.output import calculateAvg


def add_student(students):
    id = input("Student's ID: ")
    name = input("Student's name: ")
    dOB = input("Student's DOB: ")
    student = Student.Student(id, name, dOB)
    students.append(student)

    f = open('Students.txt', 'a')
    f.write("StudentID: " + id + "\n" + "StudentName: " + name + "\n" + "SudentDoB: " + DoB)
    f.close()

def add_course(courses):
    id = input("Course's ID: ")
    name = input("Course's name: ")
    etc = input("Course's etc: ")
    course = Course.Course(id, name, etc)
    courses.append(course)

    f = open('Courses.txt', 'a')
    f.write("CourseID: " + id + "\n" + "CourseName: " + name + "\n" + "Course_credit: " + str(credit))
    f.close()



def add_mark(courses, students, studentMarks):
    courseName = input("Input course's name to input marks: ")
    for c in courses:
        if c.get_Name() == courseName:
            for s in students:
                mark = math.floor(float(input("Input " + s.get_Name() + "'s mark: ")))
                studentMark = StudentMark.StudentMark(s, c, mark)
                studentMarks.append(studentMark)
                s.set_Avg(calculateAvg(s.get_ID(), studentMarks))

    f = open('Marks.txt', 'a')
    f.write("CourseID: " + c_id + "\n" + "StudentID: " + s_id + "\n" + "Mark_detail: " + str(mark))
    f.close()