#!/usr/bin/env python
"""Comparison of plain, static and class methods.

some tests around staticmethod and classmethod decorators along with methods
for programmatically loading external data using a dict defined in a static
method as a map between the external and internal data.

Also shown is the property decorator, with a setter and deleter example.

more info about static and class methods at stackexchange:
    http://bit.ly/2sAjHEx
info about property decorators:
    http://bit.ly/2txQDL5
"""


class Test(object):
    def __init__(self, i=1, data=None, stuff=None):
        self.i = i
        print 'init var {}'.format(self.i)
        self.data = data
        self.stuff = stuff or {}
        self.l_stuff(self.stuff)

    def __repr__(self):
        return ('Test(i={}, data={}, stuff={})'.format(self.i,
                                                       self.data,
                                                       self.stuff))

    def m_basic(self):
        print 'basic method {}'.format(self.i)
        return self.i

    @classmethod
    def m_class(cls):
        # i1 = self.i
        i1 = cls().m_basic()
        print 'class method {}'.format(i1)
        return cls

    @staticmethod
    def m_static(i2=2):
        # i2 = Test.m_basic()
        print 'static method {}'.format(i2)
        return i2

    @property
    def i_method(self):
        return self.i

    @i_method.setter
    def i_method(self, new_i=None):
        if new_i is not None:
            self.i = new_i
        return self.i

    @i_method.deleter
    def i_method(self):
        print 'i_method deleter called.'
        del self.i

    @staticmethod
    def _attributes():
        """Map between external and internal data structures."""
        return {
            'external_1': 'internal1',
            'external_2': 'internal2',
            'external_3': 'internal3',
        }

    def l_stuff(self, stuff={}):
        """Load external dict to internal dict using map."""
        loaded = {}
        for key, value in self._attributes().iteritems():
            loaded[value] = stuff.get(key, None)
            self.loaded = loaded
        return loaded

    def d_stuff(self):
        for key, value in self._attributes().iteritems():
            print '{}: {}'.format(value, self.loaded.get(value, 'nothing'))


def main():
    """Main line of program, duh."""

    # call a classmethod and it initalizes, runs
    # the m_basic def and then itself.
    # can access internal calls.
    print '### classmethod ###'
    Test.m_class()
    # call a staticmethod and it runs w/o initialization
    # unless we specifically initialize the class
    print '### staticmethod ###'
    Test.m_static(i2=2)
    print '### normal class access ###'
    test_3 = Test(3)
    test_3.m_basic()
    print '### load data into data structure  ###'
    # test loading stuff
    stuff = {
            'external_1': 'a thing 1',
            'external_2': 'another thing 2'
            }
    test_4 = Test(4)
    test_4.l_stuff(stuff=stuff)
    test_4.d_stuff()
    # load stuff from __init__
    print '### Same but using __init__() ###'
    test_5 = Test(5, stuff=stuff)
    test_5.d_stuff()
    # test a property
    print '### property decorators ###'
    test_6 = Test(6)
    print 'the contents of i: {}'.format(test_6.i_method)
    test_6.i_method = 66
    print 'updated i: {}'.format(test_6.i_method)
    del test_6.i_method
    # Representation
    test_7 = Test(7)
    print 'the representation: {}'.format(repr(test_7))


if __name__ == '__main__':
    main()
