# Prove Milestone: Writing Functions
# From:  https://byui-cse.github.io/cse111-course/lesson03/prove.html
# By: Felipe dos Santos Belisário

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    print_elements("header")
    weather = ask_weather()
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
   
    if weather == 1:

        draw_sky(canvas, scene_width, scene_height, "sunny")
        draw_sun(canvas)
        draw_cloud(canvas, "sunny")
        draw_grass(canvas, scene_width, scene_height)
        # draw_grid(canvas, scene_width, scene_height, 50)
        add_trees(canvas)
    elif weather == 2:
        draw_sky(canvas, scene_width, scene_height, "cloudy")
        draw_cloud(canvas, "cloudy")
        draw_grass(canvas, scene_width, scene_height)
        # draw_grid(canvas, scene_width, scene_height, 50)
        add_trees(canvas)
    elif weather == 3:
        draw_sky(canvas, scene_width, scene_height, "cloudy")
        draw_cloud(canvas, "cloudy")
        draw_grass(canvas, scene_width, scene_height, "snow")
        # draw_grid(canvas, scene_width, scene_height, 50)
        add_trees(canvas)
        draw_snow(canvas)
    elif weather == 4:
        finish_drawing(canvas)

    
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)
    print_elements("footer")

# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height, weather):
    if weather == "sunny":    
        #Draw the sky 
        draw_rectangle(canvas, 0, scene_height / 3,scene_width, scene_height, width=0, fill="sky blue")
    elif weather == "cloudy":
        draw_rectangle(canvas, 0, scene_height / 3,scene_width, scene_height, width=0, fill="snow3")
    
def draw_sun(canvas):
    draw_oval(canvas, 500, 500, 400, 400, width=2, outline="yellow2", fill="yellow1" )

def draw_cloud(canvas, weather):
    sunny = "azure1"
    cloudy = "snow2"
    if weather == "sunny":
        draw_oval(canvas, 720, 470, 590, 400, width=2, outline=sunny, fill=sunny )
        draw_oval(canvas, 300, 470, 170, 400, width=2, outline=sunny, fill=sunny )
        draw_oval(canvas, 540, 460, 450, 420, width=2, outline=sunny, fill=sunny )
        draw_oval(canvas, 450, 460, 360, 420, width=2, outline=sunny, fill=sunny )
    elif weather == "cloudy":
        draw_oval(canvas, 720, 470, 590, 400, width=2, outline=cloudy, fill=cloudy )
        draw_oval(canvas, 300, 470, 170, 400, width=2, outline=cloudy, fill=cloudy )
        draw_oval(canvas, 540, 460, 450, 420, width=2, outline=cloudy, fill=cloudy )
        draw_oval(canvas, 450, 460, 360, 420, width=2, outline=cloudy, fill=cloudy )


def draw_grass(canvas, scene_width, scene_height, weather):
    if weather != "snow":
        """Draw the ground and all the objects on the ground."""
        draw_rectangle(canvas, 0, 0,scene_width, scene_height / 3, width=0, fill="forestGreen")
        draw_oval(canvas, 830, 250, 350, 0, width=2, outline="", fill="forestGreen" )
        draw_oval(canvas, 400, 230, 0, 0, width=2, outline="", fill="forestGreen" )
    else:
        draw_rectangle(canvas, 0, 0,scene_width, scene_height / 3, width=0, fill="snow1")
        draw_oval(canvas, 830, 250, 350, 0, width=2, outline="", fill="snow1" )
        draw_oval(canvas, 400, 230, 0, 0, width=2, outline="", fill="snow1" )

def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")

  # Draw 1st pine tree.
def first_tree(canvas):
    tree_center_x = 200
    tree_bottom = 130
    tree_height = 180
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

# Draw 2nd pine tree.
def second_tree(canvas):
    tree_center_x = 90
    tree_bottom = 70
    tree_height = 150
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    # Draw 3rd pine tree.
def third_tree(canvas):
    tree_center_x = 550
    tree_bottom = 200
    tree_height = 150
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

  # Draw 4th pine tree.
def fourth_tree(canvas): 
    tree_center_x = 700
    tree_bottom = 150
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

     # Draw 5th pine tree.
def fifth_tree(canvas):
    tree_center_x = 5
    tree_bottom = 130
    tree_height = 90
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)
    
    
    # Draw 6th pine tree.
def  sixth_tree(canvas):    
    tree_center_x = 410
    tree_bottom = 110
    tree_height = 150
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

# Function to call all of the trees functions
def add_trees(canvas):
    first_tree(canvas)
    second_tree(canvas)
    third_tree(canvas)
    fourth_tree(canvas)
    fifth_tree(canvas)
    sixth_tree(canvas)   
# Another weather user can choose
def draw_snow(canvas):
    scene_width = 800
    scene_height = 800
    half_height = round(scene_height / 2)
    min_diam = 10
    max_diam = 20

    # Draw 300 circles, each with
    # a random location and diameter.
    for i in range(300):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(0, half_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter,fill="snow1")

# Showing Initial or Ending Message
def print_elements(option): 
    break_line = "\n***********************************************\n"
    header       = "*   Welcome to the Draw Scene Program!     *"
    footer       = "*  Thanks for using the Draw Scene Program!  *"

    if option == "header":
        print(f"{break_line}{header}{break_line}")
    elif option == "footer":
        print(f"{break_line}{footer}{break_line}")

# Asking what weather the user wants to draw
def ask_weather():
    weather = 0
    
    print(
        "Please choose the Weather selecting one of the following: \n" \
        "1. Sunny\n" \
        "2. Cloudy\n" \
        "3. Snow\n" \
        "4. Quit\n" \
        
    )
     # To prevent invalid entries
    while weather not in range(1, 4):
        # To prevent non numeric entries
        try:
            weather = int(input("Please enter an weather: ") or 0)
        except:
            weather = 0

    return weather


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