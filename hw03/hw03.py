from operator import add, sub

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    a, b, c = 1, 2, 3
    for i in range(n - 3):
        a, b, c = b, c, c + 2 * b + 3 * a
    return c



def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    "*** YOUR CODE HERE ***"
    if k < 10 and k != 7:
        return False
    elif k % 10 == 7:
        return True
    else:
        return has_seven(k // 10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    "*** YOUR CODE HERE ***"
    def op_change(i):
        if i < 7:
            return 1
        if i % 7 == 0 or has_seven(i):
            return op_change(i - 1) + 1
        return op_change(i - 1)



    if n <= 7:
        return n
    if op_change(n - 1) % 2 == 0:
        return pingpong(n - 1) + 1
    else:
        return pingpong(n - 1) - 1

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    def count_inner(amount, base):
        if amount <= 0:
            return 0
        if base > amount:
            return 0
        if base == amount:
            return 1
        base_side = count_inner(amount - base, base)
        other_side = count_inner(amount, 2 * base)
        return base_side + other_side
    return count_inner(amount, 1)

def towers_of_hanoi(n, start, end):
    """Print the moves required to solve the towers of hanoi game, starting
    with n disks on the start pole and finishing on the end pole.

    The game is to assumed to have 3 poles.

    >>> towers_of_hanoi(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> towers_of_hanoi(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> towers_of_hanoi(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 0 < start <= 3 and 0 < end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"


    """
    This is recurse problem can consider
    base case:
    Move start to end
    others:
    Move n - 1 to spare rod
    Move the last one the end
    Move the n - 1 from spare to end

    Can see from MIT's 6.001 ocw. https://courses.edx.org/courses/course-v1:MITx+6.00.1x_6+2T2015/courseware/sp13_Week_3/videosequence:Lecture_5/
    """
    def print_move(fr, to):
        print("Move the top disk from rod %s to rod %s" % (fr, to))
    def tower_inner(n, fr, to, spare):
        if n == 1:
            print_move(fr, to)
        else:
            tower_inner(n - 1, fr, spare, to)
            print_move(fr, to)
            tower_inner(n - 1, spare, to, fr)
    return tower_inner(n, start, end, start + 1)


from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    return 'YOUR_EXPRESSION_HERE'
