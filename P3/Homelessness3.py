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
low_popularity_count_threshold = 3
homeless_people_threshold = 2500

homeless_uncertainty = 0.01
money_uncertainty = 0.007
housing_price_uncertainty = 0.05
health_points_uncertainty = 0.2
popularity_uncertainty = 0.05
employment_rate_uncertainty = 0.05

homeless_money_externality_factor = 6000  # $8125 Each Homeless Per Quarter on Public Fund and Tax Revenue
homeless_popularity_externality_factor = 0.0001
housing_price_homeless_externality_factor = 1
housing_price_popularity_externality_factor = 0.1
health_points_popularity_externality_factor = 0.4

homeless_money_externality_baseline = 5000
homeless_popularity_externality_baseline = 6000
housing_price_homeless_externality_baseline = 750
health_points_popularity_externality_baseline = 70

# </COMMON_DATA>

# <COMMON_CODE>
import random


class State:
    def __init__(self, old=None):
        # Default new state is a state objects initialized as the
        # initial state.
        # If called with old equal to a non-empty state, then
        # the new instance is made to be a copy of that state.
        self.money = 3400000000  # $3.4 Billion At Beginning
        self.housing_price = 1100
        self.health_points = 40
        self.employment_rate = 5
        self.popularity = 60
        self.homeless_people = 14449
        self.quarter_num = 1
        self.second_term_flag = False
        self.revenue_factor = 1.0
        self.low_popularity_count = 0
        self.homeless_change_rate = 100
        self.effectiveness_factor = 1.0
        if old is not None:
            self.money = old.money
            self.housing_price = old.housing_price
            self.health_points = old.health_points
            self.employment_rate = old.employment_rate
            self.popularity = old.popularity
            self.homeless_people = old.homeless_people
            self.quarter_num = old.quarter_num + 1
            self.second_term_flag = old.second_term_flag
            self.revenue_factor = old.revenue_factor
            self.low_popularity_count = old.low_popularity_count
            self.homeless_change_rate = old.homeless_change_rate
            self.effectiveness_factor = old.effectiveness_factor

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
             employment_rate_adjustment, popularity_adjustment, homeless_people_adjustment, uncertainty=1.0,
             revenue_factor_adjustment=0.0, homeless_change_rate_adjustment=0):
        news = State(old=self)
        # Make a copy of the current state.
        news.money += money_adjustment * self.effectiveness_factor
        news.money += 280000000 * self.revenue_factor  # $ 280 Million Per Quarter
        news.money += news.money * random.uniform(-money_uncertainty, money_uncertainty) * uncertainty
        news.housing_price += 40
        news.housing_price += housing_price_adjustment * self.effectiveness_factor
        news.housing_price += news.housing_price * random.uniform(-housing_price_uncertainty,
                                                                  housing_price_uncertainty) * uncertainty
        news.health_points += health_points_adjustment * self.effectiveness_factor
        news.health_points += news.health_points * random.uniform(-health_points_uncertainty,
                                                                  health_points_uncertainty) * uncertainty
        news.employment_rate += employment_rate_adjustment * self.effectiveness_factor
        news.employment_rate += news.employment_rate * random.uniform(-employment_rate_uncertainty,
                                                                      employment_rate_uncertainty) * uncertainty
        news.popularity += popularity_adjustment * self.effectiveness_factor
        news.popularity += news.popularity * random.uniform(-popularity_uncertainty,
                                                            popularity_uncertainty) * uncertainty
        news.homeless_people += homeless_people_adjustment * self.effectiveness_factor
        news.homeless_people += news.homeless_change_rate * self.effectiveness_factor
        news.homeless_people += news.homeless_people * random.uniform(-homeless_uncertainty,
                                                                      homeless_uncertainty) * uncertainty
        news.revenue_factor *= revenue_factor_adjustment * self.effectiveness_factor
        news.homeless_change_rate += homeless_change_rate_adjustment * self.effectiveness_factor

        news.homeless_people += (
                                            news.housing_price - housing_price_homeless_externality_baseline) * housing_price_homeless_externality_factor
        news.money -= (news.homeless_people - homeless_money_externality_baseline) * homeless_money_externality_factor
        news.popularity -= (
                                       news.homeless_people - homeless_popularity_externality_baseline) * homeless_popularity_externality_factor

        news.money = 0 if news.money < 0 else news.money
        news.housing_price = 0 if news.housing_price < 0 else news.housing_price
        news.health_points = 0.0 if news.health_points < 0 else news.health_points
        news.health_points = 100.0 if news.health_points > 100 else news.health_points
        news.employment_rate = 0.0 if news.employment_rate < 0 else news.employment_rate
        news.popularity = 0.0 if news.popularity < 0 else news.popularity
        news.popularity = 100.0 if news.popularity > 100.0 else news.popularity
        news.homeless_people = 0.0 if news.homeless_people < 0.0 else news.homeless_people

        news.low_popularity_count += (1 if news.popularity < popularity_threshold else -news.low_popularity_count)

        return news

    def enable_second_term(self):
        self.second_term_flag = True
        return self

    def isGoal(self):
        # Check if you have reached a goal state
        if self.quarter_num == 17 and (self.popularity <= 60 or (not self.second_term_flag)):
            return True
        if self.quarter_num > 32:
            return True
        if self.money < money_threshold:
            return True
        if self.low_popularity_count > low_popularity_count_threshold:
            return True
        return False

    def is_goal(self):
        return self.isGoal()

    def goal_message(self):
        if self.money < money_threshold:
            return "Your government is Bankrupted!"
        if self.low_popularity_count > low_popularity_count_threshold:
            return "Your people are disappointed in you and legislators has passed the Impeachment Bill!\nYou are Thrown Out of Office!"

        if self.quarter_num == 17 and (self.popularity <= 60 or (not self.second_term_flag)):
            return "You Stepped Down after your First term\n" + (
                "You Successfully solved homeless problem!" if self.homeless_people <= homeless_people_threshold else "You Failed to solve homeless problem")
        if self.quarter_num > 32:
            return "You Stepped Down after your Second term\n" + (
                "You Successfully solved homeless problem!" if self.homeless_people <= homeless_people_threshold else "You Failed to solve homeless problem")

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
        txt = "This is your " + str(self.quarter_num) + " quarters in office.\n"
        txt += "\nThe fund is now " + "{:.3f}".format(self.money / 1000000.0) + " Million dollars.\n"
        txt += "Your popularity is now " + "{:.1f}".format(self.popularity) + " percent.\n"
        txt += "The housing price is now " + "{:.1f}".format(self.housing_price) + " dollars per month\n"
        txt += "The health points is now " + "{:.1f}".format(self.health_points) + ".\n"
        txt += "The employment rate is now " + "{:.1f}".format(self.employment_rate) + " percent.\n"
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
    apply_count_table = {}

    def __init__(self, name, precond, state_transf, diminishing_utility_factor=1.0):
        self.name = name
        self.precond = precond
        self.state_transf = state_transf
        self.diminishing_utility_factor = (1.0 if diminishing_utility_factor < 1.0 else diminishing_utility_factor)
        Operator.apply_count_table[self.name] = 0

    def is_applicable(self, s):
        return self.precond(s)

    def apply(self, s):
        s.effectiveness_factor = self.diminishing_utility_factor ** -Operator.apply_count_table[
            self.name]  # reversed exponential fuction
        Operator.apply_count_table[self.name] += 1
        return self.state_transf(s)


