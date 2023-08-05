class MyClass:
    def __init__(self,name:str,year:int,month:str):
        self.name = name
        self.year = year
        self.month = month
        print("WELCOME TO OBJECT ORIENTED CODING")
    def study_plans(self):
        print(f"My name is {self.name} and Im going to USA on {self.month}-{self.year}")


#Create an object where we can able to access the methods in side the class
# det_name=MyClass()
# print(det_name.study_plans("Mahesh Kumar",2024,"December"))
# print(det_name.study_plans("Vidhya sagar",2026,"August"))
# print(det_name)---->object name

