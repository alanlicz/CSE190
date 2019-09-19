import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

myFont = None
ROOT = None

MAP_FRAME = None
STATUSBAR_FRAME = None
MAP_CANVAS = None
STATUSBAR_CANVAS = None
GET_OPERATOR = None
STATE_TRANS_FUNCTION = None

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
        global STATUSBAR_CANVAS
        self.text = text
        self.x0 = x0
        self.y0 = y0
        self.length = length
        self.width = width
        self.background = background
        self.fill_color = fill_color
        self.bar = STATUSBAR_CANVAS.create_rectangle(x0, y0, x0 + self.length, y0 + self.width,
                                                     fill=rgb2hex(self.background))
        self.bar_fill = STATUSBAR_CANVAS.create_rectangle(x0, y0, x0, y0 + self.width,
                                                          fill=rgb2hex(self.fill_color))
        self.text_item = STATUSBAR_CANVAS.create_text(x0 - 110, y0 + 5, text=self.text, justify=tk.LEFT, anchor=tk.W)

    def update(self, percentage):
        global STATUSBAR_CANVAS
        STATUSBAR_CANVAS.delete(self.bar_fill)
        STATUSBAR_CANVAS.delete(self.text_item)
        self.bar_fill = STATUSBAR_CANVAS.create_rectangle(self.x0, self.y0,
                                                          self.x0 + percentage * self.length,
                                                          self.y0 + self.width, fill=rgb2hex(self.fill_color))
        self.text_item = STATUSBAR_CANVAS.create_text(self.x0 - 110, self.y0 + 5, text=self.text, justify=tk.LEFT,
                                                      anchor=tk.W)


class Text:
    def __init__(self, x0, y0, text_info):
        global STATUSBAR_CANVAS
        self.x0 = x0
        self.y0 = y0
        self.text_info = text_info
        STATUSBAR_CANVAS.create_text(x0, y0, text=text_info)


class Card:
    def __init__(self, text, image_path, background_path, operator, x0=0, y0=0):
        global ROOT
        global MAP_FRAME
        global images
        self.text = text
        self.image = Image.open(image_path)
        self.image = self.image.resize((80, 40), Image.ANTIALIAS)
        print(self.image)
        self.image = ImageTk.PhotoImage(self.image)
        self.background_image = Image.open(background_path)
        self.background_image = self.background_image.resize((100, 100), Image.ANTIALIAS)
        self.background_image = ImageTk.PhotoImage(self.background_image)
        images.append(self.image)
        images.append(self.background_image)
        self.operator = operator
        self.button = tk.Button(CARD_FRAME, image=self.background_image, command=operator, width=100, height=120)
        self.button.place(x=x0, y=y0)
        self.x0 = x0
        self.y0 = y0
        self.text_label = tk.Label(master=CARD_FRAME, text=text)
        self.text_label.place()
        self.image_label = tk.Label(master=CARD_FRAME, image=self.image)
        self.image_label.place()


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
CARD_FRAME = None


def operator01():
    global STATE_TRANS_FUNCTION
    return STATE_TRANS_FUNCTION("1")


def operator02():
    global STATE_TRANS_FUNCTION
    return STATE_TRANS_FUNCTION("2")


def operator03():
    global STATE_TRANS_FUNCTION
    return STATE_TRANS_FUNCTION("3")


def operator04():
    global STATE_TRANS_FUNCTION
    return STATE_TRANS_FUNCTION("4")


def operator05():
    global STATE_TRANS_FUNCTION
    return STATE_TRANS_FUNCTION("5")


def operator06():
    global STATE_TRANS_FUNCTION
    return STATE_TRANS_FUNCTION("6")


def operator07():
    global STATE_TRANS_FUNCTION
    return STATE_TRANS_FUNCTION("7")


def operator08():
    global STATE_TRANS_FUNCTION
    return STATE_TRANS_FUNCTION("8")


def operator09():
    global STATE_TRANS_FUNCTION
    return STATE_TRANS_FUNCTION("9")


def operator10():
    global STATE_TRANS_FUNCTION
    return STATE_TRANS_FUNCTION("10")


def operator11():
    global STATE_TRANS_FUNCTION
    return STATE_TRANS_FUNCTION("11")


def operator12():
    global STATE_TRANS_FUNCTION
    return STATE_TRANS_FUNCTION("12")


def operator13():
    global STATE_TRANS_FUNCTION
    return STATE_TRANS_FUNCTION("13")


def operator14():
    global STATE_TRANS_FUNCTION
    return STATE_TRANS_FUNCTION("14")


def operator15():
    global STATE_TRANS_FUNCTION
    return STATE_TRANS_FUNCTION("15")


