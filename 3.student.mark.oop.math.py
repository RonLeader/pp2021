"""
:Author: Dao Trong Le Thai
:ID: BA9-055
:Lab work: 3
"""
import math
import numpy
import curses

# ------------------------------ Lists -------------------------------------
Student = []
StudentID = []
Course = []
CourseID = []
Mark = []
Credit = []
gpa = []
MarkGPA = []

# ------------------------------ Student -------------------------------------
class Students:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
        Student.append(self)
        StudentID.append(self.__id)

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob

# ------------------------------ Course -------------------------------------
class Courses:
    def __init__(self, cid, cname, ccredit):
        self._c_ID = cid
        self._c_Name = cname
        self._c_Credit = ccredits
        Course.append(self)
        CourseID.append(self._c_ID)
        Credit.append(self._c_Credit)

    def get_id(self):
        return self._c_ID

    def get_name(self):
        return self.cname

    def get_credit(self):
        return self._c_Credit

# ------------------------------ Marks -------------------------------------
class Marks:
    def __init__(self, mid, nid, mark, gpa):
        self._m_ID = mid
        self._n_ID = nid
        self._mark = mark
        Mark.append(self)

    def get_mid(self):
        return self.mid

    def get_nid(self):
        return self.nid

    def get_mark(self):
        return self.mark

    def get_gpa(self):
        return self.gpa


# Input total number of students

def student_num():
    print("---- TOTAL NUMBER OF STUDENTS----")
    student = int(input("Total number of student: "))
    return student


# ------------------------------ Add Student -------------------------------------

def add_student():
    print("-----ADD A STUDENT-----")
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


# ------------------------------ Add number of course -------------------------------------
def course_num():
    print("---- ADD NUMBER OF COURSE----")
    course = int(input("Total number of course: "))
    return


# Add course
def add_course():
    print("---- ADD A COURSE ----")
    cid = input("Course  ID: ")
    cname = input("Course name: ")
    cc = input("Course credit:")
    cr_o = {
        'cid': cid,
        'cname': cname,
        'cc': cc
    }
    Course.append(cr_o)
    CourseID.append(cid)


# ------------------------------ Create mark for students -------------------------------------
def create_mark():
    g = 1
    tu = len(Student)
    while g <= tu:
        g += 1
        mid = input("Student ID: ")
        if mid in Student:
            for i in range(0, len(CourseID)):
                nid = input("Course ID: ")
                if nid in CourseID:
                    mark = float(input("Student mark: "))
                    kk = {
                        'mid': mid,
                        'nid': nid,
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

    int = numpy.array([self.mark])
    null = numpy.array([self._c_Credit])
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
        strace.refresh()

        break


def gpa_sort():
    sortg = numpy.array([MarkGPA])
    sortg[::-1].sort()
    strace.addstr("GPA sorted %s: \n" % sortg)
    strace.refresh()


def show_list_student():
    print("----Student list----")
    for i in range(0, len(Student)):
        print(f"ID:{Student[i]['id']} name:{Student[i]['name']} DoB:{Student[i]['dob']}")


def show_list_course():
    print("----Course list----")
    for i in range(0, len(Course)):
        print(f"ID:{Course[i]['id']}  name : {Course[i]['name']}")


def show_mark():
    print("----Student mark list----")
    for i in range(0, len(Mark)):
        print(f"ID-course: {Mark[i]['b']} ID-Student: {Mark[i]['a']}  mark:{Mark[i]['mark']}")


# ------------------------------ Main -------------------------------------
s = int(student_num())
l = 1
while l <= s:
    l += 1
    add_student()
    show_list_student()

c = int(course_num())
p = 1
while p <= c:
    p += 1
    add_course()
    show_list_course()

# ------------------------------ GPA -------------------------------------
mark_gpa()


create_mark()
for i in range(0, len(Course)):
    ol = int(input("You choose: "))
    if ol == 1:
        print("--STUDENT MARK--")
        show_mark()
        break
    else:
        break