'''
Sign your name:________________
 
For this test, take your 30 box program and remove the Box Class into a seperate file called Box_Builder.py. Now just
import the Box Class into your main program. No need to pull request this. Just show it to your instructor if you can get
it to work. Use if __name__ =="__main__":

'''
from Box_Builder import Ball

if __name__=="__main__":
    Ball
    print("Box_builder is being run directly")
else:
    Ball
    print("Box_builder is being run imported")
