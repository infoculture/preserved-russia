#!/usr/bin/env python
import os
from py7zlib import Archive7z

THEPATH =  '/mnt/ogd/IVBBackup_1/mirrors'
f = open('files.txt')
for filename in f:
    name = THEPATH + '/' + filename.strip()
    if os.path.exists(name):
        f = open(name, 'rb')
        archive = Archive7z(f)
        filenames = archive.getnames()
        total = 0
        print dir(archive)
#        for filename in filenames:
#            cf = archive.getmember(filename)
#            total += cf.uncompressed
#        print total
#        print os.stat(name)[6]
    else:
        print 0