def operator16():
    global STATE_TRANS_FUNCTION
    return STATE_TRANS_FUNCTION("16")


def operator17():
    global STATE_TRANS_FUNCTION
    return STATE_TRANS_FUNCTION("17")


def initialize_vis(root, current_state, get_operator, state_trans_function):
    global ROOT
    global table
    global sf_map_gif
    global money_bar
    global housing_price_bar
    global health_points_bar
    global employment_rate_bar
    global popularity_bar
    global homeless_people_bar
    global button1
    global MAP_CANVAS
    global STATUSBAR_CANVAS
    global MAP_FRAME
    global STATUSBAR_FRAME
    global STATE_TRANS_FUNCTION
    global GET_OPERATOR
    global CARD_FRAME
    STATE_TRANS_FUNCTION = state_trans_function
    GET_OPERATOR = get_operator

    try:
        sf_map_gif = Image.open("SFMap.png")
        sf_map_gif = sf_map_gif.resize((500, 500), Image.ANTIALIAS)
        sf_map_gif = ImageTk.PhotoImage(sf_map_gif)
    except Exception as e:
        print("Failed to Load SF Map!")
        print(e)
    images.append(sf_map_gif)  # Store images to keep references to images to prevent garbage collection

    ROOT = root
    # ROOT.resizable(0, 0)
    MAP_FRAME = tk.Frame(master=ROOT, width=270, height=270)
    MAP_FRAME.pack()
    CARD_FRAME = tk.Frame(master=ROOT, width=1000, height=400)
    CARD_FRAME.pack()
    MAP_CANVAS = tk.Canvas(master=MAP_FRAME, width=sf_map_gif.width(), height=sf_map_gif.height())
    MAP_CANVAS.pack(side=tk.LEFT)
    MAP_CANVAS.create_image(270, 270, image=sf_map_gif, anchor=tk.CENTER)
    STATUSBAR_CANVAS = tk.Canvas(master=MAP_FRAME, width=500, height=300)
    STATUSBAR_CANVAS.pack(side=tk.RIGHT)

    table = STATUSBAR_CANVAS.create_rectangle(0, 0, 400, 300, fill=rgb2hex(background))
    money_bar = StatusBar("Money", 120, 20, 200, 20, blue, green)
    housing_price_bar = StatusBar("Housing Price", 120, 50, 200, 20, blue, yellow)
    health_points_bar = StatusBar("Health Points", 120, 80, 200, 20, blue, purple)
    employment_rate_bar = StatusBar("Employment Rate", 120, 110, 200, 20, blue, cyan)
    popularity_bar = StatusBar("Popularity", 120, 140, 200, 20, blue, orange)
    homeless_people_bar = StatusBar("Homeless People", 120, 170, 200, 20, blue, tan)

    # op_frame = tk.Frame(height=50, width=300, master=ssa.STATE_WINDOW)
    # op_frame.pack()
    Card("Rental Price Ceiling", "Op1.jpg", "Op1.jpg", operator01, 0, 0)
    Card("Build Affordable Houses", "Op2.png", "Op2.png", operator02, 100, 0)
    Card("Street Health Care Team", "Op3.jpg", "Op3.jpg", operator03, 200, 0)
    Card("Drugs Users Treatment", "Op4.jpg", "Op4.jpg", operator04, 300, 0)
    Card("Free Education and Shelters for Homeless Children", "Op5.jpg", "Op5.jpg", operator05, 400, 0)
    Card("Rental Price Ceiling", "Op6.png", "Op6.png", operator06, 500, 0)
    Card("Rental Price Ceiling", "Op7.png", "Op7.png", operator07, 600, 0)
    Card("Rental Price Ceiling", "Op8.jpg", "Op8.jpg", operator08, 700, 0)
    Card("Rental Price Ceiling", "Op9.jpg", "Op9.jpg", operator09, 800, 0)
    Card("Rental Price Ceiling", "Op10.jpg", "Op10.jpg", operator10, 0, 150)
    Card("Rental Price Ceiling", "Op11.jpg", "Op11.jpg", operator11, 100, 150)
    Card("Rental Price Ceiling", "Op12.png", "Op12.png", operator12, 200, 150)
    Card("Rental Price Ceiling", "Op13.png", "Op13.png", operator13, 300, 150)
    Card("Rental Price Ceiling", "Op14.jpg", "Op14.jpg", operator14, 400, 150)
    Card("Rental Price Ceiling", "Op15.png", "Op15.png", operator15, 500, 150)
    Card("Rental Price Ceiling", "Op16.jpg", "Op16.jpg", operator16, 600, 150)
    Card("Rental Price Ceiling", "Op17.png", "Op17.png", operator17, 700, 150)


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
