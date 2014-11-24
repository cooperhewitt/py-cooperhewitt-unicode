#!/usr/bin/env python

import sys
import cooperhewitt.unicode.names as names

if __name__ == '__main__':

    source = sys.argv[1]
    char = sys.argv[2]

    char = char.decode('utf-8')

    ref = names.lookup(source)
    name = ref.name(char)

    print "%s is %s" % (char, name)
