import random
import math
UWNetID = "hxu6" # replace with your own UWNetID.
LAST_NAME = "XU"   # replace with your own last name.
FIRST_NAME = "MARCO" # replace with your own first name.

def double(n):
  return 2*n

def roll_die():
    return int(random.randint(1,6))
def roll_dice():
	return roll_die()
def three_x_squared_plus_2_x_plus_1(x):
	return 3*(x*x)+2*x+1
def please_repeat_that(somethings):
    return str(somethings)+" -- I said, "+str(somethings)
def play_dice():
    while True:
        input("Let's play dice. I'll go first.\nPress Enter when you are ready for me to take my turn.")
        computerdice1=roll_die()
        computerdice2=roll_die()
        computerdicesum=computerdice1+computerdice2
        input("I rolled a "+str(computerdice1)+" and a "+str(computerdice2)+", for a total of "+\
            str(computerdicesum)+". Can you beat that?\nYour turn. Press Enter to roll the dice.")
        
        playerdice1=roll_die()
        playerdice2=roll_die()
        playerdicesum=playerdice1+playerdice2

        result=""
        if(playerdicesum>computerdicesum):
            result="You lose"
        else:
            if(playerdicesum==computerdicesum):
                result="We draw"
            else:
                result="You win"
                
        choice=input("You rolled a "+str(playerdice1)+" and a "+str(playerdice2)+", for a total of "+\
            str(playerdicesum)+". "+result+". Do you want to play again (Y or N).")
        if choice == "Y" or choice== "y":
            pass
        else:
            break
def play_die():
	return play_dice()
def cube_root(number):
    return math.pow(number,1.0/3) if number>=0 else -math.pow(abs(number),1.0/3)

def makepal(string):
    list=[]
    for i in range(len(string)):
        list.append(string[i])
    for i in range(len(string)-1,-1,-1):
        list.append(string[i])
    return list


class Movie:
    def __init__(self,genre,title,director,releasedate,language,actors,summary):
        self.genre=genre
        self.title=title
        self.director=director
        self.releasedate=releasedate
        self.language=language
        self.actors=actors
        self.summary=summary
    def __str__(self):
        actors_string=""
        for actor in self.actors:
            actors_string=actors_string+actor+", "
        actors_string=actors_string[0:len(actors_string)-2]
        return "Movie with genre "+self.genre+", title '"+self.title+"', directed by "+\
            self.director+",released during "+str(self.releasedate)+" in "+self.language+\
                ", with leading actors "+actors_string+"; plot summary: "+self.summary


def by_genre(movie_list, genre):
    matched_movies=[]
    for movie in movie_list:
        if movie.genre==genre:
            matched_movies.append(movie)
    return matched_movies

def is_prime(p):
    if p<=1:
        return False
    if p<=3:
        return True
    if (p % 2 == 0 or p % 3 == 0) : 
        return False

    limit=int(math.sqrt(p))

    for n in range(5,limit+1,6):
        if p%n==0:
            return False
    return True
def does_p_divide_n_minus_m(p, n, m):
    return (n-m)%p==0

def find_the_number():
    number=random.randint(0,199)
    guessflag=False

    try:
        print("I just came up with a number, wanna guess it?")
        print("If you don't want to play with me, press Ctrl+C to exit")
        option1=input("Would you like to ask some questions about the number first[Y] \
or directly guess it?[N(Default)]\n")
        guessflag=not (option1=="Y" or option1=="y")
        while True:
            while not guessflag:
                option2=input("Let me give you some prompt:\n\
If you subtract m from my number, is the result divisible by p?\n\n\
The rule is that p must be a prime number, and m must be less than p.\n\
Press Enter to Continue\n")
                m=int(input("Please input m:"))
                p=int(input("Please input p:"))
                while not (is_prime(p) and m < p) :
                    print("You gave me wrong numbers.\n\
The rule is that p must be a prime number, and m must be less than p.\n")
                    m=int(input("Please input m:"))
                    p=int(input("Please input p, a prime number:"))
                if does_p_divide_n_minus_m(p,number,m):
                    print("You are lucky, you guessed right")
                else:
                    print("Oops, that's not true")
                option3=input("Would you like to have more prompt[Enter(Default)] or Directly Guess the Number[G]?\n")
                if(option3=="G" or option3=="g"):
                    guessflag=True
            while guessflag:
                user_number=int(input("Please input the Number you guess:"))
                if user_number==number:
                    print("You are a Lucky Star! You guessed right!")
                    guessflag=False
                else:
                    option4=input("Humm, not right. Try again[Default] or ask some questions?[A]\n")
                    if (option4=="A" or option4=="a"):
                        guessflag=False
                    
            
    except KeyboardInterrupt:
        print("Well, that's it. Goodbye.")
        return 0
    print("Goodbye")


star_wars_v=Movie("scifi","Star Wars: Episode V - The Empire Strikes Back", \
    "Irvin Kershner",1980,"English",["Mark Hamill","Harrison Ford","Carrie Fisher"],\

    "After the Rebels are brutally overpowered by the Empire on the ice planet Hoth,\
 Luke Skywalker begins Jedi training with Yoda, while his friends are pursued by Darth Vader.")

back_to_the_future_1=Movie("scifi","Back to the Future","Robert Zemeckis",1985,\
    "English",["Michael J. Fox","Christopher Lloyd","Lea Thompson"],\
    
    "Marty McFly, a 17-year-old high school student, is accidentally sent\
 thirty years into the past in a time-traveling DeLorean invented by his close friend,\
 the maverick scientist Doc Brown.")

blade_runner=Movie("scifi","Blade Runner","Ridley Scott",1982,"English",\
    ["Harrison Ford","Rutger Hauer","Sean Young"],\

        "A blade runner must pursue and terminate four replicants who stole a ship in space,\
 and have returned to Earth to find their creator.")

breakfast_club=Movie("comedy","The Breakfast Club","John Hughes",1985,\
    "English",["Emilio Estevez", "Judd Nelson","Molly Ringwald"],\
        "Five high school students meet in Saturday detention and discover how\
 they have a lot more in common than they thought.")

god_of_gamblers=Movie("drama","God of Gamblers","Jing Wong",1989,"Cantonese",\
    ["Yun-Fat Chow", "Andy Lau", "Joey Wang"],
    "A master gambler loses his memory, and is befriended by a street hustler\
 who discovers his supernatural gambling abilities.")

if __name__ == "__main__":
    # play_dice()
    # print(cube_root(float(input("Input Number to get its cube root:"))))
    # print(makepal(str(input("Input String to test makepal:"))))
    # print(blade_runner)
    # print(by_genre([star_wars_v],"scifi")[0])
    # print(is_prime(int(input("Input Number to Check its Primality:"))))
    #find_the_number()
    pass