#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """print x elements of a list.

    Args:
    my_list (list): The list of all elements.
    x (int): the number of elements of list to print.

    Return:
    The number of elements printed.
    """
    rter = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            rter += 1
        except IndexError:
            break
    print()
    return (rter)
