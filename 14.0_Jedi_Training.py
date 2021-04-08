'''
Sign your name: Geni W
 
For this test, take your 30 box program and remove the Box Class into a seperate file called Box_Builder.py. Now just
import the Box Class into your main program. No need to pull request this. Just show it to your instructor if you can get
it to work. Use if __name__ =="__main__":

'''
import arcade
import random
from Box_builder import *

SW = 600
SH = 600
box_num = 30
BW = 30


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.box_list = []  # Make list to hold boxes

        # create boxes
        for i in range(box_num):
            s = random.randint(10, 50)
            dx = random.randint(-5, 5)
            dy = random.randint(-5, 5)
            x = random.randint(BW + s // 2, SW - BW - s // 2)
            y = random.randint(BW + s // 2, SW - BW - s // 2)
            c = arcade.color.BLACK
            if dx == 0 and dy == 0:
                dx = 20
            box = Box(x, y, s, dx, dy, c)
            self.box_list.append(box)

    def on_draw(self):
        arcade.start_render()
        for box in self.box_list:
            box.draw_box()
        # Make rails
        arcade.draw_rectangle_filled(BW // 2, SH // 2, BW, SH, arcade.color.PINK)  # Left
        arcade.draw_rectangle_filled(SW - BW // 2, SH // 2, BW, SH, arcade.color.BANANA_YELLOW)  # Right
        arcade.draw_rectangle_filled(SW // 2, SH - BW // 2, SW, BW, arcade.color.BLUE_GREEN)  # Top
        arcade.draw_rectangle_filled(SW // 2, BW // 2, SW, BW, arcade.color.BLUEBERRY)  # Bottom

    def on_update(self, dt):
        for box in self.box_list:
            box.update_box()


def main():
    window = MyGame(SW, SH, "30 Boxes")
    arcade.run()


if __name__ == "__main__":
    main()
