
class StudentMark:
    def __init__(self, student, course, mark):
        self.__student = student
        self.__course = course
        self.__mark = mark

    def get_Student(self):
        return self.__student

    def get_Course(self):
        return self.__course

    def get_Mark(self):
        return self.__mark

    def describe(self):
        print(self.__student.get_ID() + " " + self.__student.get_Name() + " "
              + self.__course.get_Name() + " " + str(self.__mark))