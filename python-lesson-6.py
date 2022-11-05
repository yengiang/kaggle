""" 1. Have you ever felt debugging involved a bit of luck? The following program has a bug. Try to identify the bug and fix it.
def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
        else:
            return False
Try to identify the bug and fix it in the cell below: """

#Version 1:
def has_lucky_number(nums):
    for num in nums:
        if num % 7 == 0:
            return True
    return False

#Version 2:
def has_lucky_number(nums):
    return any([num % 7 == 0 for num in nums])

""" 2. Look at the Python expression below. 
What do you think we'll get when we run it? When you've made your prediction, uncomment the code and run the cell to see if you were right.
#[1, 2, 3, 4] > 2 """

#Version 1:
def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    res = []
    for ele in L:
        res.append(ele > thresh)
    return res
    pass

#Version 2:
def elementwise_greater_than(L, thresh):
    return [ele > thresh for ele in L]

""" 3. Complete the body of the function below according to its docstring. """

def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False
    pass

""" 4. Next to the Blackjack table, the Python Challenge Casino has a slot machine. 
You can get a result from the slot machine by calling `play_slot_machine()`.
The number it returns is your winnings in dollars. Usually it returns 0.  
But sometimes you'll get lucky and get a big payday. Try running it below:
play_slot_machine()

By the way, did we mention that each play costs $1? Don't worry, we'll send you the bill later.
On average, how much money can you expect to gain (or lose) every time you play the machine?  
The casino keeps it a secret, but you can estimate the average value of each pull using a technique called the **Monte Carlo method**. 
To estimate the average outcome, we simulate the scenario many times, and return the average result.

Complete the following function to calculate the average value per play of the slot machine. """
def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    """
    payouts = [play_slot_machine()-1 for i in range(n_runs)]
    # Calculate the average value
    avg_payout = sum(payouts) / n_runs
    return avg_payout
    pass
