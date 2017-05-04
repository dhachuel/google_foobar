"""
Don't Get Volunteered!
======================

As a henchman on Commander Lambda's space station, you're expected to be resourceful, smart, and a quick thinker. It's not easy building a doomsday device and capturing bunnies at the same time, after all! In order to make sure that everyone working for her is sufficiently quick-witted, Commander Lambda has installed new flooring outside the henchman dormitories. It looks like a chessboard, and every morning and evening you have to solve a new movement puzzle in order to cross the floor. That would be fine if you got to be the rook or the queen, but instead, you have to be the knight. Worse, if you take too much time solving the puzzle, you get "volunteered" as a test subject for the LAMBCHOP doomsday device!

To help yourself get to and from your bunk every day, write a function called answer(src, dest) which takes in two parameters: the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle.  The function should return an integer representing the smallest number of moves it will take for you to travel from the source square to the destination square using a chess knight's moves (that is, two squares in any direction immediately followed by one square perpendicular to that direction, or vice versa, in an "L" shape).  Both the source and destination squares will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below:

-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) src = 19
    (int) dest = 36
Output:
    (int) 1

Inputs:
    (int) src = 0
    (int) dest = 1
Output:
    (int) 3
"""

def floor(x):
    """
    This function returns the mathematical floor of an input number.
    
    Args:
        x (int, float) : an input number

    Return:
        (int, float) the floor of the input number
    """
    # Validate input data type
    if not isinstance(x, (float, int)):
        raise TypeError("Input `n` is not numeric.")
        
    return x - (x % 1)

def minKnigthMoves(x, y):
    """
    For a sample 8 by 8 grid, the minimum standard chess 
    knight moves to reach any location from the origin (0, 0)
    are as follows:
        
    7								6
    6							4	5
    5						4	5	4
    4					4	3	4	5
    3				2	3	4	3	4
    2			4	3	2	3	4	5
    1		2	1	2	3	4	3	4
    0	0	3	2	3	2	3	4	5
    	0	1	2	3	4	5	6	7

    We can notice some patterns like symmetry along the x, y and y = +-y
    axis. By focusing only on the lower triangle we can generalize some
    rules to compute the minimum number of moves.
    
    The below method/function returns the minimum number of moves that
    a standard chess knight needs to reach any location in the lower triangle
    part of an 8 by 8 board if the starting point is the origin (0, 0).
    
    Args:
        x (int) : the x coordinate of the destination
        y (int) : the y coordinate of the destination

    Return:
        (int) the minimum number of moves for the knight's tour
    """
    # Get diagonal symmetric equivalent (lower triangle constraint)
    if x < y:
        x, y = y, x
    
    # Managed 2 exceptions
    if (x, y) == (1, 0):
        return 3
    if (x, y) == (2, 2):
        return 4
    
    # Main algebraic formula
    delta = x - y
    if y > delta:
        return int(delta - 2*floor((delta-y)/3.0))
    else:
        return int(delta - 2*floor((delta-y)/4.0))

def answer(src, dest):
    """
    Main function wrapper for the minimum number of knight moves in 
    a standard chess board.
    
    Args:
        src (int) : the origin/start of the knight in the board
        dest (int) : the destination of the knight
    """
    # Remap to indeces (only valid in 8 by 8 boards)
    y_src = src//8
    x_src = src%8
    y_dest = dest//8
    x_dest = dest%8
    
    # Translate src and dest to (0,0) origin (normalization)
    x_dest_norm = x_dest - x_src
    y_dest_norm = y_dest - y_src
    
    # Calculate min number of moves
    print "x : " + str(abs(x_dest_norm)) + ", y : " + str(abs(y_dest_norm))
    return minKnigthMoves(x=abs(x_dest_norm), y=abs(y_dest_norm))
