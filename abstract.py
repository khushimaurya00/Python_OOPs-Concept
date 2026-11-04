from abc import ABC,abstractmethod

class Payment(ABC): #parent abstract class
    @abstractmethod
    def pay(self,amount):
        pass

class CreditCard(Payment):
    def pay(self,amount):
        print("Paid",amount,"Using Credit Card")

class Cash(Payment):
    def pay(self,amount):
        print("Paid",amount,"Using Cash")

class DebitCard(Payment):
    def pay(self,amount):
        print("Paid",amount,"Using Debit Card")

class NetBanking(Payment):
    def pay(self,amount):
        print("Paid",amount,"Using Net Banking")

class UPI(Payment):
    def pay(self,amount):
        print("Paid",amount,"Using UPI")

class Cheque(Payment):
    def pay(self,amount):
        print("Paid",amount,"Using Cheque")

p1=UPI()
p1.pay(5000)

p2=Cash()
p2.pay(500)

p3=CreditCard()
p3.pay(900)

p4=DebitCard()
p4.pay(2000)

p5=Cheque()
p5.pay(50000)

p6=NetBanking()
p6.pay(9000)
# ---------------------------------------------------------------------------------------

from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

class Bike(Vehicle):
    def drive(self):
        print("Bike is moving")

class Car(Vehicle):
    def drive(self):
        print("Car is moving")

class Bus(Vehicle):
    def drive(self):
        print("Bus is moving")

class Cycle(Vehicle):
    def drive(self):
        print("Cycle is moving")

car=Car()
bike=Bike()
bus=Bus()
cycle=Cycle()
car.drive()
bike.drive()
bus.drive()
cycle.drive()
# -----------------------------------------------------------------------------------------

print("1: Bank Account")

from abc import ABC, abstractmethod

class BankAccount(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(BankAccount):
    def deposit(self, amount):
        print("Savings Account Deposit:", amount)

    def withdraw(self, amount):
        print("Savings Account Withdrawal:", amount)

class CurrentAccount(BankAccount):
    def deposit(self, amount):
        print("Current Account Deposit:", amount)

    def withdraw(self, amount):
        print("Current Account Withdrawal:", amount)

s = SavingsAccount()
c = CurrentAccount()

s.deposit(5000)
s.withdraw(1000)

c.deposit(10000)
c.withdraw(2000)
# --------------------------------------------------------------------------------------

print("2: Notification System")

from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print("Sending Email Notification")

class SMSNotification(Notification):
    def send(self):
        print("Sending SMS Notification")

class WhatsAppNotification(Notification):
    def send(self):
        print("Sending WhatsApp Notification")


e = EmailNotification()
s = SMSNotification()
w = WhatsAppNotification()

e.send()
s.send()
w.send()
# --------------------------------------------------------------------------

print("3: Institute Management")

from abc import ABC, abstractmethod

class Person(ABC):

    @abstractmethod
    def display_details(self):
        pass

class Student(Person):
    def display_details(self):
        print("Student Name: Khushi Maurya")
        print("Trade: AIPA")

class Teacher(Person):
    def display_details(self):
        print("Teacher Name: Mr. Shailesh Yadav")
        print("Subject: Python")

class Principal(Person):
    def display_details(self):
        print("Principal Name: Mr. Ajay Pal Singh")
        print("Institute: NSTIW Allahabad")

s = Student()
t = Teacher()
p = Principal()

print("Student Details:")
s.display_details()

print("Teacher Details:")
t.display_details()

print("Principal Details:")
p.display_details()
# ---------------------------------------------------------------------------------------------------

print("4: Math Methods ")

import math
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

c = Circle(5)
r = Rectangle(10, 4)
s = Square(6)

print("Area of Circle =", round(c.area(), 2))
print("Area of Rectangle =", r.area())
print("Area of Square =", s.area())