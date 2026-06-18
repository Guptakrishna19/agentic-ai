class Student:
    def __init__(self,name,__id,skills):
        self.name =name 
        self.__id= __id
        self.skills = skills

    def add_skill(self, skill):
        self.skills.append(skill)

    def display(self):
        print("Student found!!!")
        print(f"Name: {self.name}, ID: {self._id}, Skills: {self.skills}")


    
student1=Student("Harish","I041",[])
student1.add_skill("Python")
student1.add_skill("AI")
student1.add_skill("DSA")

student2=Student("Mihir","I066",[])
student2.add_skill("Python")
student2.add_skill("SQL")
student2.add_skill("ML")

student3=Student("Parth","I044",[])
student3.add_skill("Python")
student3.add_skill("Java")
student3.add_skill("ML")

students=[student1,student2,student3]

# for student in students:
#     student.display()

def find_student_by_id(__id):
    for student in students:
        if student.__id==__id:
            return student
    return None
try:
    __id=input ("Enter student_id: ")
    result=find_student_by_id(__id)
    result.display()
except AttributeError:
    print(f"no student found with this id: {__id}")