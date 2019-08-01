#!/usr/bin/env python
"""Test shared argparse vars.

The question came up if there was way to share a var within an exclusive
argeparse group to make for a slightly cleaner test of variables.
This example has expanded to include some non-exclusive shared vars."""

import argparse
import pprint


def demo_xclusive(xclusive):
    if xclusive == 'aaaaa':
        print("the a's have it")
        return 'a'
    elif xclusive == 'bbbbb':
        print("it be")
        return 'b'


def demo_grouparg(share_def):
    foo = 0
    if 'd' in share_def:
        foo += 1
        print('d')
    if 'e' in share_def:
        print('e')
        foo += 2
    if 'f' in share_def:
        print('f')
        foo += 4
    print(foo)
    return foo


def build_parser():
    def csv(stringtarget):
        return stringtarget.split(',')

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument(
        '-c',
        '--csv',
        type=csv,
        help='take in options from a csv split string',
        default='thing1,thing2',
        dest='csv_items')
    # A list of items in csv form
    parser.add_argument(
        '-x',
        '--example',
        help='test example',
        action='store_true',
        dest='xample',
        default=False)
    nonexclusive_group = parser.add_argument_group('nonexclusive',
                                                   'Pick d,e, and/or f')
    # A shared var example w/o groups.  Set the dest and the action of
    # append_const will push the const to that name.
    nonexclusive_group.add_argument(
        '-d',
        help='opt d',
        const='d',
        action='append_const',
        dest='sdef')
    nonexclusive_group.add_argument(
        '-e',
        help='opt e',
        const='e',
        action='append_const',
        dest='sdef')
    nonexclusive_group.add_argument(
        '-f',
        help='opt f',
        const='f',
        action='append_const',
        dest='sdef')

    exclusive_group = parser.add_mutually_exclusive_group()
    # Set the dest the same across the two arguments,
    # then use the action `store_const` to push the contents
    # of const to the shared dest.
    exclusive_group.add_argument(
        '-a',
        help='exclusive example a',
        action='store_const',
        const='aaaaa',
        dest='xclusive')
    exclusive_group.add_argument(
        '-b',
        help='exclusive example b',
        action='store_const',
        const='bbbbb',
        dest='xclusive')
    # set a default of 'bbbbb' for the group
    parser.set_defaults(xclusive='bbbbb')

    return parser


if __name__ == '__main__':  # pragma: no cover
    parser = build_parser()
    args = parser.parse_args()
    pprint.pprint(args)
    if not args.sdef:
        sdef = ['d', 'e', 'f']
    else:
        sdef = args.sdef

    demo_xclusive(xclusive=args.xclusive)
    demo_grouparg(share_def=sdef)
    if args.csv_items:
        for i in args.csv_items:
            print('csv: {}'.format(i))
