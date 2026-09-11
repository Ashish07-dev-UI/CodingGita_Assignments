# <------------------------------------------------------Question-60------------------------------------------------------------>

# name = input("Student Name: ")
# a, b, c = input("Enter your English,Math,Computer marks: ").split()

# total = (int(a) + int(b) + int(c))
# avg = (int(a) + int(b) + int(c))/ 3

# print(f"Name: {name}")
# print(f"Avgerage: {avg}")
# print(f"Total: {total}")


# <------------------------------------------------------Question-61------------------------------------------------------------>

# details = input("Enter ID: ").split("-")

# print("Degree: ",details[0])
# print("Batch: ",details[1])
# print("Branch: ",details[2])
# print("Roll Number: ",details[3])


# <------------------------------------------------------Question-62------------------------------------------------------------>

# name = input("Enter Name: ").lower().split()

# print(name[0],end=".")
# print(name[2])


# <------------------------------------------------------Question-63------------------------------------------------------------>

# word = input("Enter any Sentence: ").split()

# print("First word: ",word[0])
# print("Last word: ",word[-1])


# <------------------------------------------------------Question-64------------------------------------------------------------>

# email = input("Enter you E-mail: ")

# print("@ Present:", "@" in email)

# parts = email.split("@")

# print("Username:", parts[0])
# print("Domain:", parts[1])


# <------------------------------------------------------Question-65------------------------------------------------------------>

# char = input("Enter a word: ")
# a = ord(char)
# b = a - 1
# c = a + 1

# print("Character: ",char)
# print("Code: ",a)
# print("Previous: ",chr(b))
# print("Next: ",chr(c))


# <------------------------------------------------------Question-66------------------------------------------------------------>

# prod_nam = input("Enter product name: ")
# cost = int(input("Enter Price: "))
# quantity = int(input("Enter quantity: "))
# discount = int(input("Enter discount: "))

# subtotal = (cost * quantity)
# total_discount = subtotal * discount / 100
# final_total = subtotal - discount

# print(f"Product: {prod_nam}")
# print(f"Price: {cost:.2f}")
# print(f"Quantity: {quantity}")
# print(f"Subtotal: {subtotal:.2f}")
# print(f"Discount: {discount:.2f}")
# print(f"Final Total: {final_total:.2f}")


# <------------------------------------------------------Question-67------------------------------------------------------------>

# date = input("Enter date: ").split("-")

# print("Day: ",date[0])
# print("Month: ",date[1])
# print("Year: ",date[2])


# <------------------------------------------------------Question-68------------------------------------------------------------>

# text = input()

# words = text.split()

# first = words[0]
# second = words[1]

# print("First Word:", first)
# print("Second Word:", second)
# print("First Word Reversed:", first[::-1])
# print("Second Word Reversed:", second[::-1])

# <------------------------------------------------------Question-69------------------------------------------------------------>

# student = input("Enter your details: ")

# parts = student.split("-")

# degree = parts[0]
# batch = parts[1]
# branch = parts[2]
# roll = parts[3]

# code = f"{degree}/{branch}/{roll}"

# print("Degree:", degree)
# print("Batch:", batch)
# print("Branch:", branch)
# print("Roll:", roll)
# print("Code:", code)


# <------------------------------------------------------Question-70------------------------------------------------------------>

# name = input("Enter Full Name :")

# words = name.split()

# first_name = words[0]
# last_name = words[-1]

# first_upper = first_name[:3].upper()
# last_lower = last_name[1:].lower()

# reversed_name = name[::-1]

# output = f"""Original: {name}
# First Name: {first_name}
# Last Name: {last_name}
# First Name (Upper Part): {first_upper}
# Last Name (Lower Part): {last_lower}
# Full Name Reversed: {reversed_name}"""

# print(output)
