"""module to answer Fibonacci Series Exercise in Lesson 2"""


def fibonacci(n: int):
    """return nth value of fibonacci sequence starting with index 0
    args:
        n: positive integer for indicating sequence number to return


    returns:
        fib number at nth position
    """
    pass

    if n < 0:
        raise ValueError('input must be greater than or equal to 0')

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        counter = 2
        previous = 0
        current = 1

        while counter <= n:
            next = previous + current
            previous, current = current, next
            counter += 1
        return next


def lucas(n: int):
    """return nth value of lucas sequence starting with index 0
    args:
        n: positive integer for indicating sequence number to return


    returns:
        lucas number at nth position
    """
    pass

    if n < 0:
        raise ValueError('input must be greater than or equal to 0')

    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        counter = 2
        previous = 2
        current = 1

        while counter <= n:
            next = previous + current
            previous, current = current, next
            counter += 1
        return next


def sum_series(n:int, index0:int=0, index1:int=1):
    """return nth index (starting at 0) of summing series.
    starting values defined by index0 and index1
    args:
        n: non-negative integer for indicating sequence number to return
        index0: number in first index of sereies
        index1: number in second index of series 
    returns:
        value at nth position in summing series"""
    pass
