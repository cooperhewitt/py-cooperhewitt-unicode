#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import logging

class lookup:

    def __init__(self, data):
        fh = open(data, 'r')
        self.lookup = json.load(fh)

    def name(self, char):        
        id = ord(char)
        hex = "%04X" % id

        logging.debug("char: %s id: %s hex: %s" % (char, id, hex))
        return self.lookup.get(hex, None)

if __name__ == '__main__':

    import sys

    source = sys.argv[1]
    input = sys.argv[2]

    char = char.decode('utf-8')

    ref = names.lookup(source)
    name = ref.name(char)

    print "%s is %s" % (char, name)
