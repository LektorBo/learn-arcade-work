import arcade
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Ball():
    def __init__(self):
        # --- Class Attributes ---
        # Ball position
        self.x = 0
        self.y = 0

        # Ball's vector
        self.change_x = 0
        self.change_y = 0

        # Ball size
        self.size = 10

        # Ball color
        self.color = [255, 255, 255]

    # --- Class Methods ---
    def move(self):
        self.x += self.change_x
        self.y += self.change_y

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, self.color )

def main():
    the_ball = Ball()
    the_ball.x = 100
    the_ball.y = 100
    the_ball.change_x = 500
    the_ball.change_y = 500
    the_ball.color = [255, 255, 255]
    # Open up a window
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Ball test")

    #Setting background color (wooden table)
    arcade.set_background_color((0, 0, 0))

    # Starting to draw
    arcade.start_render()

    the_ball.draw()
    the_ball.move()

    # Ending the draw
    arcade.finish_render()

    #Keep the window up until someone closes it
    arcade.run()

main()