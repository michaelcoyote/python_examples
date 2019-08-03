#!/usr/bin/env python3


class ClassExample(object):
    """Comparison of plain, static and class methods.

    Some tests around staticmethod and classmethod decorators along
    with methods for programmatically loading external data using a
    dict defined in a static method as a map between the external
    and internal data.

    Also shown is the property decorator, with a setter and deleter
    examples with some discussion of how these can be used to create a
    complete interface for accessing variable values within the object
    without directly accessing the object itself.

    more info about static and class methods at stackexchange:
        http://bit.ly/2sAjHEx
    info about property decorators:
        http://bit.ly/2txQDL5
        PEP-318: https://www.python.org/dev/peps/pep-0318/
    """

    def __init__(self, i=1, data=None, stuff=None):
        """Initializer methods configure the class copy.

        Assignment of variables and data validation can
        happen here.

        Note that the validation of data can happen within
        other class modules.  This allows the logic to be
        reused (e.g. you can use setters not only to access
        internal vars but do bounds checking and other things
        and this logic can be reused when an internal variable
        needs to be updated.
        """
        self.int_value = i
        print('init int variable: {}'.format(self.int_value))
        # Set a default value for self.data if none set at init time
        if data:
            self.data = data
        else:
            self.data = f"The int value is {self.int_value}"
        self.stuff = stuff or {}
        self.load_stuff(self.stuff)

    def __repr__(self):
        """Return a printable representation of an object."""
        return (f"ClassExample(i={self._integer_value}, "
                f"data={self.data}, stuff={self.stuff})")

    @property
    def int_value(self):
        """Getter for self._integer_value."""
        return self._integer_value

    @int_value.setter
    def int_value(self, i):
        """Setter for self._integer_value w/ type check.

        We use raise to throw a TypeError, but other things
        can be done here like checking bounds, etc."""
        if isinstance(i, int):
            self._integer_value = i
        else:
            raise TypeError("int_value must be integer")

    def int_multiplier(self):
        """Return a list of products for the int_value up to 10."""
        return [i * self.int_value for i in range(1, 11)]

    def m_basic(self, i=None):
        """Basic method implementation.

        We can set and get with this method but must use the
        standard interface to do so and the class must be
        instansiated before use.
        e.g. no calling with ClassExample.m_basic()
        """
        if i is not None:
            self.int_value = i
        print('basic method {}'.format(self._integer_value))
        return self.int_value

    @classmethod
    def m_class(cls):
        """The classmethod accesses the class object directly.

        Note that the cls keyword is a shortcut for the
        actual class name (in this case ClassExample).

        Use classmethod if you need to access the class methods
        or instances.
        """
        i1 = cls().int_value
        print('class method {}'.format(i1))
        return i1

    @staticmethod
    def m_static(nonclassvar=2):
        """The staticmethod has no access to the class.

        Generally this is used for implementation details since it
        has no access to the class or instance objects.

        Think carefully about your Class organization when using
        this as it may make sense to split out a staticmethod into
        it's own module instead of having it in the class.
        """
        # nonclassvar = ClassExample.m_basic()
        print('static method {}'.format(nonclassvar))
        return nonclassvar

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data=None):
        if new_data is not None:
            self._data = new_data
        return self._data

    @data.deleter
    def data(self):
        print('data deleter called.')
        del self._data

    @staticmethod
    def _attributes(ln=3):
        """Create map for external and internal data structures.

        Again this is a static method with no access to class.
        This method only creates a map for external to internal
        data structures so it doesn't need access, and it's specific
        to creating a map for this class so it's probably fine
        being in the class as a static method.

        Given a lenght of 3, this method will return a map
        dictionary something like this:

        map = {
            'external_1': 'internal_1',
            'external_2': 'internal_2',
            'external_3': 'internal_3',
        }
        """
        map = {}
        for i in range(1, (ln + 1)):
            map[f"external_{i}"] = f"internal_{i}"
        return map

    def load_stuff(self, stuff={}):
        """Load external dict to internal dict using map."""
        loaded = {}
        for key, value in self._attributes(len(stuff)).items():
            loaded[value] = stuff.get(key, None)
            self._int_stuff = loaded
        return loaded

    def d_stuff(self):
        """Display the internally mapped stuff."""
        for key, value in self._attributes().items():
            print('{}: {}'.format(value,
                                  self._int_stuff.get(value, 'nothing')))
        return self._int_stuff


def main():
    """Main line of program, eh!

    This is mostly just a quick way to illustrate
    the class examples. Everything has print statements and
    is noisy as heck.  Note that there is a Test suite
    where there's a lot of example code calling the class
    and showing how the examples work."""

    # call a classmethod and it initalizes, runs
    # the m_basic def and then itself.
    # can access internal calls.
    print('### classmethod ###')
    ClassExample.m_class()
    # call a staticmethod and it runs w/o initialization
    # unless we specifically initialize the class
    print('### staticmethod ###')
    ClassExample.m_static(nonclassvar=2)
    print('### normal class access ###')
    test_3 = ClassExample(3)
    test_3.m_basic()
    print('### load data into data structure  ###')
    # test loading stuff
    stuff = {
            'external_1': 'a thing 1',
            'external_2': 'another thing 2'
            }
    test_4 = ClassExample(4)
    test_4.load_stuff(stuff=stuff)
    test_4.d_stuff()
    # load stuff from __init__
    print('### Same but using __init__() ###')
    test_5 = ClassExample(5, stuff=stuff)
    test_5.d_stuff()
    # test a property
    print('### property decorators ###')
    test_6 = ClassExample(i=6, data='datum')
    print('the contents of data: {}'.format(test_6.data))
    test_6.data = 'datas'
    print('updated data: {}'.format(test_6.data))
    del test_6.data
    # Representation
    test_7 = ClassExample(7)
    print('the representation: {}'.format(repr(test_7)))


if __name__ == '__main__':
    main()
