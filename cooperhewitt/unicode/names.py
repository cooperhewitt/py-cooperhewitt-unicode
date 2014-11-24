#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

class lookup:

    def __init__(self, data):
        fh = open(data, 'r')
        self.lookup = json.load(fh)

    def name(self, char):        
        id = ord(char)
        hex = "%04x" % id

        return self.lookup[hex]

if __name__ == '__main__':

    import sys

    source = sys.argv[1]
    char = sys.argv[2]

    char = char.decode('utf-8')

    l = lookup(source)
    name = l.name(char)

    print "%s is %s" % (char, name)
