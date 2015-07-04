# Q4
def get_seven_a(x):
    """
    >>> x = [1, 3, [5, 7], 9]
    >>> get_seven_a(x)
    7
    """
    "*** YOUR CODE HERE ***"
    return x[2][1] 

def get_seven_b(x):
    """
    >>> x = [[7]]
    >>> get_seven_b(x)
    7
    """
    "*** YOUR CODE HERE ***"
    return x[0][0]

def get_seven_c(x):
    """
    >>> x = [1, [2, [3, [4, [5, [6, [7]]]]]]]
    >>> get_seven_c(x)
    7
    """
    "*** YOUR CODE HERE ***"
    return x[1][1][1][1][1][1][0] 

# Q5
def reverse_recursive(lst):
    """Returns the reverse of the given list.

    >>> reverse_recursive([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    "*** YOUR CODE HERE ***"
    length = len(lst)
    if length <= 1:
        return lst
    else:
        return [lst[-1]] + reverse_recursive(lst[1:length-1]) + [lst[0]]

def merge(lst1, lst2):
    """Merges two sorted lists recursively.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"
    result = []
    while not (len(lst1) == 0 and len(lst2) == 0):
        if len(lst1) == 0:
            result += lst2
            lst2 = []
        elif len(lst2) == 0:
            result += lst1
            lst1 = []
        else:
            if (lst1[0] < lst2[0]):
                result.append(lst1[0])
                lst1.remove(lst1[0])
            else:
                result.append(lst2[0])
                lst2.remove(lst2[0])
    return result

# Q8
from math import sqrt

def is_square(n):
    return float(sqrt(n)) == int(sqrt(n))

def squares(seq):
    """Returns a new list containing elements of the original list that are
    perfect squares.

    >>> seq = [49, 8, 2, 1, 102]
    >>> squares(seq)
    [49, 1]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    "*** YOUR CODE HERE ***"
    return [num for num in seq if is_square(num)]

