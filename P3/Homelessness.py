# <METADATA>
SOLUZION_VERSION = "3.0"
PROBLEM_NAME = "Homelessness"
PROBLEM_VERSION = "1.0"
PROBLEM_AUTHORS = ["Marco Xu", "Alan Li", "Sandy Zhang", "Ethan Jiang"]
PROBLEM_CREATION_DATE = "10-SEP-2019"

# </METADATA>

# <COMMON_DATA>
housing_price_threshold = 500
health_points_threshold = 20
money_threshold = 10000
employment_threshold = 0
popularity_threshold = 5
homeless_people_threshold = 2500

homeless_uncertainty = 0.1
money_uncertainty = 0.1
housing_price_uncertainty = 0.1
health_points_uncertainty = 0.2
popularity_uncertainty = 0.1
employment_rate_uncertainty = 0.1

homeless_money_externality_factor = 0.1
homeless_popularity_externality_factor = 0.1
housing_homeless_price_externality_factor = 0.1
housing_popularity_price_externality_factor = 0.1

homeless_money_externality_baseline = 5000
homeless_popularity_externality_baseline = 6000
# </COMMON_DATA>

# <COMMON_CODE>
import random


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
        self.homeless_people = 14449
        self.quarter_num = 1
        self.second_term_flag = False
        if old is not None:
            self.money = old.money
            self.housing_price = old.housing_price
            self.health_points = old.health_points
            self.employment_rate = old.employment_rate
            self.popularity = old.popularity
            self.homeless_people = old.homeless_people
            self.quarter_num = old.quarter_num + 1
            self.second_term_flag = old.second_term_flag

    def can_move(self, money_adjustment, housing_price_adjustment, health_points_adjustment,
                 employment_rate_adjustment, popularity_adjustment, homeless_people_adjustment):
        # if self.money + 1000000 + money_adjustment <= 0:
        #     return False
        # if self.employment_rate + employment_rate_adjustment <= 0:
        #     return False
        # if self.health_points + health_points_adjustment <= 15:
        #     return False
        # if self.popularity + popularity_adjustment <= 20:
        #     return False
        # if self.housing_price + housing_price_adjustment > 800:
        #     return False
        # if self.homeless_people + homeless_people_adjustment > 12000:
        #     return False
        # Check whether the move will result in game failure
        return True

    def move(self, money_adjustment, housing_price_adjustment, health_points_adjustment,
             employment_rate_adjustment, popularity_adjustment, homeless_people_adjustment, uncertainty=1.0):
        news = State(old=self)
        # Make a copy of the current state.
        news.money += money_adjustment
        news.money += 250000
        news.money += news.money * random.uniform(-money_uncertainty, money_uncertainty) * uncertainty
        news.housing_price += housing_price_adjustment
        news.housing_price += news.housing_price * random.uniform(-housing_price_uncertainty,
                                                                  housing_price_uncertainty) * uncertainty
        news.health_points += health_points_adjustment
        news.health_points += news.health_points * random.uniform(-health_points_uncertainty,
                                                                  health_points_uncertainty) * uncertainty
        news.employment_rate += employment_rate_adjustment
        news.employment_rate += news.employment_rate * random.uniform(-employment_rate_uncertainty,
                                                                      employment_rate_uncertainty) * uncertainty
        news.popularity += popularity_adjustment
        news.popularity += news.popularity * random.uniform(-popularity_uncertainty,
                                                            popularity_uncertainty) * uncertainty
        news.homeless_people += homeless_people_adjustment
        news.homeless_people += news.homeless_people * random.uniform(-homeless_uncertainty,
                                                                      homeless_uncertainty) * uncertainty
        news.money = 0 if news.money < 0 else news.money
        news.housing_price = 0 if news.housing_price < 0 else news.housing_price
        news.health_points = 0.0 if news.health_points < 0 else news.health_points
        news.employment_rate = 0.0 if news.employment_rate < 0 else news.employment_rate
        news.popularity = 0.0 if news.popularity < 0 else news.popularity
        news.popularity = 100.0 if news.popularity > 100.0 else news.popularity
        news.homeless_people = 0.0 if news.homeless_people < 0.0 else news.homeless_people
        return news

    def enable_second_term(self):
        self.second_term_flag = True
        return self

    def isGoal(self):
        # Check if you have reached a goal state
        if self.quarter_num >= 16 and not (self.popularity <= 0.6 or (not self.second_term_flag)):
            return True
        if self.quarter_num >= 32:
            return True
        if self.money < money_threshold:
            return True
        if self.popularity <= popularity_threshold:
            return True
        return False

    def is_goal(self):
        # Check if you have reached a goal state
        if self.quarter_num >= 16 and not (self.popularity <= 0.6 or (not self.second_term_flag)):
            return True
        if self.quarter_num >= 32:
            return True
        if self.money < money_threshold:
            return True
        if self.popularity <= popularity_threshold:
            return True
        return False

    def goal_message(self):
        if self.money < money_threshold:
            return "Your government is Bankrupted!"
        if self.popularity <= popularity_threshold:
            return "Your people are disappointed in you and legislators has passed the Impeachment Bill!\n" \
                   "You are Thrown Out of Office!"

        if self.quarter_num >= 16 and not (self.popularity <= 60 or (not self.second_term_flag)):
            return "You Stepped Down after your First term\n" + (
                "You Successfully solved homeless problem!" if self.homeless_people <= homeless_people_threshold
                else "You Failed to solve homeless problem")
        if self.quarter_num >= 32:
            return "You Stepped Down after your Second term\n" + (
                "You Successfully solved homeless problem!" if self.homeless_people <= homeless_people_threshold
                else "You Failed to solve homeless problem")

    def __eq__(self, s2):
        if s2 == None:
            return False
        if self.homeless_people != s2.homeless_people:
            return False
        if self.popularity != s2.popularity:
            return False
        if self.employment_rate != s2.employment_rate:
            return False
        if self.health_points != s2.health_points:
            return False
        if self.housing_price != s2.housing_price:
            return False
        if self.money != s2.money:
            return False
        return True

    def __str__(self):
        # Produces a textual description of a state.
        # Might not be needed in normal operation with GUIs.
        txt = "This is your " + str(self.quarter_num) + " quarters in office."
        txt += "\nThe fund is now " + "{:.1f}".format(self.money) + " dollars.\n"
        txt += "The housing price is now " + "{:.1f}".format(self.housing_price) + " dollars per month\n"
        txt += "The health points is now " + "{:.1f}".format(self.health_points) + ".\n"
        txt += "The employment rate is now " + "{:.1f}".format(self.employment_rate) + " percent.\n"
        txt += "Your popularity is now " + "{:.1f}".format(self.popularity) + " percent.\n"
        txt += "There are " + "{:.0f}".format(self.homeless_people) + " homeless people.\n"
        return txt

    def __hash__(self):
        return (str(self)).__hash__()


