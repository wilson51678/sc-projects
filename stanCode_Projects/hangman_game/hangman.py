"""
File: hangman.py
name: Wilson
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    This program plays hangman game.
    Users sees a dashed word, trying to
    correctly figure the un-dashed word out
    by inputting one character each round.
    If the user input is correct, show the
    updated word on console. Players have N_TURNS
    to try in order to win this game.
    """
    # This is use for the return word of' random word'
    guess = random_word()
    print(guess)
    guess_dashed = dashed(guess)

    chance = N_TURNS
    # This loop insure the player to keep playing.
    while chance > 0 and guess_dashed != guess:
        print('The word looks like ' + str(guess_dashed))
        print('you have ' + str(chance) + ' guesses left')
        input_ch = input('Your guess: ')
        # This step would check whether 'input_ch' is the correct form
        while input_ch.isalpha() is False or len(input_ch) != 1:
            print('illegal format')
            input_ch = input('Your guess: ')
        # This step check whether player guess the right character in 'guess'
        if input_ch.upper() in guess:
            ans = ''
            # This for loop would make a new string when player enter the right character
            for i in range(len(guess)):
                if input_ch.upper() == guess[i]:
                    ans += guess[i]
                # This step would start when player enter the right character in second time.
                elif guess_dashed[i].isalpha():
                    ans += guess_dashed[i]
                # The rest of new string would fill with'-'
                else:
                    ans +='-'
            guess_dashed = ans
            print('you are correct!')
        # When player guess the wrong character, chance will minus one
        else:
            chance-=1
            print('There is no '+str(input_ch)+"'s in the word")

    # This step show up when player fail 7 times guesses
    if chance == 0:
        print('You are completely hung :( ')
    # This step show 'guess' when player guess all the character right
    else:
        print('You win')
    print('The word was:'+str(guess))


def dashed(guess):
    """
    This function should block every word of 'guess'.
    :param guess: str
    :return: str, replace every words of 'guess' to '-'.
    """
    new = ''
    for i in range(len(guess)):
        ch = guess[i]
        new +='-'
    return new


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
