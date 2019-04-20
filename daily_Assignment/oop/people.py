class Person:
    def __init__(self, name='', age=0, department=''):
        self.name = name
        self.age = age
        self.dp = department


class Student:
    # advisor = ''

    def __init__(self, name='', age=0, department='', id=0, GPA=1.0):
        Person.__init__(self, name=name, age=age, department=department)
        self.id = id
        self.GPA = GPA

    def reg_advisor(self, x):
        self.advisor = x.name

    def print_info(self):
        print("제 이름은 %s, 나이는 %d, 학과는 %s, 지도교수님은 %s 입니다." % (self.name, self.age, self.dp, self.advisor))


class Professor:
    student = list()

    def __init__(self, name='', age=0, department='', position='', laboratory=''):
        Person.__init__(self, name=name, age=age, department=department)
        self.position = position
        self.laboratory = laboratory

    def reg_student(self, stu):
        self.student.append(stu.name)

    def print_info(self):
        # print("제 이름은 %s, 나이는 %d, 학과는 %s, 지도학생은 %s, 입니다."%(self.name, self.age, self.dp, self.student))
        print("제 이름은 {}, 나이는 {}, 학과는 {}, 지도학생은 {},{} 입니다." .format(self.name, self.age, self.dp, self.student[0], self.student[1]))


stu1 = Student('Kim', 30, 'Computer', 20001234, 4.5)
stu2 = Student('Lee', 22, 'Computer', 20101234, 0.5)
prof1 = Professor('Lee', 55, 'computer', 'Full', 'KLE')

stu1.reg_advisor(prof1)
stu2.reg_advisor(prof1)

prof1.reg_student(stu1)
prof1.reg_student(stu2)

stu1.print_info()
stu2.print_info()
prof1.print_info()