def goal_message(s):
    return ""


def goal_test(s): return s.isGoal()


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
OPERATORS = [Operator("Housing: Rental Price Ceiling",
                      lambda s: s.can_move(-1000000, -100, 5, 0, 10, 0),
                      lambda s: s.move(-1000000, -100, 5, 0, 10, 0, uncertainty=0.9)),
             # Test can_move function. Note that money variable has changed.

             Operator("Housing: Build Affordable Houses",
                      lambda s: s.can_move(-500000, -100, 5, 0, 10, -1000),
                      lambda s: s.move(-500000, -100, 5, 0, 10, -1000)),
             # Test isGoal function

             Operator("Health: Street Health Care Team",
                      lambda s: s.can_move(-300000, 0, 15, 0, 5, 0),
                      lambda s: s.move(-300000, 0, 15, 0, 5, 0)),

             Operator("Health: Drugs Users Treatment",
                      lambda s: s.can_move(-250000, 0, 10, 0, 10, 0),
                      lambda s: s.move(-250000, 0, 10, 0, 10, 0)),

             Operator("Eduction: Free Education and Shelters for Homeless Children",
                      lambda s: s.can_move(-800000, 0, 0, 5, 20, -1000),
                      lambda s: s.move(-800000, 0, 0, 5, 20, -1000)),

             Operator("Job: Free Job Training",
                      lambda s: s.can_move(-800000, -50, 5, 10, 5, -1000),
                      lambda s: s.move(-800000, -50, 5, 10, 5, -1000)),

             Operator("Job: Provide Job Opportunities for Homelessness People",
                      lambda s: s.can_move(-400000, -50, 5, 10, -15, -1500),
                      lambda s: s.move(-400000, -50, 5, 10, -15, -1500)),

             Operator("Financial: Tax Increasing",
                      lambda s: s.can_move(1000000, 0, 0, 0, -20, 0),
                      lambda s: s.move(1000000, 0, 0, 0, -20, 0)),

             Operator("Financial: Tax Decreasing",
                      lambda s: s.can_move(-500000, 0, 0, 0, 15, 0),
                      lambda s: s.move(-500000, 0, 0, 0, 15, 0)),

             Operator("Housing: Provide Portable Shelter",
                      lambda s: s.can_move(-50000, 0, 5, 0, -5, 0),
                      lambda s: s.move(-50000, 0, 5, 0, -5, 0)),

             Operator("Housing: Provide Gathering Place for Homeless",
                      lambda s: s.can_move(-100000, 0, 5, 0, 5, 0),
                      lambda s: s.move(-100000, 0, 5, 0, 5, 0)),

             Operator("Financial: Increase Minimum Wage",
                      lambda s: s.can_move(-2000000, -50, 0, -5, 10, 0),
                      lambda s: s.move(-2000000, -50, 0, -5, 10, 0)),

             Operator("Job: Make Homelessness Has Priority in Finding Jobs",
                      lambda s: s.can_move(-100000, -30, 5, 10, -15, -3000),
                      lambda s: s.move(-100000, -30, 5, 10, -15, -3000, uncertainty=1.15)),

             Operator("Health: Low Price Insurance",
                      lambda s: s.can_move(-2000000, 0, 10, 0, 5, 0),
                      lambda s: s.move(-2000000, 0, 10, 0, 5, 0, uncertainty=1.1)),

             Operator("Education: Free College Tuition",
                      lambda s: s.can_move(-3000000, 0, 3, 10, 10, -1000),
                      lambda s: s.move(-3000000, 0, 3, 10, 10, -1000, uncertainty=1.1)),

             Operator("Health: Provide Free Food for Homelessness",
                      lambda s: s.can_move(-80000, 0, 10, 0, 0, 0),
                      lambda s: s.move(-80000, 0, 10, 0, 0, 0)),
             Operator("Prepare For your Second Term Election",
                      lambda s: True,
                      lambda s: s.enable_second_term())]

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