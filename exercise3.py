# student management 

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.average = 0
        self.status = "PENDING"
        

    def add_marks(self,num1, num2, num3, num4, num5):
        self.maths = num1
        self.physics = num2
        self.chemistry = num3
        self.hindi = num4
        self.english = num5
        self.calc_average()

    def calc_average(self):
        self.average = (self.maths + self.physics + self.chemistry + self.hindi + self.english)/5
        if self.average > 40:
            self.status = "PASS"

        else:
            self.status = "FAIL"

    def result(self):
        print(f"Name: {self.name}\n"
              f"Roll NO. : {self.roll_no}\n"
              f"Result: {self.status}\n"
              f"Average: {self.average}")
        
student1 = Student("harsha", 1234)
student1.add_marks(80,95,85,94,97)
student1.result()


student2 = Student("rahul", 4567)
student1.add_marks(20,45,35,14,27)
student1.result()