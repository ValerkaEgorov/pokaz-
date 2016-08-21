#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import sys

Utf8 = codecs.lookup ( 'utf-8' )
Cp866 = codecs.lookup ( 'cp866' )

with open ( u'data.txt', 'rt' ) as TRG :
    for Line in TRG :
        if Line[-1] == '\n' : Line = Line[:-1]
        Text = Utf8.decode ( Line ) [0]
        sys.stdout.write ( Cp866.encode(Text)[0] )
        sys.stdout.write ( '\n' )
