import tkinter as tk
from tkinter import font, messagebox
from PIL import Image, ImageTk
import random
import os
import subprocess
import webbrowser

myFont = None
ROOT = None

MAP_FRAME = None
STATUSBAR_FRAME = None
MAP_CANVAS = None
STATUSBAR_CANVAS = None
GET_OPERATOR = None
STATE_TRANS_FUNCTION = None
GOAL_MESSAGE_FUNCTION = None
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
    def __init__(self, text, background_path, operator, x0=0, y0=0):
        global ROOT
        global MAP_FRAME
        global images
        global CARD_FRAME
        self.text = text
        self.background_image = Image.open(background_path)
        self.background_image = self.background_image.resize((100, 100), Image.ANTIALIAS)
        self.background_image = ImageTk.PhotoImage(self.background_image)
        images.append(self.background_image)
        self.operator = operator
        self.button = tk.Button(CARD_FRAME, image=self.background_image, command=operator, width=100, height=100)
        self.button.place(x=x0, y=y0)
        self.x0 = x0
        self.y0 = y0
        self.text_label = tk.Label(master=CARD_FRAME, text=text)
        self.text_label.place(x=x0+10, y=y0 + 110)


"""
class Button:
    def __init__(self, container, text, image):
        self.container = container
        self.text = text
        self.image = image
        # self.command = command
        self.button = tk.Button(master=self.container, text=self.text, image=self.image)
        self.button.tk.place()
"""

images = []  # Store images to keep references to images to prevent garbage collection

table = None
money_bar = None
housing_price_bar = None
health_points_bar = None
employment_rate_bar = None
popularity_bar = None
homeless_people_bar = None
sf_map_gif = None
homeless_icon = None
homeless_items = []
homeless_items_downtown = []
HOMELESS_ITEMS_FACTOR = 80
CARD_FRAME = None
CARDS = []
BACK_BUTTON = None
QUIT_BUTTON = None


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


def back():
    global STATE_TRANS_FUNCTION
    return STATE_TRANS_FUNCTION("B")


def quit():
    global STATE_TRANS_FUNCTION
    return STATE_TRANS_FUNCTION("Q")


def render_homeless_map(homeless_percentage):
    global MAP_CANVAS
    global homeless_items
    global homeless_icon
    global HOMELESS_ITEMS_FACTOR
    global homeless_items_downtown
    if int(HOMELESS_ITEMS_FACTOR * homeless_percentage) - len(homeless_items) >= 0:
        for i in range(0, int(HOMELESS_ITEMS_FACTOR * homeless_percentage) - len(homeless_items)):
            homeless_items.append(MAP_CANVAS.create_image(int(random.uniform(40, 380)), int(random.uniform(170, 500)),
                                                          image=homeless_icon))
    else:
        for i in range(0, len(homeless_items) - int(HOMELESS_ITEMS_FACTOR * homeless_percentage)):
            index = int(random.uniform(0, len(homeless_items) - 1))
            MAP_CANVAS.delete(homeless_items[index])
            del homeless_items[index]

    if int(HOMELESS_ITEMS_FACTOR * homeless_percentage) - len(homeless_items_downtown) >= 0:
        for i in range(0, int(HOMELESS_ITEMS_FACTOR * homeless_percentage) - len(homeless_items_downtown)):
            homeless_items_downtown.append(
                MAP_CANVAS.create_image(int(random.uniform(180, 380)), int(random.uniform(120, 320)),
                                        image=homeless_icon))
    else:
        for i in range(0, len(homeless_items_downtown) - int(HOMELESS_ITEMS_FACTOR * homeless_percentage)):
            index = int(random.uniform(0, len(homeless_items_downtown)))
            MAP_CANVAS.delete(homeless_items_downtown[index])
            del homeless_items_downtown[index]


