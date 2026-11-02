# Encapsulation
print("1.) Encapsulation")
class employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def inc_salary(self, amount):
        if amount >0:
            self.__salary += amount
            print("Salary updated")
        else:
         print("Invalid amount")

emp=employee("Khushi",25,50000)
print("Salary:",emp.get_salary())

emp.inc_salary(8000)
print("New Balance:",emp.get_salary())

# -----------------------------------------------------------------
# Single Inheritance
print("2.) Single Inheritance")
class Animal():
    def property(self):
        print("Animal has 4 legs")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d=Dog()
d.property()
d.bark()

# ------------------------------------------------------------------
# Multiple Inheritance
print("3.) Multiple Inheritance")
class Father():
    def skills1(self):
        print("Driving")

class Mother():
    def skill2(self):
        print("Cooking")

class Child(Father,Mother):
    def Qualities(self):
        print("Inherited skills from parents:")


x=Child()
x.Qualities()
x.skills1()
x.skill2()
# ------------------------------------------------------------------

# Multilevel inheritance
print("4.) Multilevel Inheritance")
class Grandfather():
    def house(self):
        print("Grandfather's house")

class Father(Grandfather):
    def bike(Self):
        print("Father's bike")

class Son(Father):
    def laptop(self):
        print("Son's Laptop")

class Grandson(Son):
    def car(self):
        print("Grandson's car")


g=Grandson()
g.house()
g.bike()
g.laptop()
g.car()
# ------------------------------------------------------------------

# Hierarchical Inheritance
print("5.) Hierarchal Inheritance")
class Institute():
    def name(self):
        print("NSTIW Allahabad")

class Teacher(Institute):
    pass
class Student(Institute):
    pass
class Housekeeping(Institute):
    pass

t=Teacher()
s=Student()
h=Housekeeping()

s.name()
t.name()
h.name()