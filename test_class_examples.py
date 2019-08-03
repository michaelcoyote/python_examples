import pytest
import class_examples


class TestClassExample(object):
    def test_ex_import(self):
        ex1 = class_examples.ClassExample()
        assert(ex1.m_basic() == 1)
        ex1.m_basic(i=2)
        assert(ex1.m_basic() == 2)

    def test_ex_getter(object):
        ex1 = class_examples.ClassExample()
        assert(ex1.int_value == 1)

    def test_ex_setter(object):
        ex1 = class_examples.ClassExample()
        assert(ex1.int_value == 1)
        ex1.int_value = 66
        assert(ex1.int_value == 66)

    def test_ex_setter_nonint_type_error(self):
        with pytest.raises(TypeError):
            class_examples.ClassExample(i="notanint")

    def test_ex_multiplier_function(self):
        ex1 = class_examples.ClassExample(2)
        assert(ex1.int_multiplier() == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    def test_ex_repr(object):
        ex1 = class_examples.ClassExample(i=23, data='datum')
        print(repr(ex1))
        assert(repr(ex1) == 'ClassExample(i=23, data=datum, stuff={})')

    def test_ex_staticmethod(object):
        assert(class_examples.ClassExample.m_static(3) == 3)

    def test_ex_classmethod(object):
        assert(class_examples.ClassExample.m_class() == 1)

    def test_internal_external_map(object):
        dict_in = {
                'external_1': 'thing 1',
                'external_2': 'thing 2'
                }
        ex1 = class_examples.ClassExample()
        ex1.load_stuff(stuff=dict_in)
        assert(ex1.d_stuff() == {'internal_1': 'thing 1',
                                 'internal_2': 'thing 2'})
