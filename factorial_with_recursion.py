def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1)

print(int(fact(input("Enter a number: "))))
