import arcade
import random


def mini(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= c and b <= c:
        return b
    elif c <= a and c <= b:
        return c


def box(h, w):
    for i in range(h):
        print("o" * w)


def find(list, n):
    p = 0
    for i in list:
        if i == n:
            print("Found", n, "at position", p)
        p += 1


def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("fizzbuzz")
        elif i % 5 == 0:
            print("buzz")
        elif i % 3 == 0:
            print("fizz")
        else:
            print(i)


def fibonacci(n):
    nlist = [1, 1, 2]
    for i in range(3, n):
        nlist.append(nlist[i-2]+nlist[i-1])
    return nlist


def create_list(l):
    nlist = []
    for i in range(l):
        nlist.append(random.randint(1, 6))
    return nlist


def count_list(list, n):
    count = 0
    for i in list:
        if i == n:
            count += 1
    return count


def average_list(list):
    n = 0
    for i in list:
        n += i
    avg = n/len(list)
    return avg


def draw_BB8(x,y, radius):
    arcade.draw_circle_outline(x, y, radius * 1.1, arcade.color.BLACK, 10)
    arcade.draw_circle_filled(x, y, radius, arcade.color.WHITE)
    arcade.draw_circle_outline(x, y, radius * 1.1 / 1.5, arcade.color.BLACK, 10)
    arcade.draw_circle_filled(x, y, radius / 1.5, arcade.color.ORANGE)
    arcade.draw_circle_outline(x, y, radius * 1.2 / 3, arcade.color.BLACK, 10)
    arcade.draw_circle_filled(x, y, radius / 3, arcade.color.ASH_GREY)
    arcade.draw_rectangle_filled(x, y + radius * .9, radius * 1.65, 7, arcade.color.BLACK)
    arcade.draw_arc_outline(x, y + radius * .9, radius * 1.55, radius * 1.55, arcade.color.BLACK, 0, 180, 10)
    arcade.draw_arc_filled(x, y + radius * .9, radius * 1.5, radius * 1.5, arcade.color.WHITE, 0, 180)
    arcade.draw_circle_outline(x, y + radius * 1.25, radius / 4 * 1.2, arcade.color.BLACK, 5)
    arcade.draw_circle_filled(x, y + radius * 1.25, radius / 4, arcade.color.SKY_BLUE)