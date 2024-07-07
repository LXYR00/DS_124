"""A game picking and guessing a random number from 1 to 100."""

import numpy as np

number = np.random.randint(1, 101)
number = int(number)

bottom_line = 1
top_line = 100

"""The function made a search area less till number is guessed."""

def guessing_number(number, bottom_line, top_line, attempts=0):
    
    """It splits search area into 2 parts"""

    x = (bottom_line+top_line) // 2

    """It returns guessed number and number of attempts
    if it's already guessed. Or cuts the search area 
    untill tne number is guessed."""

    if x == number:
        attempts += 1
        return x, attempts
    
    elif x > number:
        attempts += 1
        top_line = x-1
        return guessing_number(number, bottom_line, top_line, attempts)
    
    elif x < number:
        attempts += 1
        bottom_line = x+1
        return guessing_number(number, bottom_line, top_line, attempts)
    
result = guessing_number(number, bottom_line, top_line)

print(f'It took {result[1]} attempts to guess number {result[0]}.')
