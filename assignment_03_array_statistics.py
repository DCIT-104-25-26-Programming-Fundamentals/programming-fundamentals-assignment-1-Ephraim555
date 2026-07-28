# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
 
n = int(input("How many numbers? "))

def stats(n):
    if n <= 0:
        return "Error: number must be greater than 0"
    array = []
    for i in range(n):
        value = int(input("Enter a number: "))
        array.append(value)
    summ = 0
    for x in range(len(array)):
        summ += array[x]

    avg = summ / n
 
    maxx = array[0]
    for a in range(len(array)):
        if array[a] > maxx:
            maxx = array[a]

    minn = array[0]
    for a in range(len(array)):
        if array[a] < minn:
            minn = array[a]

    return "Results: \n Sum: {} \n Average: {} \n Maximum: {} \n Minimum: {}".format(summ, avg, maxx, minn)

print(stats(n))