"""class Car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def display(self):
        print("My car is a",self.color,self.brand)
c1=Car("Toyota","Red")
c2=Car("Honda","Blue")
c1.display()
c2.display()"""

"""class Student:
    def __init__(self,name,marks,age):
        self.name=name
        self.marks=marks
        self.age=age
    def grade(self):
        if self.marks>=90:
            print(self.name,"got an A grade")
        elif self.marks>=75:
             print(self.name,"got B grade")
        else:
             print(self.name,"got a C grade")
s1=Student("Anu",92)
s2=Student("Rahul",80)
s3=Student("Meera",60)
s1.grade()
s2.grade()
s3.grade()"""

class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def grade(self):
        if self.marks>=90:
            print(self.name,self.age,"years old got an A grade")
        elif self.marks>=75:
             print(self.name,self.age,"years old got B grade")
        else:
             print(self.name,self.age,"years old got a C grade")
s1=Student("Anu",18,92)
s2=Student("Rahul",19,80)
s3=Student("Meera",20,60)
s1.grade()
s2.grade()
s3.grade()
            
