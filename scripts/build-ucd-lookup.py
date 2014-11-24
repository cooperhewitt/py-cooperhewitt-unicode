#!/usr/bin/env python

import sys
import urllib
import csv
import json

if __name__ == '__main__':

    ucd = 'http://unicode.org/Public/UCD/latest/ucd/UnicodeData.txt'
    rsp = urllib.urlopen(ucd)

    reader = csv.reader(rsp, delimiter=';')

    lookup = {}

    for row in reader:
    
        hex = row[0]
        name = row[1]
        lookup[hex] = name

    json.dump(lookup, sys.stdout)
    sys.exit()
