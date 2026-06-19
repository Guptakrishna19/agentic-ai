class Courses:
    def __init__(self,c_name,c_id):
        self.c_name =c_name 
        self.c_id =c_id 

    def display(self):
        print(f"Name: {self.c_name}, ID: {self.c_id}")

class Student:
    def __init__(self,name,__id):
        self.name =name 
        self.__id= __id
        self.skills =[]
        self.courses=[]

    def add_skill(self, skill):
        self.skills.append(skill)
    
    def add_course(self,course):
        self.courses.append(course)

    def display(self):
        print("Student found!!!")
        print(f"Name: {self.name}, ID: {self.__id}, Skills: {self.skills}")

        print("Courses of the student: ")
        for c in self.courses:
            c.display()


## create courses

course1=Courses("Python","C001")
course2=Courses("AI","C002")
course3=Courses("DSA","C003")

## Add skills

student1=Student("Harish","I041")
student1.add_skill("Python")
student1.add_skill("AI")
student1.add_skill("DSA")

student2=Student("Mihir","I066")
student2.add_skill("Python")
student2.add_skill("SQL")
student2.add_skill("ML")

student3=Student("Parth","I044")
student3.add_skill("Python")
student3.add_skill("Java")
student3.add_skill("ML")

student1.add_course(course1)
student1.add_course(course2)

student2.add_course(course1)

student3.add_course(course2)
student3.add_course(course3)

students=[student1,student2,student3]

for student in students:
    student.display()