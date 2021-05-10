
class Course:
    def __init__(self, id, name, etc):
        self.__id = id
        self.__name = name
        self.__etc = etc

    def describe(self):
        print("Id: " + self.__id + " Course name: " + self.__name + " etc: " + self.__etc)

    def getName(self):
        return self.__name