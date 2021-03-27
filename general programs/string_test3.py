
# Python3 program for the above approach

# Function to check if the strings
# can be made equal or not by
# reversing a substring of X
def checkString(X, Y):

    # Store the first index from
    # the left which contains unequal
    # characters in both the strings
    L = -1

    # Store the first element from
    # the right which contains unequal
    # characters in both the strings
    R = -1

    # Checks for the first index from
    # left in which characters in both
    # the strings are unequal
    for i in range(len(X)):
        if (X[i] != Y[i]):

            # Store the current index
            L = i

            # Break out of the loop
            break

    # Checks for the first index from
    # right in which characters in both
    # the strings are unequal
    for i in range(len(X) - 1, 0, -1):
        if (X[i] != Y[i]):

            # Store the current index
            R = i

            # Break out of the loop
            break

    X = list(X)

    X = X[:L] + X[R  : L - 1 : -1 ] + X[R + 1:]

    # If X and Y are equal
    if (X == list(Y)):
        print("Yes")

    # Otherwise
    else:
        print("No")

# Driver Code
if __name__ == "__main__" :

    X = "adcbef"
    Y = "abvdef"

    # Function Call
    checkString(X, Y)