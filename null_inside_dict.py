#!/usr/bin/env python
# coding: utf-8
"""None vs. empty dict"""
t2 = {None}  # noqa
t3 = dict()  # noqa
if (t2 == t3):
    print('t2 and t3 are the same')
