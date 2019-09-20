#!/usr/bin/env python
"""Example Algorithms."""


class Node(object):
    def __init__(self, value, link):
        self.value = value
        self.link = link

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


def binary_search(narray, nleft, nright, ntarget):
    """Binary Search.

    https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/implementing-binary-search-of-an-array
    https://www.geeksforgeeks.org/binary-search/

    Basically we split a numerically sorted array of numbers in half and check
    the value every iteration.  If the value is the same we return the array
    index number.

    If the number is low we set the new left side index to the guess + 1
    If the number is too high we set the new right side index to the guess - 1

    If we run out of guesses we will see the right index become lower or equal
    to the right index.
    """
    while nleft <= nright:
        # center the guess index
        guess = int(nleft + (nright - nleft)/2)
        print('index no: {} value: {}'.format(guess, narray[guess]))
        # If the guess index is correct, return the index
        if narray[guess] == ntarget:
            print('target: {} = {}'.format(ntarget, narray[guess]))
            return guess
        # If the target is greater remove indexes left of guess
        elif narray[guess] < ntarget:
            nleft = guess + 1
        # If the target is less (only other option) remove indexes right of
        # guess
        else:
            nright = guess - 1
    # if the left sides and right sides meet or overlap the array doesn't
    # contain the target number
    return (-1)


def main():
    narray = ([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
               59, 61, 67, 71, 73, 79, 83, 89, 97])
    ntarget = 67
    binsrc_r = binary_search(narray=narray,
                             nleft=0,
                             nright=(len(narray)-1),
                             ntarget=ntarget)
    print('Binary Search - Result: {}'.format(binsrc_r))


if __name__ == '__main__':
    main()
