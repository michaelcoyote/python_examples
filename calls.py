#!/usr/bin/env python
"""This is an example of __call__().

Here's a bunch of examples:
https://stackoverflow.com/questions/5824881/python-call-special-method-practical-example
"""


class CallableCache(object):
    """Cache or Memoization example.

    We store a varible in the class and use
    the __call__() function to update.
    This is against what I've been taught about
    keeping vars immutable, but can have utility
    in some cases.
    https://en.wikipedia.org/wiki/Memoization
    """
    def __init__(self):
        self.cache = 0

    def __call__(self, number):
        self.cache = self.cache + number
        return self.cache


class DecoratorCall(object):
    """Create a decorator class.

    __init__ takes in the varible for the decorator and stores
    __call__ takes in the function and wraps in a new function
    and returns that
    """
    def __init__(self, incoming):
        self.incoming = incoming

    def __call__(self, f):
        def new_f():
            print('function: {}'.format(f.__name__))
            f()
            print('{}'.format(self.incoming))
        return new_f


@DecoratorCall('world')
def hello():
    print('hello')


def main():
    cc = CallableCache()
    for i in range(0, 4):
        print('{}'.format(cc(2)))
    # decorated function
    hello()


if __name__ == '__main__':
    main()
