#<METADATA>
SOLUZION_VERSION = "0.2"
PROBLEM_NAME = "Instant Insanity"
PROBLEM_VERSION = "0.1"
PROBLEM_AUTHORS = ['Marco.Xu']
PROBLEM_CREATION_DATE = "29-JUL-2018"

#</METADATA>

#<COMMON_DATA>
#</COMMON_DATA>

#<COMMON_CODE>

import random
from collections import deque
#Red 0 Green 1 Blue 2 White 3
#
#Cube face
#  Pitch
#    _5_
# |1|2(Yaw)|3|4 Roll
#    _6_
#
#
colors=["Red","Green","Blue","White"]

class Cube:
  def __init__(self):
    self.faces=[0,0,0,0,0,0]
    colorcount=[0,0,0,0]
    for i in range(6):
      color=random.randint(0,3)
      while colorcount[color]>=2:
        color=random.randint(0,3)
      self.faces[i]=color
      colorcount[color]+=1

  def yawrotate(self,isClockWise):
    yawindexs0=[0,4,2,5]
    if isClockWise:
      yawindexs1=[4,2,5,0]
    else:
      yawindexs1=[5,0,2,4]
    temp=[0,0,0,0]
    for i in range(4):
      temp[i]=self.faces[yawindexs0[i]]
    for i in range(4):
      self.faces[yawindexs1[i]]=temp[i]

  def pitchrotate(self,isClockWise):
    pitchindexs0=[0,1,2,3]
    if isClockWise:
      pitchindexs1=[1,2,3,0]
    else:
      pitchindexs1=[3,0,1,2]
    temp=[0,0,0,0]
    for i in range(4):
      temp[i]=self.faces[pitchindexs0[i]]
    for i in range(4):
      self.faces[pitchindexs1[i]]=temp[i]
    
  def rollrotate(self,isClockWise):
    rollindexs0=[1,5,3,4]
    if isClockWise:
      rollindexs1=[5,3,4,1]
    else:
      rollindexs1=[4,1,5,3]
    temp=[0,0,0,0]
    for i in range(4):
      temp[i]=self.faces[rollindexs0[i]]
    for i in range(4):
      self.faces[rollindexs1[i]]=temp[i]
  def __str__(self):
    return "\n      ["+colors[self.faces[4]]+"]\n"+"["+colors[self.faces[0]]+"]"+\
      "["+colors[self.faces[1]]+"]"+"["+colors[self.faces[2]]+"]"+"["+colors[self.faces[3]]+"]"+\
        "\n      ["+colors[self.faces[5]]+"]\n"
  def __hash__(self):
    return (str(self)).__hash__()

#Face 4 is default downside
class State:
  def __init__(self, old=None):
    self.cubes=[Cube() for i in range(4)]
    if old:
      self.cube=old.cube
  def can_move(self):
    return True

  def move(self,cubeindex,rotateyaw,rotatepitch,rotateroll):
    new = State(old=self)
    new.cubes[cubeindex].yawrotate(rotateyaw)
    new.cubes[cubeindex].yawrotate(rotatepitch)
    new.cubes[cubeindex].yawrotate(rotateroll)

    return new
  def countcolors(side):
    return 0
  def describe_state(self):
    # Produces a textual description of a state.
    # Might not be needed in normal operation with GUIs.
    return str(self)

  def is_goal(self):
    colorcounts=[0,0,0,0]
    for i in range(4):
      for cube in self.cubes:
        colorcounts[cube.faces[i]]+=1

  def __eq__(self, s2):
    return self.__hash__()==s2.__hash__()

  def __str__(self):
    string=""
    for cube in cubes:
      string.join(str(cube))
    return string

  def __hash__(self):
    return (str(self)).__hash__()

def goal_test(s): return s.is_goal()

def goal_message(s):
  return "Congratulations on successfully guiding fox, chicken, grain, and farmer across the river!"

def copy_state(s):
  return State(old=s)

class Operator:
  def __init__(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)
#</COMMON_CODE>

#<INITIAL_STATE>
INITIAL_STATE = State()
#</INITIAL_STATE>

#<OPERATORS>
phi0 = Operator("Farmer crosses alone",
  lambda s: s.can_move(False,False,False),
  lambda s: s.move(False,False,False))

phi1 = Operator("Farmer crosses the river with fox",
  lambda s: s.can_move(True,False,False),
  lambda s: s.move(True,False,False))

phi2 = Operator("Farmer crosses the river with chicken",
  lambda s: s.can_move(False,True,False),
  lambda s: s.move(False,True,False))

phi3 = Operator("Farmer crosses the river with grain",
  lambda s: s.can_move(False,False,True),
  lambda s: s.move(False,False,True))


OPERATORS = [phi0, phi1, phi2, phi3]
#</OPERATORS>

#<GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>

#<STATE_VIS>

#</STATE_VIS>

def test():
    pass

if __name__=="__main__":
    test()