#!/usr/bin/env python
"""Extended arguments and keyword arguments."""


def hypervolume(length, *lengths):
    """Non keyword arg example.

    The inital postional argument is there to insure
    that the function fails with a TypeError and not
    a StopIteration error when not given any arguments
    which is more consistent with a function erroring
    out due to no args.
    This is a good standard practice for dealing with
    any required argument in a function.
    """
    v = length
    for item in lengths:
        v *= item
    return v


def tag(name, **attributes):
    """Keyword args can be handled by appending ** to the var.

    The kwargs can be accessed as a python dict.
    """
    result = '<' + name
    for key, value in attributes.items():
        result += ' {k}="{v}"'.format(k=key, v=str(value))
    result += '>'
    return result


def main():
    print('{}'.format(hypervolume(2)))
    print('{}'.format(hypervolume(2, 4)))
    print('{}'.format(hypervolume(2, 4, 6)))
    print('{}'.format(hypervolume(2, 4, 6, 8)))
    print('{}'.format(tag('img', src='kozik_labbit.jpg',
                          alt='Smorkin Labbit')))
    # *args call syntax
    thisthat = ['this', 'that']
    print('{}: {}'.format(*thisthat))
    # **kwargs call syntax
    backforth = {'b': 'back', 'f': 'forth'}
    print('{b}: {f}'.format(**backforth))


if __name__ == '__main__':
    main()
