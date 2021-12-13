class RegisterCourse:
    def __init__(self):
        self.name = "Mustafa"
        self.surname = "Kapucu"
        self.__exam1 = 74
        self.__exam2 = 80
        self.courses = []

    def __add(self, course):
        self.courses.append(course)

    def getExam1(self):
        return self.__exam1

    def setExam1(self, newVal):
        self.__exam1 = newVal


course = RegisterCourse()
course.setExam1(100)
print(course.getExam1())
