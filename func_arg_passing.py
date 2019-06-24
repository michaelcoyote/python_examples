#!/usr/bin/env python
"""Pass nonexclusive variables"""

import argparse


def test_passargument(share_def):
    """Choose to do a, b or both."""
    def a_thing():
        print("do a thing")
        return 1

    def b_thing():
        print("do b thing")
        return 2

    if 'a' and 'b' in share_def:
        r = a_thing()
        r += b_thing()
        return r
    if 'a' in share_def:
        r = a_thing()
        return r
    if 'b' in share_def:
        r = b_thing()
        return r


def build_parser():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    group = parser.add_argument_group('Three nonexclusive choices:',
                                      'Pick a, b, or a & b ')
    group.add_argument(
        '-a',
        help='opt a',
        const='a',
        action='append_const',
        dest='shared')
    group.add_argument(
        '-b',
        help='opt b',
        const='b',
        action='append_const',
        dest='shared')


if __name__ == '__main__':  # pragma: no cover
    parser = build_parser()
    args = parser.parse_args()
    if not args.shared:
        shared = ['a', 'b']
    else:
        shared = args.shared

    test_passargument(shared)
