# import pytest
import class_examples


class TestClassExample(object):
    def test_ex_import(self):
        ex1 = class_examples.Test()
        assert(ex1.m_basic() == 1)

    def test_ex_getter(object):
        ex1 = class_examples.Test()
        assert(ex1.i_method == 1)

    def test_ex_setter(object):
        ex1 = class_examples.Test()
        assert(ex1.i_method == 1)
        ex1.i_method = 66
        assert(ex1.i_method == 66)

    def test_ex_repr(object):
        ex1 = class_examples.Test(i=23, data='datum')
        print(repr(ex1))
        assert(repr(ex1) == 'Test(i=23, data=datum, stuff={})')
