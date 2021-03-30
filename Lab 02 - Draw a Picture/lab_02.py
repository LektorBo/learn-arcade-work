# Drawing a plate with a pizza slice

import arcade

# Open up a window
arcade.open_window(800, 600, "Pizza on plate")

#Setting background color (wooden table)
arcade.set_background_color((184, 116, 20))

# Starting to draw
arcade.start_render()

# Drawig the plate
arcade.draw_circle_filled(400, 300, 250, (255, 255, 255))
arcade.draw_circle_outline(400, 300, 250, (0, 0, 0))
arcade.draw_circle_outline(400, 300, 200, (0, 0, 0))

# Drawing the pizza slice
arcade.draw_triangle_filled(300, 350, 620, 330, 500, 100, (235, 153, 38))
arcade.draw_triangle_outline(300, 350, 620, 330, 500, 100, (0, 0, 0))
arcade.draw_arc_filled(559, 215, 259.422, 60, (201, 156, 58), 0, 180, 242.3)    # Crust
arcade.draw_arc_outline(559, 215, 259.422, 60, (0,0,0), 0, 180, 3, 242.3)       # Crust

#Drawing pepperoni on  the pizza slice
arcade.draw_circle_filled(400, 320, 20, (201, 42, 42))
arcade.draw_circle_filled(400, 270, 20, (201, 42, 42))
arcade.draw_circle_filled(450, 310, 20, (201, 42, 42))
arcade.draw_circle_filled(450, 240, 20, (201, 42, 42))
arcade.draw_circle_filled(500, 290, 20, (201, 42, 42))
arcade.draw_circle_filled(550, 300, 20, (201, 42, 42))
arcade.draw_circle_filled(520, 240, 20, (201, 42, 42))
arcade.draw_circle_filled(500, 180, 20, (201, 42, 42))

# Ending the draw
arcade.finish_render()

#Keep the window up until someone closes it
arcade.run()