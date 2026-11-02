class Aipa:
    def __init__(self,name,roll_no,trade,marks): #__init__= constructor
        self.name=name
        self.roll_no=roll_no
        self.trade=trade
        self.marks=marks

std1=Aipa("Khushi","1","AIPA",90)
std2=Aipa("Arsh",2,"AIPA",90)

print(std1.name)
print(std1.roll_no)
print(std1.trade)
print(std1.marks)

print(std2.name)
print(std2.roll_no)
print(std2.trade)
print(std2.marks)

class Student:
    def __init__(self,name,roll_no,trade,marks): #__init__= constructor
        self.name=name
        self.roll_no=roll_no
        self.trade=trade
        self.marks=marks
        
    def display_details(self):
        print("Name",self.name)
        print("Roll_no",self.roll_no)
        print("Trade",self.trade)
        print("Marks",self.marks)

    def check_result(self):
        if self.marks >=40:
            print("Pass")
        else:
            print("Fail")

    def percentage(self,total_marks):
        return (self.marks/total_marks)*100

student1=Student("Khushi",1,"AIPA",89)
student2=Student("Arsh",2,"COPA",90)

student1.display_details()
student1.check_result()
print(student1.percentage(100),"%")

student2.display_details()
student2.check_result()
print(student2.percentage(100),"%")

class Car:
    def __init__(self,name,model,color,price,speed): #__init__= constructor
        self.name=name
        self.model=model
        self.color=color
        self.price=price
        self.speed=speed
        
    def display_details(self):
        print("Name:",self.name)
        print("Model:",self.model)
        print("Color:",self.color)
        print("Price:",self.price)
        print("Speed:",self.speed)

    def check_price(self):
        if self.price >=1000000:
            print("Expensive Car")
        else:
            print("Affordable Car")

    def check_speed(self):
        if self.speed >=100:
            print("Highest Spped")
        elif self.speed >=80:
            print("Average Speed Car")
        else:
            print("Low Speed Car")

    def discount(self,discount_percentage):
        return self.price - (self.price*discount_percentage/100)

Car1=Car("BMW","X5","White",5000000,110)
Car2=Car("THAR","Mahindra Thar","Blue",150000,160)

Car1.display_details()
Car1.check_price()
Car1.check_speed()
print("price after discount:",Car1.discount(10))

Car2.display_details()
Car2.check_price()
Car2.check_speed()
print("price after discount:",Car2.discount(20))