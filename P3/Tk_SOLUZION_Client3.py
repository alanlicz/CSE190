#!/usr/bin/python3
"""Tk_SOLUZION_Client3.py
    Works with the example files
       Missionaries3.py
         and
       Missionaries3_VIS_FOR_TK3.py.

Differences from Tk_SOLUZION_Client.py:

1. Allows putting image file names in the array of colors
  that was used in show_state_array.py, and attempts to
  show the image, loading it into Tkinter if it has not already been
  loaded and converted to a PhotoImage object.
  (So in each element of the array of colors, you can either have
  a color, given as an rgb triple as before, or a string giving an image filename.)

2. Does not use the shell for user input. All user input is
  in the Tkinter GUI window.  But diagnostic info and the help message still
  comes to the shell.

3. Operators are applied by selecting them from a drop-down "combo" box
  and then clicking on the "Apply" button.

4. Does not require a separate file show_state_array.py

Last updated 17 Sept. 2019. --Steve Tanimoto

    """

# global variables for the problem and solving process:

STEP = 0;
DEPTH = 0;
OPERATORS = [];
CURRENT_STATE = None;
STATE_STACK = []
APPLICABILITY_VECTOR = []

problem_name = 'Homelessness3'  # Default problem name. Edit or give a command-line parameter to change it.


def compute_applicability_vector():
    global CURRENT_STATE, APPLICABILITY_VECTOR
    APPLICABILITY_VECTOR = [op.is_applicable(CURRENT_STATE) for op in OPERATORS]


def show_instructions():
    tkprint('''\nINSTRUCTIONS:\n
The current state of your problem session represents where you
are in the problem-solving process.  You can try to progress
forward by applying an operator to change the state.
To do this, type the number of an applicable operator.
The program shows you a list of what operators are 
applicable in the current state.

You can also go backwards (undoing a previous step)
by typing 'B'.  

If you reach a goal state, you have solved the problem,
and the computer will usually tell you that, but it depends
on what kind of problem you are solving.''')


'''      
def apply_one_op():
    """Populate a popup menu with the names of currently applicable
       operators, and let the user choose which one to apply."""
    currently_applicable_ops = applicable_ops(CURRENT_STATE)
    #print "Applicable operators: ",\
    #    map(lambda o: o.name, currently_applicable_ops)
    #print("Now need to apply the op")

def applicable_ops(s):
    """Returns the subset of OPERATORS whose preconditions are
       satisfied by the state s."""
    return [o for o in OPERATORS if o.is_applicable(s)]
'''
# Define the general infrastructure for visualizations.
import tkinter as tk
from tkinter import ttk

# PIL is from the Pillow package. Needed to convert jpg images to PhotoImages,
# and for resizing images.
from PIL import Image as PIL_Image
from PIL import ImageTk as PIL_ImageTk

STATE_WINDOW = None
THE_CANVAS = None
CAPTION = None
LOWER_GUI_PART = None
ROOT = None


def initialize_tk(title="Tk_SOLUZION_Client3"):
    global ROOT, STATE_WINDOW, THE_CANVAS, CAPTION
    ROOT = tk.Tk()
    ROOT.title(title)
    STATE_WINDOW = tk.Frame(ROOT, width=1, height=1)
    STATE_WINDOW.pack()
    print("Generic VIS initialization finished")


def get_choices(self):
    "This makes sure that only legal operators (for the current state) are shown in the combo box."
    global APPLICABILITY_VECTOR, OPERATORS
    new_values = [(str(i) + ": " + OPERATORS[i].name) for i in range(len(OPERATORS)) if APPLICABILITY_VECTOR[i]]
    new_values += ["H: Help", "B: Back", "Q: Quit"]
    return new_values


def take_turn(command):
    global CURRENT_STATE, STATE_STACK, DEPTH, STEP, OPERATORS, APPLICABILITY_VECTOR
    global ROOT
    # print("In take_turn, command is: "+command)
    if command == "B" or command == "b":
        if len(STATE_STACK) > 1:
            STATE_STACK.pop()
            DEPTH -= 1
            STEP += 1
        else:
            tkprint("You're already back at the initial state.")
            return -1
        CURRENT_STATE = STATE_STACK[-1]
        PROBLEM.render_state(CURRENT_STATE)
        return -1

    if command == "H" or command == "h": show_instructions(); return -1
    if command == "Q" or command == "q": ROOT.destroy()
    if command == "": return -1
    if CURRENT_STATE.is_goal():
        PROBLEM.render_state(CURRENT_STATE)
        return 0
    try:
        i = int(command)
    except:
        tkprint("Unknown command or bad operator number.")
        return -1
    tkprint("Operator " + str(i) + " selected.")
    if i < 0 or i >= len(OPERATORS):
        tkprint("There is no operator with number " + str(i))
        return -1
    if APPLICABILITY_VECTOR[i]:
        CURRENT_STATE = OPERATORS[i].apply(CURRENT_STATE)
        STATE_STACK.append(CURRENT_STATE)
        PROBLEM.render_state(CURRENT_STATE)
        compute_applicability_vector()
        DEPTH += 1
        STEP += 1
        return 1
    else:
        tkprint("Operator " + str(i) + " is not applicable to the current state.")
        return -1
    # print("Operator "+command+" not yet supported.")


def tkprint(txt): print(txt)  # Could be changed to render text on the GUI.


# The following is only executed if this module is being run as the main
# program, rather than imported from another one.
if __name__ == '__main__':
    # Now import the problem formulation and the problem-specific visualization stuff.

    import sys, importlib.util

    # Get the PROBLEM name from the command-line arguments

    if len(sys.argv) < 2:
        """ The following few lines go with the LINUX version of the text client.
    print('''
         Usage: 
  ./IDLE_Text_SOLUZION_Client <PROBLEM NAME>
         For example:
  ./IDLE_Text_SOLUZION_Client Missionaries
    ''')
    exit(1)
    """
        sys.argv = ['Tk_SOLUZION_Client3.py', problem_name]  # IDLE and Tk version only.
        # Sets up sys.argv as if it were coming in on a Linux command line.

    problem_name = sys.argv[1]
    print("problem_name = " + problem_name)

    try:
        spec = importlib.util.spec_from_file_location(problem_name, problem_name + ".py")
        PROBLEM = spec.loader.load_module()
    except Exception as e:
        print(e)
        exit(1)

    try:
        print("Trying to import the vis file.")
        spec = importlib.util.spec_from_file_location(problem_name + '_VIS_FOR_TK3',
                                                      problem_name + '_VIS_FOR_TK3.py')
        VIS = spec.loader.load_module()

    except Exception as e:
        print(e)
        exit(1)

    OPERATORS = PROBLEM.OPERATORS
    STATE_STACK = []
    TITLE = "Tk_SOLUZION_Client (Version 3)"

    CURRENT_STATE = PROBLEM.State()
    STATE_STACK = [CURRENT_STATE]
    compute_applicability_vector()

    try:
        print("Trying to initialize the visualization")
        PROBLEM.render_state = VIS.render_state
        initialize_tk()
        VIS.initialize_vis(ROOT, CURRENT_STATE, get_choices, take_turn)
        PROBLEM.render_state(CURRENT_STATE)
    except Exception as e:
        print("Could not initialize the visualization.")
        print(e)

    STATE_WINDOW.mainloop()  # This lets Tk take over the event loop, show graphics, etc.
    print("The session is finished.")
