#!/usr/bin/env python

import json

f = open('/home/yipeiw/Documents/dialogue/cnn-qa-json/questions-json/110120pmt.qa.json')

line = f.readline()
f.close()

data = json.loads(str(line.strip()))

print data[0].keys()
#answer, question, dcId, sentId
print data[0].values()
print len(data)
