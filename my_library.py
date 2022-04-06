def reverse(text):
    result = " "
    text_length = len(text)
    for i in range(1,len(text) + 1):
        result = result + text[i * -1]
    return result
def get_user_choice():
    while True:
        command = str(input("Command: "))
        if command.lower() == "f" or command.lower() == "m" or command.lower() == "s" or command.lower() == "d" or command.lower() == "q":
            print("You entered:", command)
            return command
        else:
            print("Hey, that's not a command. Here are your options:" )
            print("f - Full speed ahead")
            print("m - Moderate speed")
            print("s - Status")
            print("d - Drink")
            print("q - Quit")
def sum_list():
    sum=0
    list = [45, 2, 10, -5, 100]
    for item in list:
        sum+=item
    print(sum)
def count_to_ten():
    x=0
    for i in range(10):
        x+=1
        print(x)
def increase():
    num = float(input("Enter a number: "))
    num+=1
    print("Your number has been increased to", num)
def mini(x,y,z):
    if x <= y and x <= z:
        return x
    if y <= x and y <= z:
        return y
    if z <= x and z <= y:
        return z
def box(x,y):
    for i in range(x):
        print("o"*y)
def find(list,key):
    pos=0
    for item in list:
        if item==key:
            print("Found",key,"at position", pos)
        pos+=1
def fizzbuzz(x):
    for i in range(1,x+1):
        if i%15==0:
            print("Fizzbuzz")
        elif i%5==0:
            print("Buzz")
        elif i%3==0:
            print("Fizz")
        else:
            print(i)
def Fibonacci():
    b=1
    a=0
    sum=a+b
    n=1
    x=11
    for i in range(99):
        print(f"{sum:50,}")
        a=b
        b=sum
        sum=a+b
def count_list(list,c):
    count=0
    for item in list:
        if item==c:
            count+=1
    return count
import arcade
import random
def draw_BB8(x,y, radius):
    arcade.draw_circle_filled(x,y,radius+2,arcade.color.BLACK)
    arcade.draw_circle_filled(x,y,radius,arcade.color.WHITE)
    arcade.draw_circle_filled(x,y,radius*0.7+2,arcade.color.BLACK)
    arcade.draw_circle_filled(x,y,radius*0.7,arcade.color.ORANGE)
    arcade.draw_circle_filled(x,y,radius*0.4+2,arcade.color.BLACK)
    arcade.draw_circle_filled(x,y,radius*0.4,arcade.color.LIGHT_STEEL_BLUE)
    arcade.draw_arc_filled(x,y+radius*0.85,radius*1.5,radius*1.5,arcade.color.BLACK,0,180,0,54)
    arcade.draw_arc_filled(x,y+radius*0.91,radius*1.4,radius*1.3,arcade.color.WHITE,0,180,0,54)
    arcade.draw_circle_filled(x, y + radius * 1.25, radius / 4, arcade.color.BLACK)
    arcade.draw_circle_filled(x,y+radius*1.25,radius/5,arcade.color.BLUE_GRAY)