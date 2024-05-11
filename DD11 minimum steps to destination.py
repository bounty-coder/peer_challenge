'''Given an infinite number line. You start at 0 and can go either to the left or to the right.
    The condition is that in the ith move, you must take i steps. 
    Given a destination d, find the minimum number of steps required to reach that destination.'''

# Example 1:
# Input: d = 2
# Output: 3
# Explaination: The steps takn are +1, -2 and +3.

# Example 2:
# Input: d = 10
# Output: 4
# Explaination: The steps are +1, +2, +3 and +4.


def minSteps(dest):
    steps=0
    summ=0
    while summ<dest:
        steps+=1
        summ+=steps
    while summ-dest&1:
        steps+=1
        summ+=steps
    return steps


'''logic behind is, go uptill that number by sum
    if reached that exact number, return steps
    else, check until the difference is not odd"

    # why odd?
    # if difference is 10, it is even
    # then we just assume that instead of doing +5, we did -5
    #but for odd we cant do this, so increase number of steps
