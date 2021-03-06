"""

Java - Constraints
==================

Your code will be compiled using standard Java 7. It must implement the answer() method in the solution stub.

Execution time is limited. Some classes are restricted (e.g. java.lang.ClassLoader). You will see a notice if you use a restricted class when you verify your solution.

Third-party libraries, input/output operations, spawning threads or processes and changes to the execution environment are not allowed.

Python - Constraints
====================

Your code will run inside a Python 2.7.6 sandbox.

Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.


Solar Doomsday
==============

Who would've guessed? Doomsday devices take a LOT of power. Commander Lambda wants to supplement the LAMBCHOP's quantum antimatter reactor core with solar arrays, and she's tasked you with setting up the solar panels. 

Due to the nature of the space station's outer paneling, all of its solar panels must be squares. Fortunately, you have one very large and flat area of solar material, a pair of industrial-strength scissors, and enough MegaCorp Solar Tape(TM) to piece together any excess panel material into more squares. For example, if you had a total area of 12 square yards of solar material, you would be able to make one 3x3 square panel (with a total area of 9). That would leave 3 square yards, so you can turn those into three 1x1 square solar panels.

Write a function answer(area) that takes as its input a single unit of measure representing the total area of solar panels you have (between 1 and 1000000 inclusive) and returns a list of the areas of the largest squares you could make out of those panels, starting with the largest squares first. So, following the example above, answer(12) would return [9, 1, 1, 1].

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) area = 12
Output:
    (int list) [9, 1, 1, 1]

Inputs:
    (int) area = 15324
Output:
    (int list) [15129, 169, 25, 1]

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

"""


def sqrt(n, precision, debug=False):
    """
    This function returns the square root of a positive integer.
    
    :param n: an integer
    :param precision: precision of the result
    :return: the square root of the input integer
    """
    
    # Validate input type
    if not isinstance(n, int):
        raise TypeError("Input param `n` must be of type int. Got an {}".format(
            type(n)
    ))
    if not isinstance(precision, (int, float)):
        raise TypeError("Input param `precision` must be of type int or float. Got an {}".format(
            type(n)
    ))
    
    # Validate input value
    if n < 1:
        raise ValueError("Input param `n` must be a positive integer.")
    
    # Base case
    if n == 1:
        return 1
    
    # Initial setup for upper and lower bounds for Newton's method
    low, high = 1, n
    
    while abs(low-high) > precision:
    
        # Recalculate mid point
        mid = (high + low) / 2.0
        if debug: 
            print "mid: "+str(mid)
    
        # CASE 1: current result is too large
        if mid*mid > n:
            high = mid # update new upper bound to be mid point
    
        # CASE 2: current result is too low
        else:
            low = mid # update new lower bound to be mid point
    
    return mid


def answer(area):
    """
    This function takes as its input a single unit of measure
    representing the total area of solar panels you have (between 1 and 1000000 inclusive)
    and returns a list of the areas of the largest squares you could make out of those panels,
    starting with the largest squares first. So, following the example above, answer(12) would
    return [9, 1, 1, 1].
    
    :param area: single unit of measure representing the total area of solar panels you have (between 1 and 1000000 inclusive)
    :return: a list of the areas of the largest squares you could make out of those panels, starting with the largest squares first
    """
    
    # Initialize empty container for results
    response = []

    # Validate lower bound contraint
    if area < 1:
        return response

    # Iteratively find maximum size sub-squares
    while area > 0:
        # Get an estimate of the current area square root.
        # Note that precision DOES NOT need to be high since we are
        # only interested in integer values.
        current_max = int(round(sqrt(area, 0.1),0))

        # Sometime because of error/imprecision in sqrt() calculation
        # the rounded estimated square root squared might higher
        # than the initial area.
        if current_max**2 > area:
            # Update `current_max` if limit is violated
            current_max = current_max - 1
      
        # Append result to result container
        response.append(current_max**2)  
        
        # Update area to be the remaining area
        area = area - current_max**2
        
    return response
    



#error_cases = []
#for i in range(1,1000000):
#    print "PROCESSING : " + str(i)
#    ans = answer(i)
#    if sum(ans) != i:
#        error_cases.append(i)
