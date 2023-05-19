import arcade
import random

SH = 600
SW = 600


class Box:
    def __init__(self, pos_x, pos_y, dx, dy, size, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.size = size
        self.col = col

    def draw_box(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.size, self.size, self.col)

    def update_box(self):
        self.pos_x += self.dx
        self.pos_y += self.dy

        # Bounce ball off of walls
        if self.pos_x > SW - self.size/2 - 30:
            self.dx *= -1
            self.col = arcade.color.UFO_GREEN
        if self.pos_x < 30 + self.size/2:
            self.dx *= -1
            self.col = arcade.color.ALLOY_ORANGE
        if self.pos_y > SH - self.size/2 - 30:
            self.dy *= -1
            self.col = arcade.color.AO
        if self.pos_y < 30 + self.size/2:
            self.dy *= -1
            self.col = arcade.color.RADICAL_RED