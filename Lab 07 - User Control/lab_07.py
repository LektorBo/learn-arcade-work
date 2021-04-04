""" Lab 7 - User Control """

import arcade
import random

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLATE_RADIUS = 250
MOVEMENT_SPEED = 3

def draw_plate(center_x, center_y, radius):
    """ Drawing the plate """
    arcade.draw_circle_filled(center_x, center_y, radius, (255, 255, 255))
    arcade.draw_circle_outline(center_x, center_y, radius, (0, 0, 0))
    arcade.draw_circle_outline(center_x, center_y, radius-50, (0, 0, 0))

def draw_pizza(corner_x1, corner_y1):
    """ Drawing the pizza slice """
    corner_x2 = corner_x1+1.28*PLATE_RADIUS
    corner_y2 = corner_y1-0.08*PLATE_RADIUS
    corner_x3 = corner_x1+0.8*PLATE_RADIUS
    corner_y3 = corner_y1-PLATE_RADIUS
    arcade.draw_triangle_filled(corner_x1, corner_y1, corner_x2, corner_y2, corner_x3, corner_y3, (235, 153, 38))
    arcade.draw_triangle_outline(corner_x1, corner_y1, corner_x2, corner_y2, corner_x3, corner_y3, (0, 0, 0))
    # Crust
    arcade.draw_arc_filled((corner_x2 + corner_x3)/2-1,
                            (corner_y2 + corner_y3)/2,
                            ((corner_x2-corner_x3)**2 + (corner_y2-corner_y3)**2)**0.5,
                            PLATE_RADIUS*0.24,
                            (201, 156, 58),
                            0,
                            180,
                            242.3)
    arcade.draw_arc_outline((corner_x2 + corner_x3)/2-1,
                            (corner_y2 + corner_y3)/2,
                            ((corner_x2-corner_x3)**2 + (corner_y2-corner_y3)**2)**0.5,
                            PLATE_RADIUS*0.24,
                            (0, 0, 0),
                            0,
                            180,
                            3,
                            242.3)

def draw_pepperoni(x, y):
    """ Drawing pepperoni on  the pizza slice """
    arcade.draw_circle_filled(x, y, PLATE_RADIUS/12.5, (201, 42, 42))
    arcade.draw_circle_outline(x, y, PLATE_RADIUS/12.5, (0, 0, 0))
    arcade.draw_circle_outline(x-2, y+7, 0.006*PLATE_RADIUS, (0, 0, 0))
    arcade.draw_circle_outline(x+7, y-2, 0.006*PLATE_RADIUS, (0, 0, 0))
    arcade.draw_circle_outline(x+3, y+6, 0.006*PLATE_RADIUS, (0, 0, 0))
    arcade.draw_circle_outline(x-6, y-3, 0.006*PLATE_RADIUS, (0, 0, 0))

class Knife:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color, color2):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color
        self.color2 = color2

        self.chrunch = arcade.load_sound("crunch.1.ogg")

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_ellipse_filled(self.position_x, self.position_y, 20, 200, self.color)
        arcade.draw_rectangle_filled(self.position_x, self.position_y+100, 20, 200, self.color)
        arcade.draw_arc_filled(self.position_x+10, self.position_y+200, 400, 40, self.color2, 0, 90, 90)


    def update(self):
        # Move the knife
        self.position_y += self.change_y
        self.position_x += self.change_x


        # See if the ball hit the edge of the screen. If so, change direction

        if self.position_x < self.radius:

            self.position_x = self.radius
            arcade.play_sound(self.chrunch)



        if self.position_x > SCREEN_WIDTH - self.radius:

            self.position_x = SCREEN_WIDTH - self.radius
            arcade.play_sound(self.chrunch)



        if self.position_y < self.radius + 90:

            self.position_y = self.radius + 90
            arcade.play_sound(self.chrunch)



        if self.position_y > SCREEN_HEIGHT - (self.radius + 390):

            self.position_y = SCREEN_HEIGHT - (self.radius+ 390)
            arcade.play_sound(self.chrunch)

class Fork:
    def __init__(self, position_x, position_y, change_x, change_y, width, height, color, color2):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.width = width
        self.height = height
        self.color = color
        self.color2 = color2

    def draw(self):
        """ Draw the fork with the instance variables we have. """
        arcade.draw_ellipse_filled(self.position_x, self.position_y, 20, 200, self.color)
        arcade.draw_rectangle_filled(self.position_x, self.position_y+110, 20, 240, self.color)
        arcade.draw_arc_filled(self.position_x, self.position_y+230, 40, 80, self.color2, 0, 180, 180)
        arcade.draw_rectangle_filled(self.position_x, self.position_y+260, 3, 80, self.color2)
        arcade.draw_rectangle_filled(self.position_x+9, self.position_y+260, 3, 80, self.color2)
        arcade.draw_rectangle_filled(self.position_x+18, self.position_y+260, 3, 80, self.color2)
        arcade.draw_rectangle_filled(self.position_x-9, self.position_y+260, 3, 80, self.color2)
        arcade.draw_rectangle_filled(self.position_x-18, self.position_y+260, 3, 80, self.color2)


    def update(self):
        # Move the fork
        self.position_y += self.change_y
        self.position_x += self.change_x


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        self.set_mouse_visible(False)
        self.space_sound = arcade.load_sound("CantStopWaiting.ogg")
        self.crunch = arcade.load_sound("crunch.1.ogg")

        self.knife = Knife(50, 50, 0, 0, 15, arcade.color.BLACK, arcade.color.SILVER)
        self.fork = Fork(150, 50, 0, 0, 30, 30, arcade.color.BLACK, arcade.color.SILVER)

    def on_draw(self):
        arcade.start_render()

        # Drawing background
        arcade.set_background_color((184, 116, 20))
        draw_plate(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLATE_RADIUS)
        draw_pizza(SCREEN_WIDTH/2 - PLATE_RADIUS/2.5, SCREEN_HEIGHT/2 + PLATE_RADIUS/5)
        draw_pepperoni(400, 320)
        draw_pepperoni(400, 270)
        draw_pepperoni(450, 310)
        draw_pepperoni(450, 240)
        draw_pepperoni(500, 290)
        draw_pepperoni(550, 300)
        draw_pepperoni(520, 240)
        draw_pepperoni(500, 180)

        self.knife.draw()
        self.fork.draw()

    def update(self, delta_time):
        self.knife.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.knife.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.knife.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.knife.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.knife.change_y = -MOVEMENT_SPEED
        

        # If the user hits  the space bar, play the sound that we loaded
        if key == arcade.key.SPACE:

            arcade.play_sound(self.space_sound)

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.knife.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.knife.change_y = 0

    def on_mouse_motion(self, x, y, dx, dy):

        """ Called to update our objects. Happens approximately 60 times per second."""

        self.fork.position_x = x

        self.fork.position_y = y
    
    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """

        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.crunch)


def main():
    window = MyGame()
    arcade.run()


main()