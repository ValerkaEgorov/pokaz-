#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs

Win1251 = codecs.lookup ( 'windows-1251' )

Text = u'Привет, мир!!!'

( Bytes, N ) = Win1251.encode ( Text )

with open ( u'file.txt', 'wt' ) as TRG :
    TRG.write ( Bytes ) 