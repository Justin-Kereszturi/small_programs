import math
nterm = int(input("nterm --> "))
f = -1
s = 1
count = 0
while count < nterm:
    nth = f + s
    f = s
    s = nth
    count += 1
    print(nth)
