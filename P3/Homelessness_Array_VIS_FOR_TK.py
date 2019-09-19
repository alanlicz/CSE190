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
    def __init__(self, text, x0, y0, length, width, background, fill_color):
        self.text = text
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
        self.text_item = ssa.STATE_WINDOW.canvas.create_text(x0 - 110, y0 + 5, text=self.text, justify=tk.LEFT,
                                                             anchor=tk.W)

    def update(self, percentage):
        ssa.STATE_WINDOW.canvas.delete(self.bar_fill)
        ssa.STATE_WINDOW.canvas.delete(self.text_item)
        self.bar_fill = ssa.STATE_WINDOW.canvas.create_rectangle(self.x0, self.y0,
                                                                 self.x0 + percentage * self.length,
                                                                 self.y0 + self.width, fill=rgb2hex(self.fill_color))
        self.text_item = ssa.STATE_WINDOW.canvas.create_text(self.x0 - 110, self.y0 + 5, text=self.text,
                                                             justify=tk.LEFT, anchor=tk.W)


class Button:
    def __init__(self, x0, y0, container, image):
        self.container = container
        self.image = image
        self.x0 = x0
        self.y0 = y0
        tempimg = Image.open(self.image)
        tempimg = tempimg.resize((100, 100), Image.ANTIALIAS)
        tempimg = ImageTk.PhotoImage(tempimg)
        images.append(tempimg)
        self.button = tk.Button(master=self.container, image=tempimg)
        self.button.grid(row=self.x0, column=self.y0)


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

    initialize_tk(WIDTH, HEIGHT, TITLE)
    table = ssa.STATE_WINDOW.canvas.create_rectangle(600, 0, 1200, 200, fill=rgb2hex(background))
    money_bar = StatusBar("Money", 800, 20, 200, 20, blue, green)
    housing_price_bar = StatusBar("Housing Price", 800, 50, 200, 20, blue, yellow)
    health_points_bar = StatusBar("Health Points", 800, 80, 200, 20, blue, purple)
    employment_rate_bar = StatusBar("Employment Rate", 800, 110, 200, 20, blue, cyan)
    popularity_bar = StatusBar("Popularity", 800, 140, 200, 20, blue, orange)
    homeless_people_bar = StatusBar("Homeless People", 800, 170, 200, 20, blue, tan)

    op_frame = tk.Frame(height=300, width=1000, master=ssa.STATE_WINDOW)
    op_frame.pack()
    Button(1, 1, op_frame, "Op1.jpg")
    Button(1, 2, op_frame, "Op2.png")
    Button(1, 3, op_frame, "Op3.jpg")
    Button(1, 4, op_frame, "Op4.jpg")
    Button(1, 5, op_frame, "Op5.jpg")
    Button(1, 6, op_frame, "Op6.png")
    Button(1, 7, op_frame, "Op7.png")
    Button(1, 8, op_frame, "Op8.jpg")
    Button(1, 9, op_frame, "Op9.jpg")
    Button(2, 1, op_frame, "Op10.jpg")
    Button(2, 2, op_frame, "Op11.jpg")
    Button(2, 3, op_frame, "Op12.png")
    Button(2, 4, op_frame, "Op13.png")
    Button(2, 5, op_frame, "Op14.jpg")
    Button(2, 6, op_frame, "Op15.png")
    Button(2, 7, op_frame, "Op16.jpg")
    Button(2, 8, op_frame, "Op17.pn3g")

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
    money_bar.text = "Money\n{:,}".format(int(s.money))
    housing_price_bar.text = "Housing Price\n{:.1f}".format(s.housing_price)
    health_points_bar.text = "Health Points\n{:.1f}".format(s.health_points)
    employment_rate_bar.text = "Employment Rate\n{:.1f}".format(s.employment_rate)
    popularity_bar.text = "Popularity\n{:.1f}".format(s.popularity)
    homeless_people_bar.text = "Homeless People\n{:.0f}".format(s.homeless_people)
    money_bar.update(s.money / 5000000000.0)
    housing_price_bar.update(s.housing_price / 2400.0)
    health_points_bar.update(s.health_points / 100.0)
    employment_rate_bar.update(s.employment_rate / 50.0)
    popularity_bar.update(s.popularity / 100.0)
    homeless_people_bar.update(s.homeless_people / 25000.0)
