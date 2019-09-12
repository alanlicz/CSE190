# <METADATA>
SOLUZION_VERSION = "0.2"
PROBLEM_NAME = "Homeless"
PROBLEM_VERSION = "0.1"
PROBLEM_AUTHORS = ['Marco.Xu', 'Alan Li', 'Ethan Jiang']
PROBLEM_CREATION_DATE = "10-SEP-2019"

# </METADATA>

# <COMMON_DATA>
grant_monthly = 10000000
housing_price_threshold = 500
health_points_threshold = 20
money_threshold = 0
employment_threshold = 0
popularity_threshold = 25
homeless_people_count_threshold = 1000


# </COMMON_DATA>

# <COMMON_CODE>


class State:
    def __init__(self, old=None):
        # Default new state is a state objects initialized as the
        # initial state.
        # If called with old equal to a non-empty state, then
        # the new instance is made to be a copy of that state.
        self.money = 5000000
        self.housing_price = 400
        self.health_points = 50
        self.employment_rate = 5
        self.popularity = 60
        self.homeless_people = 10000
        self.housing_price_change_factor = 1.0
        self.health_change_factor = 1.0
        self.employment_change_factor = 1.0
        self.homeless_people_change_factor = 1.0
        self.popularity_change_factor = 1.0

        if old is not None:
            self.money = old.money
            self.housing_price = old.housing_price
            self.health_points = old.health_points
            self.employment_rate = old.employment_rate
            self.popularity = old.popularity
            self.homeless_people = old.homeless_people
            self.housing_price_change_factor = old.housing_price_change_factor
            self.health_change_factor = old.health_change_factor
            self.employment_change_factor = 1.0
            self.homeless_people_change_factor = 1.0
            self.popularity_change_factor = 1.0

    def can_move(self, money, employment_factor,
                 health_change_factor, popularity):
        if (self.money+1000000) + money <= 0:
            return False
        if self.employment_change_factor + employment_factor <= 0:
            return False
        if self.health_change_factor + health_change_factor <= 0.2:
            return False
        if self.popularity + popularity <= 0.2:
            return False
        return True

    def move(self, money, employment_factor, popularity,
             homeless_people, health_change_factor, homeless_people_change_factor):
        news = State(old=self)
        # Make a copy of the current state.
        news.money += money
        news.money += 1000000
        news.housing_price *= housing_price_change_factor
        news.health_points *= housing_price
        news.employment_rate *= employment_factor
        news.popularity += popularity
        news.homeless_people += homeless_people
        news.housing_price
        news.health_change_factor += health_change_factor
        news.homeless_people_change_factor += homeless_people_change_factor
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
