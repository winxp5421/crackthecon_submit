import requests
import sys
import json

baseurl		= 'https://crackthecon.com/api/submit.php'
count			= 0
token			= 0
input_file		= sys.argv[1]
in_file		= open(input_file, 'r')

with open('token', 'r') as token_file:
    token = token_file.read().rstrip()

founds, data	= [], []
for line in in_file:
    founds.append(line.rstrip())
    data = {u"key": token, u"found": founds }

response = requests.post(baseurl, json.dumps(data))
print response.content
