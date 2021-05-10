
import input as inp
import output

students = []
studentMarks = []
courses = []

def menu():
    choice = "-1";
    while (choice != "0"):
        print("""
                   MENU
            1. Add students
            2. Add courses
            3. Add marks
            4. Show student list
            5. Show course list
            6. Show mark list
            7. Calculate average score
            8. Calculate weighted sum
            9. Sort student list
            0. Exit
            """)
        choice = input("Enter your choice: ")
        if (choice == "1"):
            inp.add_student(students)
        elif (choice == "2"):
            inp.add_course(courses)
        elif (choice == "3"):
            inp.add_mark(courses, students, studentMarks)
        elif (choice == "4"):
            output.listStudents(students)
        elif (choice == "5"):
            output.listCourses(courses)
        elif (choice == "6"):
            output.showMarks(studentMarks)
        elif (choice == "7"):
            output.showAvarage(students)
        elif (choice == "8"):
            output.showWeightedSum(courses, studentMarks)
        elif (choice == "9"):
            output.sortbyAvg(students)

if __name__ == '__main__':
    menu()