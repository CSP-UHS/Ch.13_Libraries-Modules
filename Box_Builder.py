'''
Put the Box class (from the 30 Box Bounce program) in here, and then try to call it in the jedi training
'''

import arcade
import random

screen_width = 600
screen_height = 600


class Box:
    def __init__(self, x, y, side, speed_x, speed_y):
        self.x = x
        self.y = y
        self.wx = side
        self.wy = side
        self.color = arcade.color.BLACK
        self.speed_x = speed_x
        self.speed_y = speed_y
        if self.speed_x == 0:
            self.speed_x = random.randint(2, 6)
        elif self.speed_y == 0:
            self.speed_y = random.randint(2, 6)

    def box_draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.wx, self.wy, self.color)  # draw each box
        # draw the walls

    def update_box(self):
        self.x += self.speed_x
        self.y += self.speed_y
        # check if the thing is colliding with something
        if self.x - (0.5 * self.wx) <= 30:  # collide with left wall
            if self.speed_x < 0:
                self.speed_x *= -1
            self.color = arcade.color.BLUE
        elif self.x + (0.5 * self.wx) >= screen_width - 30:     # collide with right wall
            if self.speed_x > 0:
                self.speed_x *= -1
            self.color = arcade.color.YELLOW
        elif self.y - (0.5 * self.wy) <= 30:    # collide with bottom wall
            if self.speed_y < 0:
                self.speed_y *= -1
            self.color = arcade.color.LIME_GREEN
        elif self.y + (0.5 * self.wy) >= screen_height - 30:        # collide with top wall
            if self.speed_y > 0:
                self.speed_y *= -1
            self.color = arcade.color.RED