def initialize_vis(root, current_state, get_operator, state_trans_function):
    global ROOT
    global table
    global images
    global sf_map_gif
    global money_bar
    global housing_price_bar
    global health_points_bar
    global employment_rate_bar
    global popularity_bar
    global homeless_people_bar
    global MAP_CANVAS
    global STATUSBAR_CANVAS
    global MAP_FRAME
    global STATUSBAR_FRAME
    global STATE_TRANS_FUNCTION
    global GET_OPERATOR
    global homeless_icon
    global CARD_FRAME
    global CARDS
    global BACK_BUTTON
    global QUIT_BUTTON
    global GOAL_MESSAGE_FUNCTION
    STATE_TRANS_FUNCTION = state_trans_function
    GET_OPERATOR = get_operator
    GOAL_MESSAGE_FUNCTION = current_state.goal_message

    try:
        sf_map_gif = Image.open("SFMap.png")
        sf_map_gif = sf_map_gif.resize((500, 500), Image.ANTIALIAS)
        sf_map_gif = ImageTk.PhotoImage(sf_map_gif)
    except Exception as e:
        print("Failed to Load SF Map!")
        print(e)
    images.append(sf_map_gif)  # Store images to keep references to images to prevent garbage collection

    ROOT = root
    MAP_FRAME = tk.Frame(master=ROOT, width=900, height=270)
    MAP_FRAME.pack()
    CARD_FRAME = tk.Frame(master=ROOT, width=1600, height=400)
    CARD_FRAME.pack()
    MAP_CANVAS = tk.Canvas(master=MAP_FRAME, width=sf_map_gif.width(), height=sf_map_gif.height())
    MAP_CANVAS.pack(side=tk.LEFT)
    MAP_CANVAS.create_image(0, 0, image=sf_map_gif, anchor=tk.NW)

    homeless_icon = Image.open("icon.jpg")
    homeless_icon = homeless_icon.resize((5, 10), Image.ANTIALIAS)
    homeless_icon = ImageTk.PhotoImage(homeless_icon)
    images.append(homeless_icon)
    STATUSBAR_CANVAS = tk.Canvas(master=MAP_FRAME, width=900, height=300)
    STATUSBAR_CANVAS.pack(side=tk.RIGHT)

    # table = STATUSBAR_CANVAS.create_rectangle(0, 0, 900, 300, fill=rgb2hex(background))
    money_bar = StatusBar("Money", 120, 20, 200, 20, blue, green)
    housing_price_bar = StatusBar("Housing Price", 120, 50, 200, 20, blue, yellow)
    health_points_bar = StatusBar("Health Points", 120, 80, 200, 20, blue, purple)
    employment_rate_bar = StatusBar("Employment Rate", 120, 110, 200, 20, blue, cyan)
    popularity_bar = StatusBar("Popularity", 120, 140, 200, 20, blue, orange)
    homeless_people_bar = StatusBar("Homeless People", 120, 170, 200, 20, blue, tan)

    CARDS = [
        Card("Rental Price \nCeiling", "Op1.jpg", operator01, 20, 0),
        Card("Build Affordable \nHouses", "Op2.png", operator02, 150, 0),
        Card("Street Health \nTeam", "Op3.jpg", operator03, 300, 0),
        Card("Drugs Treatment", "Op4.jpg", operator04, 450, 0),
        Card("Free Education \nand Shelters", "Op5.jpg", operator05, 600, 0),
        Card("Free Job \nTraining", "Op6.png", operator06, 750, 0),
        Card("Provide Job \nOpportunities", "Op7.png", operator07, 900, 0),
        Card("Tax Increasing", "Op8.jpg", operator08, 1050, 0),
        Card("Tax Decreasing", "Op9.jpg", operator09, 1200, 0),
        Card("Provide Portable \nShelter", "Op10.jpg", operator10, 1350, 0),
        Card("Provide Places \nfor Homeless", "Op11.jpg", operator11, 20, 150),
        Card("Increase Minimum \nWage", "Op12.png", operator12, 150, 150),
        Card("Make Homeless \nPriority in Jobs", "Op13.png", operator13, 300, 150),
        Card("Low Price \nInsurance", "Op14.jpg", operator14, 450, 150),
        Card("Free College \nTuition", "Op15.png", operator15, 600, 150),
        Card("Provide Food \nfor Homelessness", "Op16.jpg", operator16, 750, 150),
        Card("Prepare For your \nSecond Term", "Op17.png", operator17, 900, 150)]

    BACK_BUTTON = tk.Button(master=CARD_FRAME, text="Back", width=10, command=back)
    BACK_BUTTON.place(x=1100, y=150)
    QUIT_BUTTON = tk.Button(master=CARD_FRAME, text="QUIT", width=10, command=quit)
    QUIT_BUTTON.place(x=1100, y=200)
    tk.messagebox.showinfo("1111", "Game title: Can You Solve Homelessness Issue in San Fransisco?\n \n"
                                   "In this game, you will act as the government to solve the homelessness issue in San"
                                   " Francisco. In each turn, you will be provided several choices which help you "
                                   "solve the issue. Try to solve the problem without being overthrown by voters "
                                   "or getting bankrupt.")
    # help_button = tk.Button(master=CARD_FRAME, text="help", width=10, command=webbrowser.open("111.txt"))
    # help_button.place(x=1250, y=200)


def click_on_file(filename="111.txt"):
    """Open document with default application in Python."""
    try:
        os.startfile(filename)
    except AttributeError:
        subprocess.call(['open', filename])


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
    employment_rate_bar.update(s.employment_rate / 100.0)
    popularity_bar.update(s.popularity / 100.0)
    homeless_people_bar.update(s.homeless_people / 25000.0)
    render_homeless_map(s.homeless_people / 15000)
    msg_box = tk.messagebox.askquestion('Game Message', 'Do you want to check the description for each operator?'
                                                        'Click yes if you want to.', icon='warning')
    # if msg_box == 'yes':
    #     webbrowser.open("111.txt")
    quarter_button = tk.Button(master=CARD_FRAME, text="Quarter count = " + str(s.quarter_num), width=20)
    quarter_button.place(x=1250, y=150)
    help_button = tk.Button(master=CARD_FRAME, text="HELP", command=click_on_file)
    help_button.place(x=1250, y=200)
    if s.is_goal():
        tk.messagebox.showerror("Game Message", s.goal_message())


