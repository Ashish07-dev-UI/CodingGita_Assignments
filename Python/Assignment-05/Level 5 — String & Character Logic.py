# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-37  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

x = input("Enter a string: ")
i = 0

for ch in x:
    print(i, ch)
    i = i + 1


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-38  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

x = input("Enter a string: ")
c = 0

for ch in x:
    c = c + 1

print(c)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-39  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

x = input("Enter a string: ")
v = 0
c = 0

for ch in x:
    if ch != " ":
        if ch in "aeiouAEIOU":
            v = v + 1
        else:
            c = c + 1

print(f"Vowels = {v}, Consonants = {c}")


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-40  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

x = input("Enter a string: ")
t = input("Enter a target char: ")
c = 0

for ch in x:
    if ch == t:
        c = c + 1

print(c)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-41  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

x = input("Enter a string: ")
t = input("Enter a target char: ")

p = -1
i = 0

for ch in x:
    if ch == t and p == -1:
        p = i
    i = i + 1

if p == -1:
    print("Not Found")
else:
    print(p)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-42  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

x = input("Enter a string: ")
u = 0
l = 0

for ch in x:
    if ch >= 'A' and ch <= 'Z':
        u = u + 1
    elif ch >= 'a' and ch <= 'z':
        l = l + 1

print(f"Uppercase = {u}, Lowercase = {l}")


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-43  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

x = input("Enter a string: ")

for ch in x:
    print(ch, ord(ch))


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-44  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

x = input("Enter a string: ")
r = ""

for ch in x:
    if ch not in "aeiouAEIOU":
        r = r + ch

print(r)