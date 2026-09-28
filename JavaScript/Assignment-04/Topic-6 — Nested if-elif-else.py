##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Question-44 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # a = int(input("Enter 1st num: "))
# # b = int(input("Enter 2nd num: "))
# # c = int(input("Enter 3rd num: "))

# # if a>=b and a>=c:
# #     if a==b:
# #         print("A and B are Equal and Greatest")
# #     elif a==c:
# #         print("A and C are Equal and Greatest")
# #     else:
# #         print("A is Greatest")
# # elif b>=a and b>=c:
# #     if b==a:
# #         print("A and B are Equal and Greatest")
# #     elif b==c:
# #         print("B and C are Equal and Greatest")
# #     else:
# #         print("B is Greatest")
# # elif c>=a and c>=b:
# #     if c==a:
# #         print("A and C are Equal and Greatest")
# #     elif c==b:
# #         print("B and C are Equal and Greatest")
# #     else:
# #         print("C is Greatest")
# # else:
# #     print("All are Equal")


# a = int(input("Enter 1st num: "))
# b = int(input("Enter 2nd num: "))
# c = int(input("Enter 3rd num: "))

# if a == b == c:
#     print("All are Equal")
# elif a >= b and a >= c:
#     if a == b:
#         print("A and B are Equal and Greatest")
#     elif a == c:
#         print("A and C are Equal and Greatest")
#     else:
#         print("A is Greatest")
# elif b >= a and b >= c:
#     if b == c:
#         print("B and C are Equal and Greatest")
#     else:
#         print("B is Greatest")
# else:
#     print("C is Greatest")




##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Question-45 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# attendence = int(input("Enter your attendence: "))
# marks = int(input("Enter your marks: "))

# if attendence>=75:
#     if marks>=90:
#         print("A")
#     elif marks>=75 and marks<90:
#         print("B")
#     elif marks>=60 and marks<75:
#         print("C")
#     elif marks>=40 and marks<60:
#         print("D")
#     else:
#         print("F")
# else:
#     print("Not Eligible")



##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Question-46 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# salary = int(input("Enter your salary: "))
# rating = int(input("Enter your ratings: "))

# if salary >= 30000:
#     if rating ==5 :
#         print("Bonus: 20%")
#     elif rating ==4 :
#         print("Bonus: 15%")
#     elif rating ==3 :
#         print("Bonus: 10%")
#     else:
#         print("Bonus: 5%")
# else:
#     print("Not Eligible for Bonus")


##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Question-47 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# age = int(input("Enter your age: "))
# distance = int(input("Enter your distance in KM: "))

# if age==5:
#     print("Free")
# elif age>5 and age<=59:
#     print("Regular")
#     if distance<=10:
#         print("Short Distance")
#     else:
#         print("Long Distance")
# else:
#     print("Senior")


##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Question-48 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# stock = int(input("Enter your stock: "))
# payment = str(input("Enter your payment status: ")).lower()

# if stock > 0 :
#     if payment=="paid":
#         print("Order Confirmed")
#     elif payment=="pending":
#         print("Payment Pending")
#     else:
#         print("Invalid Payment Status")
# else:
#     print("Out of Stock")


##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Question-49 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# age = int(input("Enter your age: "))
# ticket = str(input("Enter your ticket type: "))

# if age<=5:
#     print("Free Travel")
# elif age>= 5 and age<60:
#     print("Regular Passenger")
#     if ticket=="ac":
#         print("AC Ticket")
#     elif ticket=="sleeper":
#         print("Sleeper Ticket")
#     else:
#         print("Invalid Ticket Type")
# else:
#     print("Senior Passenger")