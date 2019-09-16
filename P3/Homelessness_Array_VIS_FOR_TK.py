import show_state_array as ssa
from show_state_array import initialize_tk, state_array, state_display, test
import tkinter as tk
from tkinter import font, PhotoImage
import os
import numpy as np
from PIL import Image, ImageDraw

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


def rgb2hex(rgb):
    return "#%02x%02x%02x" % rgb


table = None
money_bar = None
housing_price_bar = None
health_points_bar = None
employment_rate_bar = None
popularity_bar = None
homeless_people_bar = None
# money_bar_fill = None


def initialize_vis():
    global table

    global money_bar
    global housing_price_bar
    global health_points_bar
    global employment_rate_bar
    global popularity_bar
    global homeless_people_bar
    initialize_tk(WIDTH, HEIGHT, TITLE)
    table = ssa.STATE_WINDOW.canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill=rgb2hex(background))
    money_bar = StatusBar(700, 50, 200, 20, blue, green)
    housing_price_bar = StatusBar(700, 80, 200, 20, blue, yellow)
    health_points_bar = StatusBar(700, 110, 200, 20, blue, purple)
    employment_rate_bar = StatusBar(700, 140, 200, 20, blue, cyan)
    popularity_bar = StatusBar(700, 170, 200, 20, blue, orange)
    homeless_people_bar = StatusBar(700, 200, 200, 20, blue, tan)
    ssa.STATE_WINDOW.canvas.create_text(600, 60, text="Money")
    ssa.STATE_WINDOW.canvas.create_text(600, 90, text="Housing Price")
    ssa.STATE_WINDOW.canvas.create_text(600, 120, text="Health Points")
    ssa.STATE_WINDOW.canvas.create_text(600, 150, text="Employment Rate")
    ssa.STATE_WINDOW.canvas.create_text(600, 180, text="Popularity")
    ssa.STATE_WINDOW.canvas.create_text(600, 210, text="Homeless People")
    gif1 = PhotoImage(file='Op1.gif')
    # put gif image on canvas
    # pic's upper left corner (NW) on the canvas is at x=50 y=10
    ssa.STATE_WINDOW.canvas.create_image(50, 10, image=gif1, anchor=tk.NW)
    # img = PhotoImage(file="Op1.gif")
    # ssa.STATE_WINDOW.canvas.create_image(100, 100, image=img)


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
    money_bar.update(s.money / 15000000)
    housing_price_bar.update(s.housing_price / 2000)
    health_points_bar.update(s.health_points / 200)
    employment_rate_bar.update(s.employment_rate / 300)
    popularity_bar.update(s.popularity / 200)
    homeless_people_bar.update(s.homeless_people / 50000)


