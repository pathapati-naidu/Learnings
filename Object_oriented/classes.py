class MyClass:
    def __init__(self,name:str,year:int,month:str,date:str,age:int,country:str,domain:str):
        self.name = name
        self.year = year
        self.month = month
        self.age=age
        self.country=country
        self.date=date
        self.domain=domain
    def study_plans(self):
        print(f"My name is {self.name} and Im going to USA on {self.date}/{self.month}/{self.year}")
        if self.year<2025:
            print("Best option you have opted to go there and do the education Now")
    def alternative_plans(new):
        if new.year>2025:
            print(f"{new.name} please go for switching the job roles it may offer you around 17 LPA")
        else:
            print(f"{new.name} you did it never stop working hard for your goal it may take time but you will achieve what you want")
    def create_dict(self):
        new_dict={
            "Name":self.name,
            "Age":self.age,
            "Country":self.country
        }

        #Extracting the keys in the dictionary
        print(new_dict.keys())

        #Extracting the values in the dictionary
        print(new_dict.values())

        #Extracting the keys & Values in the dictionary using the items()
        for i,j in new_dict.items():
            print(f"{i}:{j}")

        #Copying the dictionaries 1.copy() 2.dict()
        temp_dict=new_dict.copy()
        print("Original Dictionary :",new_dict)

        #Updating the dictionary with the new keys & values
        temp_dict.update({
            "Domain ":self.domain
        })
        print("Temp dictionary after copying :",temp_dict)
        new_dict=dict(temp_dict)

        new_dict.popitem()
        new_dict.pop("Country")
        print(new_dict)





#Create an object where we can able to access the methods in side the class
# det_name=MyClass()
# print(det_name.study_plans("Mahesh Kumar",2024,"December"))
# print(det_name.study_plans("Vidhya sagar",2026,"August"))
# print(det_name)---->object name
