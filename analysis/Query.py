#!/usr/bin/env python

import sys
sys.path.append('/home/yipeiw/Documents/dialogue/baseline')

import Loader
import Control
import NLG

queryfile = 'query.txt'

root = '/home/yipeiw/Documents/dialogue/cnn-qa-json/questions-json/'
datalist=[root + '110118pmt.qa.json']

#database = Loader.LoadData(datalist)
database = Loader.LoadDataPair(datalist)
resource = Loader.LoadLanguageResource()

print "load resource and database successful"

for line in open(queryfile):
	input_utter = line.strip()
	print "Q: ", input_utter
	print ""

	#Candidates, TopicLevel = Control.FindResponse(database, resource, input_utter)
	#output = NLG.GenerateResponse(TopicLevel, Candidates)
	Candidates, TopicLevel = Control.FindResponsePair(database, resource, input_utter)
        output = NLG.GenerateResponsePair(TopicLevel, Candidates)

	print "A: ", output
	print "\nCandidates:"
	for score, wordlist1, wordlist2 in Candidates:
		print score
		print " ".join(wordlist1)
		print " ".join(wordlist2)
		print ""
