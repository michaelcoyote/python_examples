#!/usr/bin/env python


class TestObj(object):
    """A test object for data."""

    def __init__(self, dat1, dat2, dat3):
        """Return a new TestObj object.

        Make sure that dat1 is shorter than 10 characters.
        """
        if len(dat1) < 10:
            self._dat1 = dat1
        else:
            raise ValueError("dat1 is longer than 10 char: {}" % dat1)

        self._dat2 = dat2
        self._dat3 = dat3

    def __str__(self):
        """Stringify data from object."""
        return('dat1: {} dat2: {} dat3: {}'
               .format(self._dat1, self._dat2, self._dat3))
