# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-23  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

n = int(input("Enter a num: "))
count = 0

if n == 0:
    count = 1

for i in range(1, n+1):
    if n > 0:
        count = count + 1
        n = n // 10

print(count)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-24  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

n = int(input("Enter a num: "))
total = 0

for i in range(1, n+1):
    if n > 0:
        total = total + (n % 10)
        n = n // 10

print(total)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-25  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

n = int(input("Enter a num: "))
product = 1

if n == 0:
    product = 0

for i in range(1, n+1):
    if n > 0:
        product = product * (n % 10)
        n = n // 10

print(product)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-26  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

n = int(input("Enter a num: "))
count = 0

if n == 0:
    count = 1

for i in range(1, n+1):
    if n > 0:
        if (n % 10) % 2 == 0:
            count = count + 1
        n = n // 10

print(count)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-27  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

n = int(input("Enter a num: "))
total = 0

for i in range(1, n+1):
    if n > 0:
        digit = n % 10
        if digit % 2 == 0:
            total = total + digit
        n = n // 10

print(total)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-28  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

n = int(input("Enter a num: "))
largest = -1

if n == 0:
    largest = 0

for i in range(1, n+1):
    if n > 0:
        digit = n % 10
        if digit > largest:
            largest = digit
        n = n // 10

print(largest)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-29  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

n = int(input("Enter a num: "))
smallest = 9

if n == 0:
    smallest = 0

for i in range(1, n+1):
    if n > 0:
        digit = n % 10
        if digit < smallest:
            smallest = digit
        n = n // 10

print(smallest)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-30  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

n = int(input("Enter a num: "))
reversed_num = 0

for i in range(1, n+1):
    if n > 0:
        reversed_num = (reversed_num * 10) + (n % 10)
        n = n // 10

print(reversed_num)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-31  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

n = int(input("Enter a num: "))
original = n
reversed_num = 0

for i in range(1, n+1):
    if n > 0:
        reversed_num = (reversed_num * 10) + (n % 10)
        n = n // 10

if original == reversed_num:
    print("Palindrome")
else:
    print("Not Palindrome")


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-32  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

n = int(input("Enter a num: "))
target = int(input("Enter target digit: "))
count = 0

if n == 0 and target == 0:
    count = 1

for i in range(1, n+1):
    if n > 0:
        if (n % 10) == target:
            count = count + 1
        n = n // 10

print(count)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-33  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

n = int(input("Enter a num: "))

for i in range(1, n+1):
    if n >= 10:
        n = n // 10

print(n)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-34  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

n = int(input("Enter a num: "))
largest = -1
smallest = 9

if n == 0:
    largest = 0
    smallest = 0

for i in range(1, n+1):
    if n > 0:
        digit = n % 10
        if digit > largest:
            largest = digit
        if digit < smallest:
            smallest = digit
        n = n // 10

diff = largest - smallest
print(diff)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-35  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

n = int(input("Enter a num: "))
pos = 1

for i in range(1, n+1):
    if n > 0:
        print(n % 10, pos)
        pos = pos + 1
        n = n // 10


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-36  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

n = int(input("Enter a 3-digit num: "))
original = n
total = 0

for i in range(3):
    digit = n % 10
    total = total + (digit * digit * digit)
    n = n // 10

if original == total:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")