import arcade
SW = 600
SH = 600
BW = 30
class Box:
    def __init__(self, x, y, side, dx, dy, c):
        self.x = x
        self.y = y
        self.side = side
        self.dx = dx
        self.dy = dy
        self.c = c

    def draw_box(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.side, self.side, self.c)

    def update_box(self):
        self.x += self.dx
        self.y += self.dy

        # Bounce off left
        if self.x <= BW + self.side / 2:
            self.dx *= -1
            self.c = arcade.color.PINK
        # Bounce off right
        if self.x >= SW - BW - self.side / 2:
            self.dx *= -1
            self.c = arcade.color.BANANA_YELLOW
        # Bounce off top
        if self.y >= SH - BW - self.side / 2:
            self.dy *= -1
            self.c = arcade.color.BLUE_GREEN
        # Bounce off bottom
        if self.y <= BW + self.side / 2:
            self.dy *= -1
            self.c = arcade.color.BLUEBERRY