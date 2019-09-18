from tkinter import *
from PIL import ImageTk, Image


class CanvasDemo:
    def __init__(self):
        window = Tk()  # Create Window
        window.title("Canvas Demo")

        # Draw a canvas on the window
        self.canvas = Canvas(window, width=200, height=100, bg="white")
        self.canvas.pack()

        # Create frame and Window is the master
        frame = Frame(window)
        frame.pack()
        # frame is the master of all the buttons
        tempimg = Image.open("Op1.jpg")
        tempimg = tempimg.resize((100, 100), Image.ANTIALIAS)
        tempimg = ImageTk.PhotoImage(tempimg)
        btRectangle = Button(frame, text="rectangle", command=self.displayRect, image=tempimg)
        btOval = Button(frame, text="Oval", command=self.displayOval, fg="black")
        btArc = Button(frame, text="Arc", command=self.displayArc)
        btPolygon = Button(frame, text="Polygon", command=self.displayPolygon)
        btLine = Button(frame, text="Line", command=self.displayLine)
        btString = Button(frame, text="String", command=self.displayString)
        btClear = Button(frame, text="Clear", command=self.displayClear)

        # Edit the layout on the canvas
        btRectangle.grid(row=1, column=1)
        btOval.grid(row=1, column=2)
        btArc.grid(row=1, column=3)
        btPolygon.grid(row=1, column=4)
        btLine.grid(row=1, column=5)
        btString.grid(row=1, column=6)
        btClear.grid(row=1, column=7)

        window.mainloop()

    def displayRect(self):
        self.canvas.create_rectangle(10, 10, 190, 90, tags="rect")

    def displayOval(self):
        self.canvas.create_oval(10, 10, 190, 90, fill="red", tags="oval")

    # start represent the starting angle，extent is the degree you want to turn. Default counterclockwise
    def displayArc(self):
        self.canvas.create_arc(10, 10, 190, 90, start=0, extent=90, width=8, fill="red", tags="arc")

    def displayPolygon(self):
        self.canvas.create_polygon(10, 10, 190, 90, 10, 90, tags="polygon")

    # arrow indicate the direction，activefill：showing special style, when mouse move to the second line,
    # it will appear blue
    def displayLine(self):
        self.canvas.create_line(10, 10, 190, 90, fill="red", tags="line")
        self.canvas.create_line(10, 90, 190, 10, width=9, arrow="first", activefill="blue", tags="line")

    # font define the typeface(name, size, style)
    def displayString(self):
        self.canvas.create_text(60, 40, text="hi, i am string", font="time 10 bold underline", tags="string")

    # delete using tag argument to delete all the graph
    def displayClear(self):
        self.canvas.delete("rect", "oval", "arc", "polygon", "line", "string")


CanvasDemo()
