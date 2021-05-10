
class Student:
    def __init__(self, id, name, dOB):
        self.__id = id
        self.__name = name
        self.__dOB = dOB

    def describe(self):
        print(self.__id + " " + self.__name + " " + self.__dOB)

    def get_ID(self):
        return self.__id

    def get_Name(self):
        return self.__name

    def get_Avg(self):
        return self.__avg

    def set_Avg(self, avg):
        self.__avg = avg