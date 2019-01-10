import math
def calc_height(base, side):
    return math.sqrt((side**2) - (base/2.0)**2)

def area(base, height):
    return (base*height)/2.0

print("If you have a equilateral or an isosceles and don't know the height press one: ")
num = input("--> ")
if num == 1:
    base = input("base: ")
    side = input("side: ")
    print("Your height is: " + str(calc_height(base, side)))
    print("and you area is: " + str(area(base, calc_height(base, side))))
else:
    print(area(input("base: "), input("height: ")))

