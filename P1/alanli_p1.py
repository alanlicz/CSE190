"""
This file contains the starter code for Project 1 in
CSE 190, Early Fall Start, 2019.

Edit or complete all the assignment statements,
function definitions, etc., as indicated in the instructions.
"""

import random

UWNetID = "tianyl28"  # replace with your own UWNetID.
LAST_NAME = "Li"  # replace with your own last name.
FIRST_NAME = "Alan"  # replace with your own first name.


# EXERCISE 1:
#   Note that this one is done for you, so you can see how
#   functions must "return" values, and NOT print them.
def double(n):
    return 2 * n


# EXERCISE 2:
def three_x_squared_plus_2_x_plus_1(n):
    return 3 * (n ** 2) + 2 * n + 1


# EXERCISE 3:
def please_repeat_that(message):
    combined_message = message + " -- I said, " + message
    return combined_message


# EXERCISE 4:
def roll_die():
    return random.randint(1, 6)


def play_dice():
    print("Let's play dice. I'll go first.")
    input("Press Enter when you are ready for me to take my turn.")

    first_dice = roll_die()
    second_dice = roll_die()
    total_num = first_dice + second_dice
    first_dice = str(first_dice)
    second_dice = str(second_dice)

    print("I rolled a " + first_dice + " and a " + second_dice + ", for a total of " + str(total_num) + " . \
    Can you beat that?")
    input("Your turn. Press Enter to roll the dice.")

    third_dice = roll_die()
    fourth_dice = roll_die()
    total_num_player = third_dice + fourth_dice

    if total_num_player < total_num:
        print("You rolled a " + str(third_dice) + " and a " + str(fourth_dice) + ", for a total of " +
              str(total_num_player) + " . You lose!")
    elif total_num_player > total_num:
        print("You rolled a " + str(third_dice) + " and a " + str(fourth_dice) + ", for a total of " +
              str(total_num_player) + " . You win!")
    else:
        print("You rolled a " + str(third_dice) + " and a " + str(fourth_dice) + ", for a total of " +
              str(total_num_player) + " . It's a tie!")
    key = input("Do you want to play again?(Y/N)")
    if key == "Y" or key == "y":
        play_dice()
    else:
        return 0


# EXERCISE 5:
def cube_root(x):
    num = x ** (1 / 3)
    return num


# EXERCISE 6:
def makepal(word):
    original_list = list(word)
    original_list_copy = original_list[:]
    original_list.reverse()
    makepal_list = original_list_copy + original_list
    return makepal_list


# EXERCISE 7:
class Movie:
    def __init__(self, genre, title, director, release_date, language, leading_actors, plot_summary):
        self.genre = genre
        self.title = title
        self.director = director
        self.release_date = release_date
        self.language = language
        self.leading_actors = leading_actors
        self.plot_summary = plot_summary

    def __str__(self):
        actor_string = ""
        for actor in self.leading_actors:
            actor_string = actor_string.join(actor)
        return "Movie with genre " + self.genre + " , tile " + "'" + self.title + "'" + ", directed by " \
               + self.director + ", releasing during " + self.release_date + " in " + self.language + \
               ", with leading actors " + actor_string + "; plot summary: " + self.plot_summary


def by_genre(movie_list, genre):
    same_kind_movie_list = []
    for movie in movie_list:
        if movie.genre == genre:
            same_kind_movie_list.append(movie)
    return same_kind_movie_list


deepwater_horizon = Movie('disaster', 'Deepwater Horizon', 'Peter Berg', '2016', 'English',
                          ['Mark Wahlberg', 'Kurt Russell'], 'A dramatization of the disaster in April 2010, when ' +
                          'the offshore drilling rig called the Deepwater Horizon exploded, resulting in the worst ' +
                          'oil spill in American history.')

san_andreas = Movie('disaster', 'San Andreas', 'Brad Peyton', '2015', 'English',
                    ['Dwayne Johnson', 'Carla Gugino'], 'In the aftermath of a massive earthquake in California, ' +
                    'a rescue-chopper pilot makes a dangerous journey with his ex-wife across the state in order to' +
                    'rescue his daughter.')

the_day_after_tomorrow = Movie('disaster', 'The Day After Tomorrow', 'Roland Emmerich', '2004', 'English',
                               ' Dennis Quaid, Jake Gyllenhaal, Emmy Rossum', 'Jack Hall, paleoclimatologist, must ' +
                               'make a daring trek from Washington, D.C. to New York City to reach his son, trapped ' +
                               'in the cross-hairs of a sudden international storm which plunges the planet into a ' +
                               'new Ice Age.')

it = Movie('horror', 'It', 'Andy Muschietti', '2017', 'English', ['Bill Skarsgård, Jaeden Martell, Finn Wolfhard'],
           'In the summer of 1989, a group of bullied kids band together to destroy a shape-shifting monster, ' +
           'which disguises itself as a clown and preys on the children of Derry, their small Maine town.')

flight = Movie('thrill', 'Flight', 'Robert Zemeckis', '2012', 'English',
               ['Denzel Washington, Nadine Velazquez, Don Cheadle | See full cast & crew'], 'An airline pilot saves ' +
               'almost all his passengers on his malfunctioning airliner which eventually crashed, but an ' +
               'investigation into the accident reveals something troubling.')

# EXERCISE 8:
random_num = random.randint(0, 200)


def find_the_number():
    print('I can tell you if the number subtract m, is the result divisible by p.( (Here the rule ' +
          'is that p must be a prime number, and m must be less than p.)) ')
    while True:
        print("You can enter m and p.(Or you can type 'q' or 'I want to guess the number.')")
        num_1 = input("The first number(m)(m must be less than p) is: ")
        if num_1 == 'q' or num_1 == 'Q':
            return 0
        if num_1 == 'I want to guess the number.':
            guess_num = input("The number you guess is?")
            if guess_num == str(random_num):
                print("Congratulations!")
                return 0
            else:
                print("That is not correct!")
                return 0
        num_2 = input("The second number(p)(p must be a prime number) is ")
        if is_prime(num_2):
            if does_p_divide_n_minus_m(num_2, random_num, num_1):
                print("The answer is affirmative.")
            else:
                print("The answer is negative.")

        message = input("Now you can tell me if you want to ask the question again, you can just say 'Y(y)' or 'N(n)'.")
        if message == 'N' or message == 'n':
            break


def is_prime(p):
    for i in range(2, int(p)):
        if int(p) % int(i) == 0:
            return False
    return True


def does_p_divide_n_minus_m(p, n, m):
    if int(m) > int(p):
        print("M must be less than p!")
        return False
    if (int(n) - int(m)) % int(p) == 0:
        return True
    else:
        return False

