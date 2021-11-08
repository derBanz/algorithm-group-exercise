
def numberguessing(low, high):
    guess = int((high - low) / 2 + low)
    inp = input(f"We guess {guess}. Please enter 'higher/lower/hit': ")

    if inp == 'higher':
        numberguessing(guess, high)
    elif inp == 'lower':
        numberguessing(low, guess)
    return "We win!"
