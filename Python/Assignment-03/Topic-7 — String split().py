# <------------------------------------------------------Question-33------------------------------------------------------------>

# text = "Python is easy"

# print(text.split())                          # Output --> ['Python', 'is', 'easy']


# <------------------------------------------------------Question-34------------------------------------------------------------>

# data = "apple,banana,mango"

# print(data.split(","))                       # Output --> ['apple', 'banana','mango']


# <------------------------------------------------------Question-35------------------------------------------------------------>

# text = "Python is easy"

# print(text.split(","))                       # Output --> ['Python', 'is', 'easy']

# Why does it not split at the spaces?
# Answer => Its because .split() is a string method in Python that breaks a string into multiple pieces and puts them into a list.


# <------------------------------------------------------Question-36------------------------------------------------------------>

# name = input("Enter your name: ")

# words = name.split()

# print(words[0])
# print(words[1])
# print(words[2])


# <------------------------------------------------------Question-37------------------------------------------------------------>

# name = input("Enter your name: ").strip()

# word = name.split()

# print("first_name: ",word[0].capitalize())
# print("first_name: ",word[1].capitalize())


# <------------------------------------------------------Question-38------------------------------------------------------------>

# name = (input("Enter any three number: "))

# words = name.split()

# num1 = int(words[0])
# num2 = int(words[1])
# num3 = int(words[2])

# print("The sum of the three no. is: ",num1 + num2 + num3)


# <------------------------------------------------------Question-39------------------------------------------------------------>

# info = input("Enter your details: ")

# words = info.split(",")

# print("Name: ",words[0])
# print("Age: ",words[1])
# print("Course: ",words[2])
# print("City: ",words[3])


# <------------------------------------------------------Question-40------------------------------------------------------------>

# email = input("Enter E-mail: ")

# words = email.split("@")

# print("Username: ",words[0])
# print("Domain: ",words[1])



# <------------------------------------------------------Question-41------------------------------------------------------------>

# inp= input("Enter Sentences: ")

# words = inp.split()

# print("First word: ",words[0])
# print("last word: ",words[-1])