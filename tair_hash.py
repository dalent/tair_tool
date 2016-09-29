#!/usr/bin/env python
# -*- coding: utf-8 -*-

import struct
import sys
import numpy
prefix="04"
magic = 0x5bd1e995
def mur_mur_hash(key):
    buf = bytearray(key)
    length = len(buf)
    h = int(97 ^ length) 
    index = 0
    while(length >= 4):
        k, = struct.unpack_from("<I", buf, index)
        k &= 0xffffffff
        k *= magic
        k &= 0xffffffff
        k ^= (k >> 24)
        k &= 0xffffffff
        k *= magic
        k &= 0xffffffff

        h *= magic
        h &= 0xffffffff

        h ^= k
        h &= 0xffffffff
        index += 4
        length -= 4

    if 3 == length:
        h ^= (buf[index + 2] << 16)
        h &= 0xffffffff

    if 2 <= length:
        h ^=(buf[index + 1] << 8)
        h &= 0xffffffff

    if 1 <= length:
        h ^= buf[index]
        h *= magic

        
    h &= 0xffffffff
    h ^= (h >> 13)
    h *= magic
    h &= 0xffffffff
    h ^= (h >> 15)
    return h & 0xffffffffL
    pass

if len(sys.argv) != 3:
    print "usage:"
    print "       %s %s" %(sys.argv[0],"key bucket")
    exit(0)
key=sys.argv[1]
bucket=int(sys.argv[2])
print "%d" %( mur_mur_hash(b"\0\4" + key) % bucket)
