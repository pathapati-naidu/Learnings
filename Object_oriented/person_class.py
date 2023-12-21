import math
class Person:
    total_marks=1000
    all=[]
    def __init__(self,name:str,marks:int):
        self.name=name
        self.marks_obtained=marks
        Person.all.append(self)
    
    def get_percentage(self):
        Value=((self.marks_obtained)/(self.total_marks))*100
        return f"{self.name}'S Percentage is {math.floor(Value)}%"
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name})"
        
class Student(Person):
    def __init__(self, name: str, marks: int,total_subjects):
        super().__init__(name, marks)
        self.subjects=total_subjects
        # self.all.append(self)


stud_obj=Student("Anil Kumar",700,6)
print(stud_obj.get_percentage())
print(Student.all)