def mini(a, b, c):
    if a < b and a < c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c


def main():
    print(mini(7, 3, 5))
    print(mini(5, 5, 4))
    print(mini(2, 2, 3))
    print(mini(-2, -6, -100))
    print(mini("Z", "B", "A"))

def box(h,w):
    for i in range(h):
        print("o"*w)

def main2():
    box(7,5) #print a box 7 high, 5 across
    print()
    box(3,2) #box 3 high, 2 across
    print()
    box(3,10) #box 3 hight, 10 across

def find(list,key):
    for i in range(len(list)):
        if list[i] == key:
            print(f"Found {key} at position {i}")

def fizzbuzz(endpoint):
    for num in range(1,endpoint+1):
        if num%15 == 0:
            print("Fizzbuzz")
        elif num%5 == 0:
            print("Buzz")
        elif num%3 == 0:
            print("Fizz")
        else:
            print(num)

def main3():
    fizzbuzz(15)

def fibonacci(num):
    x,y = -1,1
    for i in range(num):
        z = x+y
        x = y
        y = z
        print(f"{z:>50,}")

def hypotenuse(a,b):
    h=(a**2+b**2)**.5
    print(f"The hypotenuse is {h:.2f}")

def mean(a,b,c):
    ave=(a+b+c)/3.0
    print(f"The average is {ave:.2f}")

def perimeter(b,h):
    per=b*h
    print(f"The area of the rectangle was {per:.2f}")

def myprogram():
    hypotenuse(3,4)
    mean(3,7,23)
    perimeter(10,3)