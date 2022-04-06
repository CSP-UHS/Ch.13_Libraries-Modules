SW=600
SH=600
rail=10
import random
import arcade

class Ball():
    def __init__(self,pos_x,pos_y,s,dx,dy,c):
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.s=s
        self.dx=dx
        self.dy=dy
        self.col=c
    def draw_ball(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.s, self.s, self.col)
    def update_ball(self):
        self.pos_x+=self.dx
        self.pos_y+=self.dy
        if self.pos_x<=rail+self.s/2:
            self.dx *= -1
            self.col=arcade.color.BOTTLE_GREEN
        if self.pos_x>=SW-rail-self.s/2:
            self.col=arcade.color.ORIOLES_ORANGE
            self.dx *= -1
        if self.pos_y<=rail+self.s/2:
            self.col=arcade.color.DARK_BROWN
            self.dy *= -1
        if self.pos_y>=SH-rail-self.s/2:
            self.col=arcade.color.PURPLE_MOUNTAIN_MAJESTY
            self.dy *= -1






