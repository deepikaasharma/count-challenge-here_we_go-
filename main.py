"""Complete the function called here_we_go(), which takes a list as a parameter and returns:

    The sorted version of the list.
    The reversed version of the list.
    The last element of the reversed list (without removing it from the list).
    The number of times that the number 22 occurs in the list.

All of these should be returned from one function (additional information below) and the original list should not be altered. When calling the function, unpack the returned values into the variables called:

    sorted_copy
    reversed_copy
    last_element
    count_22

The below is an example of a function that returns two objects. Use it to extrapolate how you write your function.

def function_with_multiple_outputs(parameter_1):
    '''
    A function that does things.

    Parameters:
    ----------
    parameter_1 : (list)
        A list.

    Returns:
    ----------
    x : (list)
        A copy of parameter_1
    y : (list)
        The last element of parameter_1
    '''
    x = paramater_1.copy()
    y = parameter_1[-1]

    return x, y

"""

def here_we_go(list_1):
  sorted_copy = sorted(list_1)
  reversed_copy = list(reversed(list_1))
  last_element = reversed_copy[-1]
  count_22 = list_1.count(22)
  return sorted_copy, reversed_copy, last_element, count_22

# use x as the input to your function
x = [22, 23, 4, 1, 22, 4, 6, 22, 2, 7, 88, 22]

# call (and unpack) your function here

sorted_copy, reversed_copy, last_element, count_22 = here_we_go(x)