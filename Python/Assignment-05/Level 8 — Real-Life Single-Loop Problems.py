# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-62  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

n = int(input("Enter number of days: "))
t = 0
h = -1
l = -1

for i in range(n):
    e = int(input("Expense: "))
    t = t + e
    if i == 0:
        h = e
        l = e
    else:
        if e > h:
            h = e
        if e < l:
            l = e

print(f"Total: {t}")
print(f"Highest: {h}")
print(f"Lowest: {l}")


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-63  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

n = int(input("Enter number of subjects: "))
t = 0
h = -1
l = -1

for i in range(n):
    m = int(input("Mark: "))
    t = t + m
    if i == 0:
        h = m
        l = m
    else:
        if m > h:
            h = m
        if m < l:
            l = m

a = t / n
print(f"Total: {t}")
print(f"Average: {a}")
print(f"Highest: {h}")
print(f"Lowest: {l}")


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-64  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

n = int(input("Enter number of days: "))
p = 0
a = 0

for i in range(n):
    s = input("Status (P/A): ")
    if s == 'P' or s == 'p':
        p = p + 1
    else:
        a = a + 1

pct = (p / n) * 100
print(f"Present: {p}")
print(f"Absent: {a}")
print(f"Attendance: {round(pct, 2)}%")


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-65  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

n = int(input("Enter number of days: "))
t = 0
c = 0

for i in range(n):
    u = int(input("Units: "))
    t = t + u
    if u > 10:
        c = c + 1

print(f"Total Units: {t}")
print(f"Days Above 10: {c}")


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-66  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

n = int(input("Enter number of products: "))
t = 0
c = 0

for i in range(n):
    p = int(input("Price: "))
    t = t + p
    if p > 1000:
        c = c + 1

print(f"Total Bill: {t}")
print(f"Products Above 1000: {c}")


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-67  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

n = int(input("Enter number of attempts: "))
s = 0
f = 0

for i in range(n):
    a = input("Attempt (success/failed): ")
    if a == "success":
        s = s + 1
    else:
        f = f + 1

pct = (s / n) * 100
print(f"Successful: {s}")
print(f"Failed: {f}")
print(f"Success Rate: {round(pct, 1)}%")