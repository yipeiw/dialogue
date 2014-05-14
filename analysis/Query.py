#!/usr/bin/env python

import sys
sys.path.append('/home/yipeiw/Documents/dialogue/baseline')

import Loader
import Control
import NLG
import Retrieval
import Understand

import time
import os.path as path


queryfile = 'query.txt'
listfile = '/home/yipeiw/Documents/dialogue/cnn_qa.list'
outputPath = 'data'

def outputAnswer(outputfile, Candidates, input_utter):
	fout = open(outputfile, 'w')
	fout.write("Question\t%s\n" % (input_utter))
	num = 1
	for score, qstring, astring, tag in Candidates:
		fout.write("Anwser%s\t%s\t%.3f\t%s\n" % (num, astring, score, tag))
		num += 1
	fout.close()

def Filter(Candidates):
	result = []
	answers = []
	for score, qlist, alist, tag in Candidates:
		if len(alist) > 15:
			continue
		qstring = " ".join(qlist)
                astring = " ".join(alist)
		
		if astring.find('--')!=-1 or astring.find(':')!=-1:
			continue
		if astring in answers:
			continue
		result.append( (score, qstring, astring, tag) )
		answers.append(astring)
	rank_result = sorted(result, key=lambda item:item[0], reverse=True)
	last = min(len(rank_result), 5)
	return rank_result[0:last]

datalist=[line.strip() for line in open(listfile)]

start_time = time.time()
print "loading resource and database"
database = Loader.LoadDataPair(datalist)
resource = Loader.LoadLanguageResource()
print "complete successfully ", time.time()-start_time
#print "data pair %s" % (len(database['Q'].values()))

count = 0
for line in open(queryfile):
	count += 1
	input_utter = line.strip()
	outputfile = path.join(outputPath, str(count)+'.txt')

	print "Q: ", input_utter
	print ""
	
	#Candidates, TopicLevel = Control.FindResponsePair(database, resource, input_utter)
        #output = NLG.GenerateResponsePair(TopicLevel, Candidates)
	meta_info = Understand.InfoExtractor(input_utter, resource)
	Candidates, TopicLevel = Retrieval.FreqPairMatch(meta_info, database)   
	print "\nCandidates:"
	for score, wordlist1, wordlist2, tag in Candidates:
		print score
		print " ".join(wordlist1)
		print " ".join(wordlist2)
		print tag
		print ""
	print len(Filter(Candidates))

	outputAnswer(outputfile, Filter(Candidates), input_utter)
	
