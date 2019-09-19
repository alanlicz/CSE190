from show_state_array import initialize_tk, state_array, state_display, STATE_WINDOW, test

from tkinter import font

myFont = None

WIDTH = 800
HEIGHT = 600
TITLE = 'Instant Insanity'

tan = (132, 117, 69)
blue = (0, 120, 215)
brown = (100, 80, 0)
purple = (128, 0, 192)
cyan = (100, 200, 200)
orange = (247, 99, 12)
yellow = (255, 185, 0)
black = (76, 74, 72)
background = (126, 115, 95)
cube_colors = [(232, 17, 35), (16, 124, 16), (0, 120, 215), (220, 220, 220)]

the_state_array = None

def initialize_vis():
    initialize_tk(WIDTH, HEIGHT, TITLE)


def display_cube(cube, color_array, string_array, center_coordinate):
    # coordinate (row,column)
    for i in range(4):
        color_array[center_coordinate[1]][center_coordinate[0] - 1 + i] = cube_colors[cube.faces[i]]
        string_array[center_coordinate[1]][center_coordinate[0] - 1 + i] = str(i)
    color_array[center_coordinate[1] - 1][center_coordinate[0]] = cube_colors[cube.faces[4]]
    string_array[center_coordinate[1] - 1][center_coordinate[0]] = "4"
    color_array[center_coordinate[1] + 1][center_coordinate[0]] = cube_colors[cube.faces[5]]
    string_array[center_coordinate[1] + 1][center_coordinate[0]] = "5"


def render_state(s):
    # Note that font creation is only allowed after the Tk root has been
    # defined.  So we check here if the font creation is still needed,
    # and we do it (the first time this method is called).
    global myFont
    if not myFont:
        myFont = font.Font(family="Helvetica", size=18, weight="bold")
    print("In render_state, state is " + str(s))
    # Create the default array of colors
    row = [background for i in range(12)]
    the_color_array = [row[:] for i in range(15)]
    # Now create the default array of string labels.
    row = ['' for i in range(12)]
    the_string_array = [row[:] for i in range(15)]
    sides = [0, 4, 2, 5]
    the_color_array[1][6] = orange
    the_color_array[1][7] = orange
    the_string_array[1][6] = "Sides"

    for i in range(4):
        display_cube(s.cubes[i], the_color_array, the_string_array, (2, 1 + i * 4))
        the_color_array[2][6 + i] = black
        the_string_array[2][6 + i] = str(sides[i])
        the_color_array[3][6] = cube_colors[s.cubes[0].faces[0]]
        the_color_array[3][7] = cube_colors[s.cubes[0].faces[4]]
        the_color_array[3][8] = cube_colors[s.cubes[0].faces[2]]
        the_color_array[3][9] = cube_colors[s.cubes[0].faces[5]]

        the_color_array[4][6] = cube_colors[s.cubes[1].faces[0]]
        the_color_array[4][7] = cube_colors[s.cubes[1].faces[4]]
        the_color_array[4][8] = cube_colors[s.cubes[1].faces[2]]
        the_color_array[4][9] = cube_colors[s.cubes[1].faces[5]]

        the_color_array[5][6] = cube_colors[s.cubes[2].faces[0]]
        the_color_array[5][7] = cube_colors[s.cubes[2].faces[4]]
        the_color_array[5][8] = cube_colors[s.cubes[2].faces[2]]
        the_color_array[5][9] = cube_colors[s.cubes[2].faces[5]]

        the_color_array[6][6] = cube_colors[s.cubes[3].faces[0]]
        the_color_array[6][7] = cube_colors[s.cubes[3].faces[4]]
        the_color_array[6][8] = cube_colors[s.cubes[3].faces[2]]
        the_color_array[6][9] = cube_colors[s.cubes[3].faces[5]]
    # Adjust colors and strings to match the state.

    caption = "Current state of the puzzle. Textual version: " + str(s)
    global the_state_array
    if not the_state_array:
        the_state_array = state_array(color_array=the_color_array,
                                  string_array=the_string_array,
                                  text_font=myFont,
                                  caption=caption)
    else:
        the_state_array.color_array=the_color_array
        the_state_array.string_array=the_string_array
        the_state_array.text_font=myFont
        the_state_array.caption=caption
    # print("the_state_array is: "+str(the_state_array))
    the_state_array.show()
