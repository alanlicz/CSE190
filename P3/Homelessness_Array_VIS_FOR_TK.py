import show_state_array as ssa
from show_state_array import initialize_tk, state_array, state_display, test
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

myFont = None

WIDTH = 1024
HEIGHT = 600
TITLE = 'Homelessness'

tan = (132, 117, 69)
blue = (0, 120, 215)
brown = (100, 80, 0)
purple = (128, 0, 192)
cyan = (100, 200, 200)
orange = (247, 99, 12)
yellow = (255, 185, 0)
black = (76, 74, 72)
green = (20, 255, 20)
background = (126, 115, 95)


def rgb2hex(rgb):
    return "#%02x%02x%02x" % rgb


class StatusBar:
    def __init__(self, x0, y0, length, width, background, fill_color):
        self.x0 = x0
        self.y0 = y0
        self.length = length
        self.width = width
        self.background = background
        self.fill_color = fill_color
        self.bar = ssa.STATE_WINDOW.canvas.create_rectangle(x0, y0, x0 + self.length, y0 + self.width,
                                                            fill=rgb2hex(self.background))
        self.bar_fill = ssa.STATE_WINDOW.canvas.create_rectangle(x0, y0, x0, y0 + self.width,
                                                                 fill=rgb2hex(self.fill_color))

    def update(self, percentage):
        ssa.STATE_WINDOW.canvas.delete(self.bar_fill)
        self.bar_fill = ssa.STATE_WINDOW.canvas.create_rectangle(self.x0, self.y0,
                                                                 self.x0 + 20 + percentage * self.length,
                                                                 self.y0 + self.width, fill=rgb2hex(self.fill_color))


class Text:
    def __init__(self, x0, y0, text_info):
        self.x0 = x0
        self.y0 = y0
        self.text_info = text_info
        ssa.STATE_WINDOW.canvas.create_text(x0, y0, text=text_info)


class Card:
    def __init__(self, temp_text, image):
        self.image = image
        self.temp_text = temp_text
        tempimg = Image.open(self.image)
        tempimg = tempimg.resize((100, 100), Image.ANTIALIAS)
        tempimg = ImageTk.PhotoImage(tempimg)
        images.append(tempimg)
        self.op_temp_button = tk.Button(op_frame, text=self.temp_text, image=tempimg)

    def place_button(self, input_row, input_column):
        self.op_temp_button.grid(row=input_row, column=input_column)


images = []  # Store images to keep references to images to prevent garbage collection

table = None
money_bar = None
housing_price_bar = None
health_points_bar = None
employment_rate_bar = None
popularity_bar = None
homeless_people_bar = None
sf_map_gif = None
button1 = None
op_frame = None


