#!/usr/bin/env python

import sys
import cooperhewitt.unicode.names as names

if __name__ == '__main__':

    source = sys.argv[1]
    input = sys.argv[2:]

    input = ' '.join(input)
    input = input.decode('utf-8')

    ref = names.lookup(source)

    for char in input:

        if char == ' ':
            print char
            continue

        name = ref.name(char)
        print name 

    # print "%s is %s" % (char, name)
