class Student:

    college = "LNCT"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def get_clg(cls):
        return cls.college
    
    def info():
        print("this is student class")

s1 = Student(33,45,67)
s2 = Student(37,38,39)     

print(s1.avg())
print(Student.get_clg())