#!/usr/bin/python
# -*- coding: utf-8 -*-

L = [
    ( 25, u'Moscow' ),
    ( 30, u'Paris' ),
    ( 1, u'Washington' ),
    ( 1024, u'Rio-de-Janeiro' ),
    ]

for Data in L :
    X = u'Total %4d items in %-15s this summer' % Data
    print X