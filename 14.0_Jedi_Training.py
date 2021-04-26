'''
Sign your name:________________
 
For this test, take your 30 box program and remove the Box Class into a seperate file called Box_Builder.py. Now just
import the Box Class into your main program. No need to pull request this. Just show it to your instructor if you can get
it to work. Use if __name__ =="__main__":

'''

import arcade
import Box_Builder
import random

screen_height = 600
screen_width = 600


class Render(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

        self.box_list = []
        for i in range(30):
            self.box_list.append(Box_Builder.Box(random.randint(100, 500), random.randint(100, 500), random.randint(10, 50),
                                     random.randint(-10, 10), random.randint(-10, 10)))

    def on_draw(self):
        arcade.start_render()

        arcade.draw_rectangle_filled(15, screen_height / 2, 30, screen_height - 60, arcade.color.BLUE)
        arcade.draw_rectangle_filled(screen_width / 2, 15, screen_width - 60, 30, arcade.color.LIME_GREEN)
        arcade.draw_rectangle_filled(screen_width - 15, screen_height / 2, 30, screen_height - 60, arcade.color.YELLOW)
        arcade.draw_rectangle_filled(screen_width / 2, screen_height - 15, screen_width - 60, 30, arcade.color.RED)

        for i in range(len(self.box_list)):
            self.box_list[i].box_draw()

    def on_update(self, delta_time: float):
        for i in range(len(self.box_list)):
            self.box_list[i].update_box()


def main():
    window = Render(screen_width, screen_height, 'Boxes')
    arcade.run()


if __name__ == "__main__":
    main()
