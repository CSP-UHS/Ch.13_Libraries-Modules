'''
Paste all the functions that you submitted in the Functions chapter into a single file called my_library.py.
This should only include all of the (defs), not the inputs and function calls. 
Create a main program called my_program.py which will import the my_library module. 
In this program you will put the inputs and function calls. 
Use the import * so you don't have to use namespaces for each function call. 
Use if __name__ =="__main__":
'''
from my_program import *


def main():
    print(mini(7, 3, 5))
    box(7, 5)
    nlist = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]
    find(nlist, 12)
    fizzbuzz(15)
    for i in fibonacci(100):
        print(f"{i:27,}")
    my_list = create_list(10000)
    for i in range(1, 7):
        print("There are", count_list(my_list, i), i, "in the list")
    print(average_list(my_list))
    arcade.open_window(600, 600, "BB8")
    arcade.set_background_color(arcade.color.WHEAT)
    arcade.start_render()

    draw_BB8(100,50,50)
    draw_BB8(300, 300, 30)
    draw_BB8(500, 100, 20)
    draw_BB8(500, 400, 60)
    draw_BB8(120, 500, 15)

    arcade.finish_render()
    arcade.run()


if __name__ == '__main__':
    main()