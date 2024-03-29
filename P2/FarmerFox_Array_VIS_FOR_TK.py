from show_state_array import initialize_tk, state_array, state_display, STATE_WINDOW, test

from tkinter import font

myFont=None

WIDTH = 1024
HEIGHT = 400
TITLE = 'The Farmer and Fox Puzzle'

the_state_array=None

def initialize_vis():
    initialize_tk(WIDTH, HEIGHT, TITLE)

def render_state(s):
    # Note that font creation is only allowed after the Tk root has been
    # defined.  So we check here if the font creation is still needed,
    # and we do it (the first time this method is called).
    global myFont
    if not myFont:
        myFont = font.Font(family="Helvetica", size=24, weight="bold")
    print("In render_state, state is "+str(s))
    # Create the default array of colors
    tan = (126,115,95)
    blue = (0,120,215)
    brown = (100, 80, 0)
    purple = (177,70,194)
    cyan = (100, 200, 200)
    orange=(247, 99, 12)
    yellow=(255,185,0)
    black=(76,74,72)
    red=(232,17,35)
    row = [tan]*2 + [blue]*4 + [tan]*2
    the_color_array = [row, row[:],row[:]]
    # Now create the default array of string labels.
    row = ['' for i in range(8)]
    the_string_array = [row, row[:],row[:]]

    # Adjust colors and strings to match the state.

    if s.boat_on_right:
        the_color_array[0][5]=brown
        the_string_array[0][5]="Boat"
        the_color_array[0][6]=yellow
        the_string_array[0][6]="Farmer"
    else:
        the_color_array[0][2]=brown
        the_string_array[0][2]="Boat"
        the_color_array[0][1]=yellow
        the_string_array[0][1]="Farmer"
    if s.fox_on_right:
        the_color_array[0][7]=orange
        the_string_array[0][7]="Fox"
    else:
        the_color_array[0][0]=orange
        the_string_array[0][0]="Fox"
    if s.chicken_on_right:
        the_color_array[1][7]=red
        the_string_array[1][7]="Chicken"
    else:
        the_color_array[1][0]=red
        the_string_array[1][0]="Chicken"
    if s.grain_on_right:
        the_color_array[2][7]=purple
        the_string_array[2][7]="Grain"
    else:
        the_color_array[2][0]=purple
        the_string_array[2][0]="Grain"

    caption="Current state of the puzzle. Textual version: "+str(s)        
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
    #print("the_state_array is: "+str(the_state_array))
    the_state_array.show()
