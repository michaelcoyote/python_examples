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

    def test_ex_classmethod(object):
        assert(class_examples.Test.m_class() == 1)

    def test_internal_external_map(object):
        dict_in = {
                'external_1': 'thing 1',
                'external_2': 'thing 2'
                }
        ex1 = class_examples.Test()
        ex1.load_stuff(stuff=dict_in)
        assert(ex1.d_stuff() == {'internal1': 'thing 1',
                                 'internal2': 'thing 2',
                                 'internal3': None})
