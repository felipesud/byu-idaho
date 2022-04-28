# Prove Milestone: Writing Functions
# From:  https://byui-cse.github.io/cse111-course/lesson03/prove.html
# By: Felipe dos Santos Belisário

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
   
    draw_grass(canvas, scene_width, scene_height)
    # draw_grid(canvas, scene_width, scene_height, 50)


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    #Draw the sky and all the objects in the sky.
    draw_rectangle(canvas, 0, scene_height / 3,scene_width, scene_height, width=0, fill="sky blue")
    draw_oval(canvas, 500, 500, 400, 400, width=2, outline="yellow2", fill="yellow1" )
    draw_oval(canvas, 720, 470, 590, 400, width=2, outline="azure1", fill="azure1" )
    draw_oval(canvas, 300, 470, 170, 400, width=2, outline="azure1", fill="azure1" )
    draw_oval(canvas, 540, 460, 450, 420, width=2, outline="azure1", fill="azure1" )
    draw_oval(canvas, 450, 460, 360, 420, width=2, outline="azure1", fill="azure1" )

def draw_grass(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,scene_width, scene_height / 3, width=0, fill="forestGreen")
    draw_oval(canvas, 830, 250, 350, 0, width=2, outline="", fill="forestGreen" )
    draw_oval(canvas, 400, 230, 0, 0, width=2, outline="", fill="forestGreen" )



# def draw_grid(canvas, width, height, interval, color="blue"):
#     # Draw a vertical line at every x interval.
#     label_y = 15
#     for x in range(interval, width, interval):
#         draw_line(canvas, x, 0, x, height, fill=color)
#         draw_text(canvas, x, label_y, f"{x}", fill=color)

#     # Draw a horizontal line at every y interval.
#     label_x = 15
#     for y in range(interval, height, interval):
#         draw_line(canvas, 0, y, width, y, fill=color)
#         draw_text(canvas, label_x, y, f"{y}", fill=color)


# Call the main function so that
# this program will start executing.
main()