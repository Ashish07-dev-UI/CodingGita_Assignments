##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Question-58 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# a,b,c,d = str(input("Enter your student ID: ")).lower().split("-")

# if c == "cse":
#     print("CSE Student")
# else:
#     print("Non-CSE Student")


##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Question-59 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# a,c = str(input("Enter your Email address: ")).split("@")

# if c == "gmail.com":
#     print("Gmail User")
# else:
#     print("Other Email Provider")


##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Question-60 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>







##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Question-61 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# num = int(input("Enter a positive num: "))

# if num>=0 and num<9:
#     print("One Digit")
# elif num>=10 and num<99:
#     print("Two Digit")
# elif num>=100 and num<999:
#     print("Three Digit")
# else:
#     print("Four or More Digits")




##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Question-62 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# price = int(input("Enter Price: "))
# quantity = int(input("Enter quantity: "))

# subtotal = price*quantity
# print("Subtotal",subtotal)

# final1 = subtotal*20/100
# final2 = subtotal*10/100

# if subtotal>= 5000:
#     print("Discount: 20%")
#     print("Final: ",subtotal-final1)
# elif subtotal>= 2000 and subtotal<5000:
#     print("Discount: 10%")
#     print("Final: ",subtotal-final2)
# else:
#     print("Discount: 0%")
#     print("Final: ",subtotal)




##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Question-63 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# units = int(input("Enter Electric Units: "))


# if units<=100:
#     print("Rate: ₹5")
#     print("Bill: ₹",units*5)
# elif units<=300 and units>100:
#     print("Rate: ₹7")
#     print("Bill: ₹",units*7)
# else:
#     print("Rate: ₹10")
#     print("Bill: ₹",units*10)




##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Question-64 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# menu = int(input("Enter your menu num: "))
# balance = 10000

# match menu:
#     case 1:
#         print("Balance: ",balance)
#     case 2:
#         deposit = int(input("Enter deposit amount: "))
#         print("Deposit Successful, Balance: ",balance+deposit)
#     case 3:
#         withdraw = int(input("Enter your withdraw amount: "))
#         if withdraw < balance:
#             print("Withdrawal Successful, Balance: ",balance-withdraw)
#         else :
#             print("Insufficient Balance")
#     case 4:
#         print("Exit")
#     case _:
#         print("Invalid Choice")


##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Question-65 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# num = int(input("Enter food num: "))
# quantity = int(input("Enter quantity: "))

# match num:
#     case 1:
#         total=quantity*250
#         print("Total: ",total)
#     case 2:
#         total=quantity*150
#         print("Total: ",total)
#     case 3:
#         total=quantity*200
#         print("Total: ",total)
#     case 4:
#         total=quantity*120
#         print("Total: ",total)

# if total >= 500:
#     discount=total*10/100
#     print("Discount: ",discount)
#     print("Final: ",total-discount)
# else:
#     print("Total: ",total)
#     print("Discount: 0")
#     print("Final: ",total)


##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Question-66 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# a = int(input("Enter 1st Subject Marks: "))
# b = int(input("Enter 2nd Subject Marks: "))
# c = int(input("Enter 3rd Subject Marks: "))

# attendence = int(input("Enter your attendence: "))

# total = a + b + c
# avg = total / 3

# if attendence>=75:
#     if avg>=90:
#         print("Outstanding")
#     elif avg>=75 and avg<90:
#         print("Very Good")
#     elif avg>=60 and avg<75:
#         print("Good")
#     elif avg>=45 and avg<60:
#         print("Pass")
#     else:
#         print("Fail")
# else:
#     print("Not Eligible")




##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Question-67 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# dist = int(input("Enter Distance in KM: "))
# ride = str(input("Enter ride type: ")).lower().strip()

# normal = 15
# premimum = 25

# n = dist*normal
# p = dist*premimum

# match ride:
#     case "normal":
#         if dist>=20:
#             extra = n*10/100
#             print("Fare: ",n+extra)
#         else:
#             print("Fare: ",n)
#     case "premimum":
#         if dist>=20:
#             extra = p*10/100
#             print("Fare: ",p+extra)
#         else:
#             print("Fare: ",p)


##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Question-68 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# entrance = int(input("Enter Entrance Exam Score: "))
# perc = int(input("Enter 12th percentage in num: "))
# category = str(input("Enter category: "))

# match category:
#     case "general":
#         if entrance>=80 and perc>=75:
#             print("Admission Eligible")
#         else:
#             print("Admission Not Eligible")
#     case "obc":
#         if entrance>=70 and perc>=70:
#             print("Admission Eligible")
#         else:
#             print("Admission Not Eligible")
#     case "sc":
#         if entrance>=60 and perc>=60:
#             print("Admission Eligible")
#         else:
#             print("Admission Not Eligible")



