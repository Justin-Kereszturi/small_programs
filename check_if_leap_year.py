def leap(year):
    if year % 1000 == 0:
        print("not a leap year")
    elif year % 4 == 0:
        print("it is a leap year")
    else:
        print("not a leap year")

print(leap(int(input("check if leap year: "))))

