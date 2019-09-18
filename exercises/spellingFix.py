"""
This is my new file for SpellingFixes.py
"""


def SpellingFixes():
    flag = True
    print('Welcome to the spelling fix game!')
    correct_spelled_words = ['embarrassment', 'accommodate', 'occasionally']
    misspelled_words = ['embarrasment', 'acomodate', 'ocasionally']
    for word in misspelled_words:
        message = input('Fix the misspelled word = ' + word + '\nType here: ')
        if message in correct_spelled_words:
            print("That's right!")
        else:
            while flag:
                print("That's not the expected answer! Please try again. ")
                message = input('Fix the misspelled word = ' + word + '\nType here: ')
                if message in correct_spelled_words:
                    print("That's right!")
                    break


SpellingFixes()
