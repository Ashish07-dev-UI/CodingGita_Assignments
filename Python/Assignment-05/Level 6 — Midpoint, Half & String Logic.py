# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-45  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

x = input("Enter a string: ")

for i in range(len(x)):
    if i == (len(x) // 2):
        print(x[i])


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-46  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

x = input("Enter a string: ")
a = ""
b = ""

for i in range(len(x)):
    if i < (len(x) // 2):
        a = a + x[i]
    else:
        b = b + x[i]

print("First Half:", a)
print("Second Half:", b)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-47  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

x = input("Enter a string: ")
a = ""
m = ""
b = ""

for i in range(len(x)):
    if len(x) % 2 != 0:
        if i < (len(x) // 2):
            a = a + x[i]
        elif i == (len(x) // 2):
            m = x[i]
        else:
            b = b + x[i]
    else:
        if i < (len(x) // 2):
            a = a + x[i]
        else:
            b = b + x[i]

if len(x) % 2 != 0:
    print("First Half:", a)
    print("Middle:", m)
    print("Second Half:", b)
else:
    print("First Half:", a)
    print("Second Half:", b)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-48  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

x = input("Enter a string: ")
a = ""
b = ""

for i in range(len(x)):
    if i < (len(x) // 2):
        a = a + x[i]
    else:
        b = b + x[i]

if a == b:
    print("Equal Halves")
else:
    print("Different Halves")


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-49  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

x = input("Enter a string: ")
s = True

for i in range(len(x)):
    if x[i] != x[len(x) - 1 - i]:
        s = False

if s == True:
    print("Symmetric")
else:
    print("Not Symmetric")


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-50  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

x = input("Enter a string: ")
r = ""

for i in range(len(x)):
    if i % 2 == 0:
        r = r + x[i]

print(r)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-51  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

x = input("Enter a string: ")
e = 0
o = 0

for i in range(len(x)):
    if i % 2 == 0:
        e = e + 1
    else:
        o = o + 1

print(f"Even Index = {e}, Odd Index = {o}")


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-52  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

x = input("Enter a string: ")
r = ""

for i in range(len(x)):
    if i % 2 == 0:
        r = r + x[i + 1]
    else:
        r = r + x[i - 1]

print(r)