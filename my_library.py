'''
this file will contain all of the functions from Ch9 (functions)
'''


def increase(x):
    return x + 1


def count_to_ten():
    for i in range(10):
        print(i+1)


def sum_list(list):
    x = 0
    for i in range(len(list)):
        x += list[i]
    return x


def reverse(text):
    result = ""
    for i in range(len(text)):
        result += text[len(text) - 1 - i]
    return result


def get_user_choice():
    while True:
        command = input("Command: ")
        if command.upper()[:1] == 'F' or command.upper()[:1] == 'M' or command.upper()[:1] == 'S' \
                or command.upper()[:1] == 'D' or command.upper()[:1] == 'Q':
            return command

        print("Hey, that's not a command. Here are your options:")
        print("f - Full speed ahead")
        print("m - Moderate speed")
        print("s - Status")
        print("d - Drink")
        print("q - Quit")


def minimum(x, y, z):
    if x < y and x < z:
        mini = x
    elif y < x and y < z:
        mini = y
    else:
        mini = z
    return mini


def box(height, width):
    line = ''
    for i in range(width):
        line += 'o'
    for i in range(height):
        print(line)


def find(list, num):
    for i in range(len(list)):
        if list[i] == num:
            print('Found', num, 'at position', i)


def fizzbuzz(max):
    for i in range(1, max + 1):  # +1 makes sure to include the max (so it will go to 100 instead of 99)
        if i % 3 == 0 and i % 5 == 0:       # print(3 % 4) == remainder of 3
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)


def fibonacci(max):
    num = 1
    last_num = 0
    for i in range(max):
        print(f"{num:>30,}")
        num += last_num
        last_num = num - last_num
