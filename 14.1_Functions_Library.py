'''
Paste all the functions that you submitted in the Functions chapter into a single file called my_library.py.
This should only include all of the (defs), not the inputs and function calls. 
Create a main program called my_program.py which will import the my_library module. 
In this program you will put the inputs and function calls. 
Use the import * so you don't have to use namespaces for each function call. 
Use if __name__ =="__main__":
'''
from my_library import *

if __name__=="__main__":
    Fibonacci()
    mini(3,4,6)
    box(3,6)
    increase()
    count_to_ten()