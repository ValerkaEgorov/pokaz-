#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import csv

Utf8 = codecs.lookup ( 'utf-8' )

with open ( u'data.txt', 'rt' ) as TRG :
    RD = csv.reader ( TRG )
    for Record in RD :
        Record = [ Utf8.decode (X) [0] for X in Record ]
        print Record
        