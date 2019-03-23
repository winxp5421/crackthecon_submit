#!/usr/bin/env python2

import re
import sys
import json
import requests

if len(sys.argv) != 2:
    sys.exit("Usage: %s cracked_hashes.txt" % sys.argv[0])

baseurl = 'https://crackthecon.com/api/submit.php'
token   = 'Add your token here'

if not re.match('^[0-9A-Za-z]{64}$', token):
    sys.exit('Check your token.')

count  = 0
founds = []
with open(sys.argv[1], 'r') as in_file:
    for line in in_file:
        line = line.rstrip('\r\n')
        pos = line.find('$HEX[')
        if pos > -1:
            prefix = line[:pos]
            pw_dec = line[pos+5:-1].decode('hex')
            line = prefix + pw_dec
        founds.append(line)

data = {u"key": token, u"found": founds}
response = requests.post(baseurl, json.dumps(data))
print response.content
