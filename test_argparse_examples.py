import pytest
import argparse_examples


class TestArgparseExamples(object):

    def test_argparse_xample(object):
        argv = ['-x']
        parser = argparse_examples.build_parser()
        args = parser.parse_args(argv)
        assert(args.xample)

    def test_argparse_csv(object):
        argv = ['-c', 'csv1,csv2']
        parser = argparse_examples.build_parser()
        args = parser.parse_args(argv)
        assert(args.csv_items == ['csv1', 'csv2'])

    @pytest.mark.parametrize("argv, output", [
                             (['-d', '-e'], ['d', 'e']),
                             (['-d', '-e', '-f'], ['d', 'e', 'f']),
                             (['-e'], ['e']),
                             (['-f'], ['f'])])
    def test_argparse_nonexclusive(object, argv, output):
        parser = argparse_examples.build_parser()
        args = parser.parse_args(argv)
        assert(args.sdef == output)

    @pytest.mark.parametrize("argv, output, exception", [
                             (['-a'], 'aaaaa', False),
                             (['-b'], 'bbbbb', False),
                             (['-a', '-b'], [], True)])
    def test_argparse_exclusive(object, argv, output, exception):
        parser = argparse_examples.build_parser()
        if exception:
            with pytest.raises(SystemExit):
                parser.parse_args(argv)
        else:
            args = parser.parse_args(argv)
            assert(args.xclusive == output)


# these are mostly for the coverage :-)
def test_demo_grouparg():
    demo = argparse_examples.demo_grouparg(['d', 'e', 'f'])
    assert(demo == 7)


@pytest.mark.parametrize("inn, out", [
                         ('aaaaa', 'a'),
                         ('bbbbb', 'b')])
def test_demo_xclusive(inn, out):
    demo = argparse_examples.demo_xclusive(inn)
    assert(demo == out)
