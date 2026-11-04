# class CashPayment:
#     def pay(self, amount):
#         print("Paid",amount,"using cash")

# class UPIPayment:
#     def pay(self,amount):
#         print("Paid",amount,"using UPI")

# class CardPayment:
#     def pay(self,amount):
#         print("Paid",amount,"using Card")

# class NetBanking:
#     def pay(self,amount):
#         print("Paid",amount,"using NetBanking")

# choice=input("Choose payment method (cash/upi/card/netbanking):")
# if choice == "cash":
#     payment=CashPayment()
# elif choice == "upi":
#     payment=UPIPayment()
# elif choice == "Card":
#     payment=CardPayment()
# elif choice == "netbanking":
#     payment=NetBanking()
#     exit()

# payment.pay(10000)


class MobilePushNotification:
    def send(self,notification):
        print("Send Notification",notification,"by MobilePushNotification")

class Email:
    def send(self,notification):
        print("Send Notification",notification,"by Email")

class SMS:
    def send(self,notification):
        print("Send Notification",notification,"by SMS")

class WhatsApp:
    def send(self,notification):
        print("Send Notification",notification,"by WhatsApp")

choice=input("Choose notification method (MobilePushNotification/Email/SMS/WhatsApp):")
if choice == "Mobile":
    Send_Notification=MobilePushNotification()
elif choice == "Email":
    Send_Notification=Email()
elif choice == "SMS":
    Send_Notification=SMS()
elif choice == "WhatsApp":
    Send_Notification=WhatsApp()

Send_Notification.send("Your parcel has been shipped")