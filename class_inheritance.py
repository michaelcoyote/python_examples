#!/usr/bin/env python
"""This is an example."""


class Base(object):
    """Test Parent Class."""

    def __init__(self):
        print('This is the base-parent class')

    def class_method(self):
        print('This is a base class method')


class SubClassStub(Base):
    """Test Child Class w/o overrides."""
    pass


class SubClassOverride(Base):
    """Test override Base class from Child class."""

    def __init__(self):
        # If you want to use the __init__() from Base you need
        # to call it explicitly
        super(Base, self).__init__()
        print('This is extra code from the __init__ override')

    def class_method(self):
        print('Because this was overridden in the subclass it does something' +
              'different now')

    def new_subclass_method(self):
        print('Doing different stuff in the new subclass method')


def main():

    print('Base method')
    b1 = Base()
    b1.class_method()

    print('Subclass method w/o overrides')
    stub = SubClassStub()
    stub.class_method()

    print('Subclass method with overrides')
    override = SubClassOverride()
    override.class_method()
    override.new_subclass_method()


if __name__ == '__main__':
    main()