def initialize_vis():
    global table
    global sf_map_gif
    global money_bar
    global housing_price_bar
    global health_points_bar
    global employment_rate_bar
    global popularity_bar
    global homeless_people_bar
    global button1
    global op_frame

    initialize_tk(WIDTH, HEIGHT, TITLE)
    table = ssa.STATE_WINDOW.canvas.create_rectangle(600, 0, 1200, 200, fill=rgb2hex(background))
    money_bar = StatusBar(800, 20, 200, 20, blue, green)
    housing_price_bar = StatusBar(800, 50, 200, 20, blue, yellow)
    health_points_bar = StatusBar(800, 80, 200, 20, blue, purple)
    employment_rate_bar = StatusBar(800, 110, 200, 20, blue, cyan)
    popularity_bar = StatusBar(800, 140, 200, 20, blue, orange)
    homeless_people_bar = StatusBar(800, 170, 200, 20, blue, tan)

    Text(680, 30, "Money")
    Text(680, 60, "Housing Price")
    Text(680, 90, "Health Points")
    Text(680, 120, "Employment Rate")
    Text(680, 150, "Popularity")
    Text(680, 180, "Homeless People")

    op_frame = tk.Frame(height=50, width=300, master=ssa.STATE_WINDOW)
    op_frame.pack()
    op1_button = Card("Rental Price Ceiling", "Op1.jpg")
    op1_button.place_button(1, 1)
    op2_button = Card("Build Affordable Houses", "Op2.png")
    op2_button.place_button(1, 2)
    op3_button = Card("Rental Price Ceiling", "Op3.jpg")
    op3_button.place_button(1 ,3)
    op4_button = Card("Rental Price Ceiling", "Op4.jpg")
    op4_button.place_button(1, 4)
    op5_button = Card("Rental Price Ceiling", "Op5.jpg")
    op5_button.place_button(1, 5)
    op6_button = Card("Rental Price Ceiling", "Op6.png")
    op6_button.place_button(1, 6)
    """
    op7_button = Card("Rental Price Ceiling")
    op7_button.place_button(1, 7)
    op8_button = Card("Rental Price Ceiling")
    op8_button.place_button(1, 8)
    op9_button = Card("Rental Price Ceiling")
    op9_button.place_button(2, 1)
    op10_button = Card("Rental Price Ceiling")
    op10_button.place_button(2, 2)
    op11_button = Card("Rental Price Ceiling")
    op11_button.place_button(2, 3)
    op12_button = Card("Rental Price Ceiling")
    op12_button.place_button(2, 4)
    op13_button = Card("Rental Price Ceiling")
    op13_button.place_button(2, 5)
    op14_button = Card("Rental Price Ceiling")
    op14_button.place_button(2, 6)
    op15_button = Card("Rental Price Ceiling")
    op15_button.place_button(2, 7)
    op16_button = Card("Rental Price Ceiling")
    op16_button.place_button(2, 8)
    op17_button = Card("Rental Price Ceiling")
    op17_button.place_button(2, 9)
    """

    """
    tempimg = Image.open("Op1.jpg")
    tempimg = tempimg.resize((100, 100), Image.ANTIALIAS)
    tempimg = ImageTk.PhotoImage(tempimg)
    # op1_frame = tk.Frame(height=50, width=300, master=ssa.STATE_WINDOW)
    # op1_frame.pack()
    images.append(tempimg)
    # op1_frame.img = tempimg
    op1_button = tk.Button(ssa.STATE_WINDOW, text="Rental Price Ceiling", image=tempimg)
    op1_button.grid(row=1, column=1)
    """
    """
    tempimg2 = Image.open("Op2.png")
    tempimg2 = tempimg2.resize((100, 100), Image.ANTIALIAS)
    tempimg2 = ImageTk.PhotoImage(tempimg2)
    op2_frame = tk.Frame(height=50, width=300, master=ssa.STATE_WINDOW)
    op2_frame.pack()
    images.append(tempimg2)
    # op1_frame.img = tempimg
    op1_button = tk.Button(op1_frame, text="Rental Price Ceiling", image=tempimg2)
    op1_button.grid(row=1, column=2)
    """

    try:
        sf_map_gif = Image.open("SFMap.png")
        sf_map_gif = sf_map_gif.resize((500, 500), Image.ANTIALIAS)
        sf_map_gif = ImageTk.PhotoImage(sf_map_gif)

    except Exception as e:
        print("Failed to Load SF Map!")
        print(e)
    images.append(sf_map_gif)  # Store images to keep references to images to prevent garbage collection
    try:
        ssa.STATE_WINDOW.canvas.create_image(270, 270, image=sf_map_gif, anchor=tk.CENTER)
    except Exception as e:
        print("Failed to Display SF Map!")
        print(e)


def render_state(s):
    # Note that font creation is only allowed after the Tk root has been
    # defined.  So we check here if the font creation is still needed,
    # and we do it (the first time this method is called).
    global table
    global money_bar
    global housing_price_bar
    global health_points_bar
    global employment_rate_bar
    global popularity_bar
    global homeless_people_bar
    global myFont
    if not myFont:
        myFont = tk.font.Font(family="Helvetica", size=18, weight="bold")
    money_bar.update(s.money / 5000000000)
    housing_price_bar.update(s.housing_price / 2000)
    health_points_bar.update(s.health_points / 200)
    employment_rate_bar.update(s.employment_rate / 300)
    popularity_bar.update(s.popularity / 200)
    homeless_people_bar.update(s.homeless_people / 50000)
