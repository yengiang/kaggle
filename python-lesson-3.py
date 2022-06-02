""" 1. Many programming languages have sign available as a built-in function. Python doesn't, but we can define our own!

In the cell below, define a function called sign which takes a numerical argument and returns -1 if it's negative, 
1 if it's positive, and 0 if it's 0."""

def sign(x):
    if x > 0:
        return (1)
    elif x < 0:
        return (-1)
    else:
        return (0)


""" 2. We've decided to add "logging" to our to_smash function from the previous exercise.
def to_smash(total_candies):
    Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    
    print("Splitting", total_candies, "candies")
    return total_candies % 3

to_smash(91)

That isn't great grammar!

Modify the definition in the cell below to correct the grammar of our print statement. 
(If there's only one candy, we should use the singular "candy" instead of the plural "candies") """

def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    if total_candies > 1:
        print("Splitting", total_candies, "candies")
    else:
        print("Splitting", total_candies, "candy")
    return total_candies % 3

to_smash(91)
to_smash(1)


""" 3. In the tutorial, we talked about deciding whether we're prepared for the weather. I said that I'm safe from today's weather if...

I have an umbrella...
or if the rain isn't too heavy and I have a hood...
otherwise, I'm still fine unless it's raining and it's a workday
The function below uses our first attempt at turning this logic into a Python expression. I claimed that there was a bug in that code. Can you find it?

To prove that prepared_for_weather is buggy, come up with a set of inputs where either:

the function returns False (but should have returned True), or
the function returned True (but should have returned False).
To get credit for completing this question, your code should return a Correct result. """

def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    # Don't change this code. Our goal is just to find the bug, not fix it!
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

# Change the values of these inputs so they represent a case where prepared_for_weather
# returns the wrong answer.
have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = False

# Check what the function returns given the current values of the variables above
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)


""" 4. he function is_negative below is implemented correctly - it returns True if the given number is negative and False otherwise.

However, it's more verbose than it needs to be. We can actually reduce the number of lines of code in this function by 75% while keeping the same behaviour.

See if you can come up with an equivalent body that uses just one line of code, and put it in the function concise_is_negative. (HINT: you don't even need Python's ternary syntax) """

def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    pass # Your code goes here (try to keep it to one line!)
    return True if number < 0 else False


""" 5a. The boolean variables ketchup, mustard and onion represent whether a customer wants a particular topping on their hot dog. We want to implement a number of boolean functions that correspond to some yes-or-no questions about the customer's order. For example:
def onionless(ketchup, mustard, onion):
    Return whether the customer doesn't want onions.
    
    return not onion """

def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    pass
    return ketchup and mustard and onion


""" 5b. For the next function, fill in the body to match the English description in the docstring. """

def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    pass
    return not ketchup and not mustard and not onion

# Another way to solve
def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    pass
    return not (ketchup or mustard or onion)
    # Có thể để chữ not ra ngoài làm mẫu chung cho ketchup, mustard và onion.
    # Nhưng bên trong thì phải để chữ or ko phải and vì nếu để and thì chỉ có điều kiện cả 3 thứ là false, riêng lẻ hay 2 thứ đều true


""" 5c. You know what to do: for the next function, fill in the body to match the English description in the docstring. """

def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    pass 
    return onion and not (mustard and ketchup)
    # Another way to solve: return (ketchup and not mustard) or (mustard and not ketchup)


""" 6. We’ve seen that calling bool() on an integer returns False if it’s equal to 0 and True otherwise. What happens if we call int() on a bool? Try it out in the notebook cell below.

Can you take advantage of this to write a succinct function that corresponds to the English sentence "does the customer want exactly one topping?"? """

def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    pass
    return (ketchup + mustard + onion) == 1 
    # return (int(ketchup) + int(mustard) + int(onion)) == 1 cũng đúng nhưng ko cần thiết vì python đã mặc định convert nó qua int

    # Luôn nhớ là int(true) = 1 và int(false) = 0. Để giải quyết bài toán này thì cứ convert các bool qua int r cho nó cộng lại = 1
    # từ đó nó sẽ tự quyết định là 1 trong 3 cái arg phải = 1 và 2 cái còn lại = 0 thì mới thoả == 1