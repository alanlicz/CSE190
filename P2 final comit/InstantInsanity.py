# <METADATA>
SOLUZION_VERSION = "0.2"
PROBLEM_NAME = "Instant Insanity"
PROBLEM_VERSION = "0.1"
PROBLEM_AUTHORS = ['Marco.Xu', 'Alan Li', 'Ethan Jiang']
PROBLEM_CREATION_DATE = "04-SEP-2019"

# </METADATA>

# <COMMON_DATA>
colors = ["Red", "Green", "Blue", "White"]
# </COMMON_DATA>

# <COMMON_CODE>

import random
from collections import deque


# Red 0 Green 1 Blue 2 White 3
#
# Cube face
#
# Yaw clockwise:0 to 4 to 2 to 5
# Pitch clockwise:0
#  Pitch
#    _4_
# |0|1(Yaw)|2|3 Roll
#    _5_
#
#

class Cube:
    def __init__(self, old=None):
        self.faces = [0, 0, 0, 0, 0, 0]
        color_count = [0, 0, 0, 0]
        for i in range(6):
            color = random.randint(0, 3)
            while color_count[color] >= 2:
                color = random.randint(0, 3)
            # if a cube already has 2 same color faces, change the color.
            self.faces[i] = color
            color_count[color] += 1
        if old:
            self.faces = old.faces[:]

    def yawRotate(self, is_clockwise):
        yaw_index_s0 = [0, 4, 2, 5]
        # two faces will not change during the rotation, so there are only 4 elements
        if is_clockwise:
            yaw_index_s1 = [5, 0, 4, 2]
            temp = [0, 0, 0, 0]
            for i in range(4):
                temp[i] = self.faces[yaw_index_s1[i]]
            for i in range(4):
                self.faces[yaw_index_s0[i]] = temp[i]

    def rollRotate(self, isClockWise):
        pitch_index_s0 = [0, 1, 2, 3]
        if isClockWise:
            pitch_index_s1 = [3, 0, 1, 2]
            temp = [0, 0, 0, 0]
            for i in range(4):
                temp[i] = self.faces[pitch_index_s1[i]]
            for i in range(4):
                self.faces[pitch_index_s0[i]] = temp[i]

    def pitchRotate(self, isForward):
        roll_index_s0 = [1, 4, 3, 5]
        if isForward:
            roll_index_s1 = [5, 1, 4, 3]
            temp = [0, 0, 0, 0]
            for i in range(4):
                temp[i] = self.faces[roll_index_s1[i]]
            for i in range(4):
                self.faces[roll_index_s0[i]] = temp[i]

    def __str__(self):
        return "\n      [" + colors[self.faces[4]] + "]\n" + "[" + colors[self.faces[0]] + "]" + \
               "[" + colors[self.faces[1]] + "]" + "[" + colors[self.faces[2]] + "]" + "[" + colors[
                   self.faces[3]] + "]" + \
               "\n      [" + colors[self.faces[5]] + "]"

    def __hash__(self):
        return (str(self)).__hash__()


# Face 4 is default downside
class State:
    def __init__(self, old=None):
        if old:
            self.cubes = [Cube(old.cubes[i]) for i in range(4)]
        else:
            self.cubes = [Cube() for i in range(4)]

    @staticmethod
    def canMove():
        return True

    def move(self, cube_index, rotate_yaw, rotate_pitch, rotate_roll):
        """-1 for counterclockwise rotation, 0 for not rotating, 1 for clockwise rotation"""
        new = State(old=self)
        new.cubes[cube_index].yawRotate(rotate_yaw)
        new.cubes[cube_index].pitchRotate(rotate_pitch)
        new.cubes[cube_index].rollRotate(rotate_roll)

        return new

    def describe_state(self):
        # Produces a textual description of a state.
        # Might not be needed in normal operation with GUIs.
        return str(self)

    def is_goal(self):
        for i in range(4):
            color_counts = [0, 0, 0, 0]
            for cube in self.cubes:
                color_counts[cube.faces[i]] += 1
            for c in color_counts:
                if c > 1:
                    return False
        return True

    def isGoal(self):
        return self.is_goal()

    def __eq__(self, s2):
        return self.__hash__() == s2.__hash__()

    def __str__(self):
        string = ""
        for cube in self.cubes:
            string = string + str(cube)
        return string

    def __hash__(self):
        return (str(self)).__hash__()


def goal_test(s): return s.is_goal()


def goal_message(s):
    return "Congratulations on solving Instant Insanity!"


def copy_state(s):
    return State(old=s)


class Operator:
    def __init__(self, name, pre_cond, state_trans):
        self.name = name
        self.pre_cond = pre_cond
        self.state_trans = state_trans

    def is_applicable(self, s):
        return self.pre_cond(s)

    def apply(self, s):
        return self.state_trans(s)


# </COMMON_CODE>

# <INITIAL_STATE>
INITIAL_STATE = State()
# </INITIAL_STATE>

OPERATORS = [Operator("Rotate First cube for 90 degree Clockwise in Yaw direction",
                      lambda s: s.canMove(),
                      lambda s: s.move(0, 1, 0, 0)),
             Operator("Rotate First cube for 90 degree Forward in Pitch direction",
                      lambda s: s.canMove(),
                      lambda s: s.move(0, 0, 1, 0)),
             Operator("Rotate First cube for 90 degree Clockwise in Roll direction",
                      lambda s: s.canMove(),
                      lambda s: s.move(0, 0, 0, 1)),
             Operator("Rotate Second cube for 90 degree Clockwise in Yaw direction",
                      lambda s: s.canMove(),
                      lambda s: s.move(1, 1, 0, 0)),
             Operator("Rotate Second cube for 90 degree Forward in Pitch direction",
                      lambda s: s.canMove(),
                      lambda s: s.move(1, 0, 1, 0)),
             Operator("Rotate Second cube for 90 degree Clockwise in Roll direction",
                      lambda s: s.canMove(),
                      lambda s: s.move(1, 0, 0, 1)),
             Operator("Rotate Third cube for 90 degree Clockwise in Yaw direction",
                      lambda s: s.canMove(),
                      lambda s: s.move(2, 1, 0, 0)),
             Operator("Rotate Third cube for 90 degree Forward in Pitch direction",
                      lambda s: s.canMove(),
                      lambda s: s.move(2, 0, 1, 0)),
             Operator("Rotate Third cube for 90 degree Clockwise in Roll direction",
                      lambda s: s.canMove(),
                      lambda s: s.move(2, 0, 0, 1)),
             Operator("Rotate Fourth cube for 90 degree Clockwise in Yaw direction",
                      lambda s: s.canMove(),
                      lambda s: s.move(3, 1, 0, 0)),
             Operator("Rotate Fourth cube for 90 degree Forward in Pitch direction",
                      lambda s: s.canMove(),
                      lambda s: s.move(3, 0, 1, 0)),
             Operator("Rotate Fourth cube for 90 degree Clockwise in Roll direction",
                      lambda s: s.canMove(),
                      lambda s: s.move(3, 0, 0, 1))]
# </OPERATORS>

# <GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
# </GOAL_TEST>

# <GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)


# </GOAL_MESSAGE_FUNCTION>

# <STATE_VIS>

# </STATE_VIS>

def test():
    pass


if __name__ == "__main__":
    test()
