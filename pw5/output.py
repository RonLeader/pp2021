import numpy

def listCourses(courses):
    print("Course List:")
    for c in courses:
        c.describe()


def listStudents(students):
    print("Student List:")
    for s in students:
        s.describe()

def showMarks(studentMarks):
    courseName = input("Enter course's name to show marks: ")
    print("Student Marks for " + courseName)
    for studentMark in studentMarks:
        if courseName == studentMark.get_Course().get_Name():
            studentMark.describe()

def calculateAvg(id, studentMarks):
    marks = []
    for studentMark in studentMarks:
        if (studentMark.get_Student().get_ID() == id):
            marks.append(studentMark.get_Mark())
    return numpy.average(marks)



def showAvarage(students):
    id = input("Enter student's ID: ")
    for s in students:
        if id == s.get_ID():
            print("Name: " + s.get_Name() + " Avg: " + str(s.get_Avg()))

def sortbyAvg(students):
    sortedList = sorted(students, key=lambda x: x.get_Avg(), reverse=True)
    for s in sortedList:
        s.describe()

def calculateWeightedSum(id, courses, studentMarks):
    sum = 0
    for c in courses:
        smark = []
        warray = []
        for studentMark in studentMarks:
            if (studentMark.get_Student().get_ID == id):
                smark.append(studentMark.get_Mark())
                warray.append(c.etc)
        weights = numpy.array(warray)
        amark = numpy.array(smark)
        sum = sum + numpy.sum(numpy.dot(amark, weights))
    return sum

def showWeightedSum(courses, studentMarks):
    id = input("Input student id: ")
    print("Weighted sum: " + str(calculateWeightedSum(id, courses, studentMarks)))