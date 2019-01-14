def convert(n):
    if n > 1:
        convert(n//2)
    print(n % 2)

convert(int(input("convert decimal to binary: ")))
