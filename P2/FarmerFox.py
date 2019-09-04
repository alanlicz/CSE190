#<METADATA>
SOLUZION_VERSION = "0.2"
PROBLEM_NAME = "The Farmer, the Fox, the Chicken, and the Grain"
PROBLEM_VERSION = "0.1"
PROBLEM_AUTHORS = ['Marco.Xu']
PROBLEM_CREATION_DATE = "28-JUL-2019"

#</METADATA>

#<COMMON_DATA>
#</COMMON_DATA>

#<COMMON_CODE>


class State:
  def __init__(self, old=None):
    # Default new state is a state objects initialized as the
    # initial state.
    # If called with old equal to a non-empty state, then
    # the new instance is made to be a copy of that state.
    self.fox_on_right = False
    self.chicken_on_right = False
    self.grain_on_right = False
    self.boat_on_right=False

    if not old is None:
      self.fox_on_right = old.fox_on_right
      self.chicken_on_right = old.chicken_on_right
      self.grain_on_right = old.grain_on_right
      self.boat_on_right = old.boat_on_right

  def can_move(self,mvfox,mvchicken,mvgrain):
    '''Tests whether it's legal to move the boat alone 
or with fox or chicken or grain.'''
    if (self.fox_on_right==self.chicken_on_right):
        if self.boat_on_right!=self.fox_on_right:
            return False
    if (self.chicken_on_right==self.grain_on_right):
        if self.boat_on_right!=self.chicken_on_right:
            return False

    fox_on_right=self.fox_on_right ^ mvfox
    chicken_on_right=self.chicken_on_right ^ mvchicken
    grain_on_right=self.grain_on_right ^ mvgrain
    boat_on_right=self.boat_on_right ^ True

    if (fox_on_right==chicken_on_right):
        if boat_on_right!=fox_on_right:
            return False
    if (chicken_on_right==grain_on_right):
        if boat_on_right!=chicken_on_right:
            return False
    return True

  def move(self,mvfox,mvchicken,mvgrain):
    '''Assuming it's legal to make the move, this make a new state
    representing the result of moving the boat carrying
    m missionaries and c cannibals.'''
    news = State(old=self) # Make a copy of the current state.
    news.fox_on_right=news.fox_on_right ^ mvfox
    news.chicken_on_right=news.chicken_on_right ^ mvchicken
    news.grain_on_right=news.grain_on_right ^ mvgrain
    news.boat_on_right=news.boat_on_right ^ True
    return news

  def describe_state(self):
    # Produces a textual description of a state.
    # Might not be needed in normal operation with GUIs.
    txt = "Fox is on the "+"right\n" if self.fox_on_right else "left\n"
    txt += "Chicken is on the "+"right\n" if self.chicken_on_right else "left\n"
    txt += "Grain is on the "+"right\n" if self.grain_on_right else "left\n"
    txt += "Boat is on the "+"right\n" if self.boat_on_right else "left\n"
    txt += " Farmer is on the "+"right\n" if self.boat_on_right else "left\n"
    return txt

  def is_goal(self):
    '''If all Ms and Cs are on the right, then s is a goal state.'''
    return self.fox_on_right and self.chicken_on_right and self.grain_on_right and self.boat_on_right

  def __eq__(self, s2):
    if s2==None: return False
    if self.fox_on_right != s2.chicken_on_right: return False
    if self.chicken_on_right != s2.chicken_on_right: return False
    if self.grain_on_right != s2.grain_on_right: return False
    if self.boat_on_right != s2.boat_on_right: return False
    return True

  def __str__(self):
    st = '('+"Fox:"+("Right" if self.fox_on_right else "Left")
    st += ','+" Chicken:"+("Right" if self.chicken_on_right else "Left")
    st += ','+" Grain:"+("Right" if self.grain_on_right else "Left")
    st += ','+" Farmer:"+("Right" if self.boat_on_right else "Left")
    st += ','+" Boat:"+("Right" if self.boat_on_right else "Left")
    st += ')'
    return st

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