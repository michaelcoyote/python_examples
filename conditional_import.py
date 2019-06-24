#!/usr/bin/env python
"""Conditional import.

Testing a quick conditional import scenario where we only initiate
and use the imported function inside a conditional."""

import requests


class ImportTest1(object):
    def __init__(self, greet='world', gh_user=None):
        if gh_user:
            self.gh_user = gh_user
            self.req = requests.get('https://api.github.com/users/{}'
                                    .format(gh_user))
        self.greet = greet

    def hello(self):
        print('hello, {}'.format(self.greet))
        if self.gh_user:
            print('hello, {}'.format(self.req.json()['name']))
            print('your name was determined by looking up your GH '
                  'username: {}'.format(self.gh_user))


def main():
    it1 = ImportTest1(greet='folks', gh_user='michaelcoyote')
    it1.hello()


if __name__ == '__main__':
    main()
