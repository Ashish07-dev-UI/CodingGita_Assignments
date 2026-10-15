# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-53  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

n = int(input("Enter a num: "))
m1 = -1
m2 = -1

if n == 0:
    m1 = 0

for i in range(100):
    if n > 0:
        d = n % 10
        if d > m1:
            m2 = m1
            m1 = d
        elif d > m2 and d != m1:
            m2 = d
        n = n // 10

print(m2)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-54  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

x = input("Enter a string: ")
c = 0
b = 0
p = ""

for i in range(len(x)):
    if x[i] == p:
        c = c + 1
    else:
        c = 1
        p = x[i]
    
    if c > b:
        b = c

print(b)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-55  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

x = input("Enter a string: ")
t = input("Enter a target char: ")
c = 0

for i in range(len(x)):
    if x[i] == t:
        c = c + 1

f = (c / len(x)) * 100
print(f"Count = {c}, Frequency = {round(f, 2)}%")


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-56  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

n = int(input("Enter a num: "))
s = 0

for i in range(100):
    if n > 0:
        s = s + (n % 10)
        print(s)
        n = n // 10


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-57  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

n = int(input("Enter a num: "))
e = 0
o = 0

for i in range(100):
    if n > 0:
        d = n % 10
        if d % 2 == 0:
            e = e + 1
        else:
            o = o + 1
        n = n // 10

if e > o:
    print("More Even Digits")
elif o > e:
    print("More Odd Digits")
else:
    print("Equal")


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-58  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

n = int(input("Enter a num: "))
s = 0
sign = 1

for i in range(100):
    if n > 0:
        s = s + (n % 10) * sign
        sign = sign * -1
        n = n // 10

print(s)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-59  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Prediction:
# 2
# 6
# 12
# 20
# 30


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-60  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Prediction Output:
# 5
#
# Explanation: 
# The loop runs from 1 to 10. The condition `if i % 2 == 0:` checks if the number is even. 
# There are exactly 5 even numbers in this range (2, 4, 6, 8, 10). The `count` variable 
# increments by 1 each time an even number is found, so the final value printed is 5.


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Question-61  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# 1. Identify the mistake:
# The mistake is `sum = i`. This overwrites the previous value of sum in every iteration 
# instead of adding to the running total. 

# 2. Correct the program:
total_sum = 0
for i in range(1, 6):
    total_sum = total_sum + i
print(total_sum)

# 3. Explain what should happen to the accumulator:
# The accumulator variable must be added to itself along with the new value (e.g., total = total + i) 
# so that it remembers the previous calculations and keeps a continuous running total throughout the loop.