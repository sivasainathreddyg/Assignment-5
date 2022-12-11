class Student:

    def setName(self,__name):
        self.__name=__name
    def getName(self):
        return self.__name
    def setRollNumber(self,__rollnumber):
        self.__rollnumber=__rollnumber
    def getRollNumber(self):
        return self.__rollnumber
student=Student()
student.setName("siva")
student.setRollNumber("30")
print(student.getName())
print(student.getRollNumber())
