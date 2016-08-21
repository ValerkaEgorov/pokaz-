#!/usr/bin/python
# -*- coding: utf-8 -*-

import mNakladnaya

if __name__ == '__main__' :
    Nak = mNakladnaya.create ()
    
    Nak.append_blank ( title = u'Карандаши', unit = u'шт' )
    Nak.append_blank ()
    Nak.append_blank ()
    print unicode(Nak)
    
    