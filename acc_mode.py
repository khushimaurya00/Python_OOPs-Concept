# Access modifier

# class student:
#     def __init__(self):
#         self.name="Khushi"
#         self._trade="AIPA"
#         self.__marks=90

#     def show_marks(self):
#         return self.__marks

# std=student()


# print(std.name)
# print(std._trade)
# print(std.show_marks())


class Bank_Account:
    def __init__(self,account_name,balance):
        self.account_name=account_name
        self.__balance=balance

    def deposite(self,amount):
        if amount >0:
            self.__balance+= amount
            print("Deposite_Successfully")
        else:
            print("Invalid_Balance")

    def withdrawl(self,amount):
        if amount <=0:
            print("Invalid_Amount")
        elif amount <=self.__balance:
            self.__balance -=amount
            print("withdrawl successful")
        else:
            print("Insufficiet Amount")

    def check_balance(self):
           print("Current_Balance",self.__balance)

user1=Bank_Account("Khushi",1000)
print(user1.account_name)
user1.deposite(0)
user1.withdrawl(1200)
user1.check_balance()

user2=Bank_Account("Arsh",0)
print(user2.account_name)
user2.deposite(500)
user2.withdrawl(12000)
user2.check_balance()
