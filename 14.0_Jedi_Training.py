'''
Sign your name:________________
 
For this test, take your 30 box program and remove the Box Class into a seperate file called Box_Builder.py. Now just
import the Box Class into your main program. No need to pull request this. Just show it to your instructor if you can get
it to work. Use if __name__ =="__main__":

'''
from Box_Builder import *
import arcade
import random
if __name__=="__main__":


    class MyGame(arcade.Window):
        def __init__(self, SW, SH, title):
            super().__init__(SW, SH, title)
            arcade.set_background_color(arcade.color.GRAY)
            self.ball_list = []
            for i in range(30):
                s = random.randint(2, 75)
                x = random.randint(s, SW - s)
                y = random.randint(s, SH - s)
                dx = random.randint(-3, 3)
                dy = random.randint(-3, 3)
                c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                ball = Ball(x, y, s, dx, dy, c)
                if dx == 0:
                    dx += 4
                self.ball_list.append(ball)

        def on_draw(self):
            arcade.start_render()
            arcade.draw_rectangle_filled(rail / 2, SH / 2, rail, SH, arcade.color.BOTTLE_GREEN)
            arcade.draw_rectangle_filled(SW / 2, SH - rail / 2, SW, rail, arcade.color.PURPLE_MOUNTAIN_MAJESTY)
            arcade.draw_rectangle_filled(SW - rail / 2, SH / 2, rail, SH, arcade.color.ORIOLES_ORANGE)
            arcade.draw_rectangle_filled(SW / 2, rail / 2, SW, rail, arcade.color.DARK_BROWN)
            for ball in self.ball_list:
                ball.draw_ball()

        def on_update(self, dt):
            for ball in self.ball_list:
                ball.update_ball()


    def myprogram():
        window = MyGame(SW, SH, "The Hermonator")
        arcade.run()


    if __name__ == "__main__":
        myprogram()
    print("Box_builder is being run directly")
else:


    class MyGame(arcade.Window):
        def __init__(self, SW, SH, title):
            super().__init__(SW, SH, title)
            arcade.set_background_color(arcade.color.GRAY)
            self.ball_list = []
            for i in range(30):
                s = random.randint(2, 75)
                x = random.randint(s, SW - s)
                y = random.randint(s, SH - s)
                dx = random.randint(-3, 3)
                dy = random.randint(-3, 3)
                c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                ball = Ball(x, y, s, dx, dy, c)
                if dx == 0:
                    dx += 4
                self.ball_list.append(ball)

        def on_draw(self):
            arcade.start_render()
            arcade.draw_rectangle_filled(rail / 2, SH / 2, rail, SH, arcade.color.BOTTLE_GREEN)
            arcade.draw_rectangle_filled(SW / 2, SH - rail / 2, SW, rail, arcade.color.PURPLE_MOUNTAIN_MAJESTY)
            arcade.draw_rectangle_filled(SW - rail / 2, SH / 2, rail, SH, arcade.color.ORIOLES_ORANGE)
            arcade.draw_rectangle_filled(SW / 2, rail / 2, SW, rail, arcade.color.DARK_BROWN)
            for ball in self.ball_list:
                ball.draw_ball()

        def on_update(self, dt):
            for ball in self.ball_list:
                ball.update_ball()


    def myprogram():
        window = MyGame(SW, SH, "The Hermonator")
        arcade.run()


    if __name__ == "__main__":
        myprogram()
    print("Box_builder is being run imported")
