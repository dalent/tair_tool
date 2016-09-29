#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import struct
#tair version
TAIR_HTM_VERSION=0x31766257

class tair_server_conf:
    def getHashtableSize():
        return server_bucket_count * server_copy_count 

    def __init__(self, server_table):
        with open(server_table, "rb") as fh:
            self.flag =  readInt(fh)
            if self.flag != TAIR_HTM_VERSION:
                print "not server  group file:"
                sys.exit()
            self.client_version =  readInt(fh)
            self.server_version =  readInt(fh)
            self.plugins_version =  readInt(fh)
            self.area_capacity_version =  readInt(fh)
            self.last_load_config_time =  readInt(fh)
            self.migrate_block_count =  readInt(fh)
            self.server_copy_count =  readInt(fh)
            self.server_bucket_count =  readInt(fh)

    def printSelf(self):
       print "flag: 0x%x " % self.flag 
       print "client_version: %d "  % self.client_version
       print "server_version: %d "  % self.server_version
       print "plugins_version: %d "  % self.plugins_version
       print "area_capacity_version: %d " %  self.area_capacity_version
       print "last_load_config_time: %d" % self.last_load_config_time
       print "migrate_block_count: %d" %  self.migrate_block_count
       print "server_copy_count: %d" %  self.server_copy_count
       print "server_bucket_count: %d" % self.server_bucket_count

    pass


if len(sys.argv) < 2:
    print "no file name"
    sys.exit()

#读取大端数据
def readInt(fh):
    intRet = 0
    for i in range(4):
        byte = fh.read(1)
        intRet =  intRet | (ord(byte) << (i*8))
    return intRet

server_table = sys.argv[1]
conf = tair_server_conf(server_table)
conf.printSelf()
