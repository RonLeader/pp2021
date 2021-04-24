"""
:Author: Dao Trong Le Thai
:ID: BA9-055
:Lab work: 2
"""
# ------------------------------ Student -------------------------------------
class Student:

    def __init__(self, name, s_id, dob):
        self._st_Name = name
        self._st_ID = s_id
        self._st_DoB = dob

    def set_st_name(self, name):
        self._st_Name = name

    def set_st_id(self, std_id):
        self._st_ID = std_id

    def set_st_dob(self, dob):
        self._st_DoB = dob

    def get_st_name(self):
        return self._st_Name

    def get_st_id(self):
        return self._st_ID

    def get_st_dob(self):
        return self._st_DoB

# ------------------------------ Course -------------------------------------
class Course:
    def __init__(self, name, c_id):
        self._name = name
        self._id = c_id

    def set_c_name(self, name):
        self._name = name

    def set_c_id(self, c_id):
        self._id = c_id

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

# ------------------------------ Student Management -------------------------------------
class STManangement:
    _st_Name = ""
    _crs_Inf = {}

    def __init__(self):
        pass

    def set_inf(self, name, course_inf):
        self._st_Name = name
        self._crs_Inf = course_inf

    def set_st_name(self, student_name):
        self._st_Name = student_name

    def get_st_name(self):
        return self._st_Name

    def set_crs_inf(self, dic_inf):
        self._crs_Inf = dic_inf

    def get_crs_inf(self):
        return self._crs_Inf


# ------------------------------ Database -------------------------------------
st_list = [Student("T", "T", "T")]
course_list = [Course("T", "T")]
stm_list = [STManangement()]

st_list.clear()
course_list.clear()
stm_list.clear()

count_smm = 0


# ------------------------------ Method -------------------------------------


def input_domain(value, min_value, max_value):
    while value < min_value or value > max_value:
        value = int(input("Your input is invalid! Enter again: "))
    return value


def quit_menu():
    global option
    print("---------------------End of this choice---------------------")
    option = int(input("Make other choice, 0 to quit: "))
    option = input_domain(option, 0, 6)
    if option == 0:
        print("You choose quit!")


def option1():
    global i
    num_of_st = int(input("Number of student in the class: "))
    for i in range(0, num_of_st):
        name = str(input("Student name: "))
        s_id = str(input("Student ID: "))
        dob = str(input("Student DoB: "))
        st_list.append(Student(name, s_id, dob))


def option2():
    global i
    num_of_cour = int(input("Number of course: "))
    for i in range(0, num_of_cour):
        c_name = str(input("Course name: "))
        c_id = str(input("Course id: "))
        course_list.append(Course(c_name, c_id))


def option3():
    global option, i, count_smm
    name = str(input("Name of student you want to manage: "))
    cour_inf_lit = {}
    if checkStList(name):
        stm_list.append(STManangement())
        stm_list[count_smm].set_st_name(name)
        num_of_cour = int(input("Number of courses this student studied: "))
        for i in range(0, num_of_cour):
            c_name = input("N1ame of course: ")
            if checkCourseList(c_name):
                mark = int(input("Mark of this course: "))
                cour_inf_lit[c_name] = mark
                stm_list[count_smm].set_crs_inf(cour_inf_lit)
            else:
                print("Input course did not import.")
        count_smm = count_smm + 1
    else:
        option = int(input("Input wrong ! Press 3 to do again, 0 to quit: !"))


def checkStList(name):
    global i

    check = False
    for i in st_list:
        if name == i.get_st_name():
            check = True
    return check


def checkCourseList(c_name):
    global i
    for i in course_list:
        if i.get_name() == c_name:
            return True


# ------------------------------ Menu -------------------------------------
print("Program started !!!")

def menu_option():
    print("1. Set information of student: \n"
          "2. Set information of course: \n"
          "3. Set mark for student by course:\n"
          "4. Get information of student: \n"
          "5. Get information of course: \n"
          "6. Get information for student course management:\n"
          "0. Quit.")

menu_option()
option = int(input("Enter your choice: "))

while option != 0:
    if option == 1:
        option1()
        quit_menu()

    elif option == 2:
        option2()
        quit_menu()

    elif option == 3:
        option3()
        quit_menu()

    elif option == 4:
        print("All information of student in class: ")
        for i in st_list:
            print("Student's name = " + i.get_st_name(), end=". ID = ")
            print(i.get_st_id(), end=". DoB = " + i.get_st_dob())
            print()
        quit_menu()

    elif option == 5:
        print("All information of course: ")
        for i in course_list:
            print("Course's name = " + i.get_name(), end=". ID = ")
            print(i.get_id())
        quit_menu()

    elif option == 6:
        for i in stm_list:
            print("This is mark information of " + i.get_st_name() + ": ", end="")
            print(i.get_crs_inf())
        quit_menu()

    else:
        print("You choose quit!")
        break