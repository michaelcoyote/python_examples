#!/usr/bin/env python3
"""Examples of iterators."""

import datetime
import time


class IterExample():
    def __init__(self, data):
        self.index = 0
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        """Next format for py 3."""
        if self.index >= len(self.data):
            raise StopIteration()

        result = self.data[self.index]
        self.index += 1
        return result


class IterableExample:
    def __init__(self):
        self.data = [1, 2, 3, 4]

    def __iter__(self):
        return IterExample(self.data)


class AltIter:
    def __init__(self):
        self.data = [2, 4, 6, 8]

    def __getitem__(self, index):
        return self.data[index]


def main():
    print('A standard iterator example')
    for i in IterableExample():
        print('Std: {}'.format(i))

    print('An alternate iterator example')
    [print('Alt: {}'.format(i * 3)) for i in AltIter()]

    # iter() examples
    # Make an iterator out of an array
    print('Iterate through some letters')
    letters = ['l', 'e', 't', 't', 'e', 'r', 's']
    iterletters = iter(letters)
    for l in iterletters:
        print('Iter: {}'.format(l))
    # time based iter example
    print("Iterate over a time example using iter()")
    ie = iter(datetime.datetime.now, None)
    print('Initial iteration after initalization: {}'.format(next(ie)))
    time.sleep(2)
    print('Iteration after 2 second sleep: {}'.format(next(ie)))
    # unused example using a file
    # with open('ending_file.txt', 'rt') as f:
    #     for line in iter(lambda: f.readline().strip(), 'END'):
    #         print line


if __name__ == '__main__':
    main()
