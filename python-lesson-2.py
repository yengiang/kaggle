""" 1. Complete the body of the following function according to its docstring.

HINT: Python has a built-in function round. """
def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    # Replace this body with your own code.
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)
    pass
    return round(num, 2)


""" 2. The help for round says that ndigits (the second argument) may be negative. 
    
    What do you think will happen when it is? Try some examples in the following cell. """

# Put your test code here
round(338424, ndigits=-4)


""" 3. In the previous exercise, the candy-sharing friends Alice, Bob and Carol tried to split candies evenly. For the sake of their friendship, any candies left over would be smashed. For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.

Below is a simple function that will calculate the number of candies to smash for any number of total candies.

Modify it so that it optionally takes a second argument representing the number of friends the candies are being split between. If no second argument is provided, it should assume 3 friends, as before.

Update the docstring to reflect this new behaviour. """

def to_smash(total_candies, fn = 3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between fn friends.
    
    >>> to_smash(91, 3)
    1
    """
    return total_candies % fn
#meo meo