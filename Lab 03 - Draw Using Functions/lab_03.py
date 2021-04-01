# Drawing a plate with a pizza slice

import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLATE_RADIUS = 250

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
    arcade.draw_circle_outline(x-random.randint(2, 7), y+random.randint(2, 7), 0.006*PLATE_RADIUS, (0, 0, 0))
    arcade.draw_circle_outline(x+random.randint(2, 7), y-random.randint(2, 7), 0.006*PLATE_RADIUS, (0, 0, 0))
    arcade.draw_circle_outline(x+random.randint(2, 7), y+random.randint(2, 7), 0.006*PLATE_RADIUS, (0, 0, 0))
    arcade.draw_circle_outline(x-random.randint(2, 7), y-random.randint(2, 7), 0.006*PLATE_RADIUS, (0, 0, 0))

def main():
    # Open up a window
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Pizza on plate")

    #Setting background color (wooden table)
    arcade.set_background_color((184, 116, 20))

    # Starting to draw
    arcade.start_render()

    draw_plate(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLATE_RADIUS)
    draw_pizza(SCREEN_WIDTH/2 - PLATE_RADIUS/2.5, SCREEN_HEIGHT/2 + PLATE_RADIUS/5)

    #Drawing pepperoni on  the pizza slice
    draw_pepperoni(400, 320)
    draw_pepperoni(400, 270)
    draw_pepperoni(450, 310)
    draw_pepperoni(450, 240)
    draw_pepperoni(500, 290)
    draw_pepperoni(550, 300)
    draw_pepperoni(520, 240)
    draw_pepperoni(500, 180)

    # Ending the draw
    arcade.finish_render()

    #Keep the window up until someone closes it
    arcade.run()

main()