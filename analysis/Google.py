#!/usr/bin/env python

import sys
sys.path.append('/home/yipeiw/Documents/dialogue/baseline')

import time
import os.path as path

import subprocess

queryfile = 'query.txt'
outputfile = 'Google.txt'

def GoogleAPIWrapper(tool, phrase):
	subprocess.call(['java', '-jar', tool, phrase])
	answer = []
	for line in open('result.txt'):
		if line.strip().find('no results, sorry!')!=-1:
			continue
		answer.append(line.strip())
	return answer

tool = 'google_api3.jar'

fout = open(outputfile, 'w')
count = 0
for line in open(queryfile):
	count += 1
	input_utter = line.strip()
	answer = GoogleAPIWrapper(tool, input_utter)
	print "Q: ", input_utter
	fout.write("Q%s\t%s\n" % (count, input_utter))
	num = 1
	for item in answer:
		fout.write("Answer%s\t%s\n" % (num, item))
		num += 1
fout.close()
	
