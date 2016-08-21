#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import os, os.path
import zipfile
import argparse

AP = argparse.ArgumentParser ( description = u'Folder zipper' )
AP.add_argument ( u'folder', type = unicode )
AP.add_argument ( u'-m', u'--mask', type = unicode, default = None )
ARGS = AP.parse_args()

if ARGS.mask :
    TXT = re.compile ( ARGS.mask )
else :
    TXT = None

with zipfile.ZipFile ( ARGS.folder + u'.zip', 'w' ) as TRG :
    for ( path, dirs, files ) in os.walk ( ARGS.folder ) :
        for f in files :
            if TXT :
                if not TXT.search ( f ) :
                    continue
            P = os.path.join ( path, f )
            TRG.write ( P )
    