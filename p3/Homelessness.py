# <METADATA>
SOLUZION_VERSION = "0.2"
PROBLEM_NAME = "Homeless"
PROBLEM_VERSION = "0.1"
PROBLEM_AUTHORS = ['Marco.Xu', 'Alan Li', 'Ethan Jiang']
PROBLEM_CREATION_DATE = "10-SEP-2019"

# </METADATA>

# <COMMON_DATA>

# </COMMON_DATA>

# <COMMON_CODE>


class State:
    def __init__(self, old=None):
        # Default new state is a state objects initialized as the
        # initial state.
        # If called with old equal to a non-empty state, then
        # the new instance is made to be a copy of that state.

        if not old is None:
            pass

    # def can_move(self, policy):
    #     return True
    # Every move is considered as legal move

    def move(self, policy):
        news = State(old=self)
        # Make a copy of the current state.
        return news

    def describe_state(self):
        # Produces a textual description of a state.
        # Might not be needed in normal operation with GUIs.
        return self.__str__

    def is_goal(self):
        return False

    def isGoal(self):
        return self.is_goal()

    def __eq__(self, s2):
        return self.__hash__() == s2.__hash__()

    def __str__(self):
        st = ""
        return st

    def __hash__(self):
        return (str(self)).__hash__()


def goal_test(s): return s.is_goal()


def goal_message(s):
    return "Congratulations on successfully solving homeless problem!"


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


# </COMMON_CODE>

# <INITIAL_STATE>
INITIAL_STATE = State()
# </INITIAL_STATE>

# <OPERATORS>
OPERATORS = []
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
    test()  # <METADATA>
SOLUZION_VERSION = "0.2"
PROBLEM_NAME = "Homeless"
PROBLEM_VERSION = "0.1"
PROBLEM_AUTHORS = ['Marco.Xu', 'Alan Li', 'Ethan Jiang']
PROBLEM_CREATION_DATE = "10-SEP-2019"


# </METADATA>

# <COMMON_DATA>
# </COMMON_DATA>

# <COMMON_CODE>


class State:
    def __init__(self, old=None):
        # Default new state is a state objects initialized as the
        # initial state.
        # If called with old equal to a non-empty state, then
        # the new instance is made to be a copy of that state.

        if not old is None:
            pass

    def can_move(self, policy):
        return True

    def move(self, policy):
        news = State(old=self)  # Make a copy of the current state.
        return news

    def describe_state(self):
        # Produces a textual description of a state.
        # Might not be needed in normal operation with GUIs.
        return self.__str__

    def is_goal(self):
        return False

    def isGoal(self):
        return self.is_goal()

    def __eq__(self, s2):
        return self.__hash__() == s2.__hash__()

    def __str__(self):
        st = ""
        return st

    def __hash__(self):
        return (str(self)).__hash__()


def goal_test(s): return s.is_goal()


def goal_message(s):
    return "Congratulations on successfully solving homeless problem!"


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


# </COMMON_CODE>

# <INITIAL_STATE>
INITIAL_STATE = State()
# </INITIAL_STATE>

# <OPERATORS>
OPERATORS = []
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
