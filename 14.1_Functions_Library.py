'''
Paste all the functions that you submitted in the Functions chapter into a single file called my_library.py.
This should only include all of the (defs), not the inputs and function calls. 
Create a main program called my_program.py which will import the my_library module. 
In this program you will put the inputs and function calls. 
Use the import * so you don't have to use namespaces for each function call. 
Use if __name__ =="__main__":
'''

from my_library import *                                # import the my library library


def main():
    print(increase(int(input("Enter a number: "))))     # print a number that was increased by one

    my_list = [1, 23, 4, 4, 2, 18]
    print(sum_list(my_list))                            # sum the list

    print(reverse(input("Enter a string of text: ")))   # reverse string of text

    print("You entered:", get_user_choice())            # do the weird get user choice function

    num1 = input('Enter number: ')
    num2 = input('Enter number: ')
    num3 = input('Enter number: ')
    print(minimum(num1, num2, num3))                    # take 3 inputs and then find the minimum

    box(7, 5)                                           # print a box 7 high, 5 across

    find(my_list, 4)                                    # find the number 4 in my_list

    fizzbuzz(100)                                       # do fizzbuzz

    fibonacci(100)                                      # write every fibonacci number up to 100


if __name__ == "__main__":
    main()