# </COMMON_CODE>

# <INITIAL_STATE>
INITIAL_STATE = State()
# </INITIAL_STATE>


OPERATORS = [
    Operator("Doing Nothing",
             lambda s: True,
             lambda s: s.move(0, 0, 0, 0, 0, 0)),

    Operator("Housing: Rental Price Ceiling",
             lambda s: True,
             lambda s: s.move(-80000000, -50, 5, 0, -5, 0, uncertainty=0.9, homeless_change_rate_adjustment=-50),
             diminishing_utility_factor=2.0),
    # Test can_move function. Note that money variable has changed.

    Operator("Housing: Build Affordable Houses",
             lambda s: True,
             lambda s: s.move(-800000000, -200, 5, 0, 15, 0),
             diminishing_utility_factor=1.0),
    # Test isGoal function

    Operator("Health: Street Health Care Team",
             lambda s: True,
             lambda s: s.move(-10000000, 0, 15, 0, 5, -400)),

    Operator("Health: Drugs Users Treatment",
             lambda s: True,
             lambda s: s.move(-2000000, 0, 10, 0, 10, -500)),

    Operator("Eduction: Free Education and Shelters for Homeless Children",
             lambda s: True,
             lambda s: s.move(-100000000, 0, 0, 5, 20, -1000)),

    Operator("Job: Free Job Training",
             lambda s: True,
             lambda s: s.move(-40000000, 0, 5, 10, 5, -500)),

    Operator("Job: Provide Job Opportunities for Homelessness People",
             lambda s: True,
             lambda s: s.move(-8000000, 0, 5, 10, -15, -500)),

    Operator("Housing: Provide Portable Shelter",
             lambda s: True,
             lambda s: s.move(-50000000, 0, 5, 0, -5, 0)),

    Operator("Housing: Building Shelter for Homeless",
             lambda s: True,
             lambda s: s.move(-500000000, 0, 5, 0, 5, -2000),
             diminishing_utility_factor=1.2),

    Operator("Housing: Restricting Unfair Eviction of Renter",
             lambda s: True,
             lambda s: s.move(0, 0, 0, 0, 8, 0, homeless_change_rate_adjustment=-200),
             diminishing_utility_factor=2.5),

    Operator("Financial: Increase Minimum Wage",
             lambda s: True,
             lambda s: s.move(10000000, 30, 0, -5, 5, 0)),

    Operator("Financial: Raise Tax",
             lambda s: True,
             lambda s: s.move(0, 0, 0, 0, -20, 0, revenue_factor_adjustment=0.2)),

    Operator("Financial: Cut Tax",
             lambda s: True,
             lambda s: s.move(0, 0, 0, 0, 8, 0, revenue_factor_adjustment=-0.3)),

    Operator("Financial: Big Tech Tax",
             lambda s: True,
             lambda s: s.move(0, -150, 0, -5, 5, 0, revenue_factor_adjustment=0.1),
             diminishing_utility_factor=2.0),

    Operator("Job: Make Homelessness Has Priority in Finding Jobs",
             lambda s: True,
             lambda s: s.move(-500000, 0, 5, 10, -15, -300, uncertainty=1.15)),

    Operator("Health: Provide Free Food for Homelessness",
             lambda s: True,
             lambda s: s.move(-10000000, 0, 10, 0, 0, 0)),
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