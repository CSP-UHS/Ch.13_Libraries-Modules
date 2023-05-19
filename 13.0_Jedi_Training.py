'''
Sign your name:Samuel Pattison
 
For this test, take your 30 box program and remove the Box Class into a seperate file called Box_Builder.py. Now just
import the Box Class into your main program. No need to pull request this. Just show it to your instructor if you can get
it to work. Use if __name__ =="__main__":

'''
from Box_Builder import *


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BRIGHT_NAVY_BLUE)
        self.balls = []
        for i in range(30):
            size = random.randint(10, 50)
            x = random.randint(30 + size, 570 - size)
            y = random.randint(30 + size, 570 - size)
            dx = random.randint(-5, 5)
            if dx == 0:
                dx += 1
            dy = random.randint(-5, 5)
            if dy == 0:
                dy += 1
            col = arcade.color.BLACK
            box = Box(x, y, dx, dy, size, col)
            self.balls.append(box)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(300, 585, 540, 30, arcade.color.AO)
        arcade.draw_rectangle_filled(585, 300, 30, 540, arcade.color.UFO_GREEN)
        arcade.draw_rectangle_filled(300, 15, 540, 30, arcade.color.RADICAL_RED)
        arcade.draw_rectangle_filled(15, 300, 30, 540, arcade.color.ALLOY_ORANGE)
        for box in self.balls:
            box.draw_box()

    def on_update(self, dt):
        for box in self.balls:
            box.update_box()


def main():
    window = MyGame(SW, SH, "Thirty Boxes")
    arcade.run()


if __name__ == "__main__":
    main()