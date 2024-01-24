#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list safely, handling potential errors."""

    count = 0  # Keep track of printed elements
    try:
        for i in range(x):
            print(my_list[i], end="")  # Print without newline
            count += 1
    except IndexError:
        pass  # Handle list index out of range gracefully

    print()  # Add a newline after printing elements
    return count  # Return the number of elements printed

