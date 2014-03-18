#!/usr/bin/etc python

import nltk
from collections import defaultdict
import json

def LoadLanguageResource():
        WeightRules=defaultdict(int)
        nounlist = ['NN', 'NNS', 'NNP', 'NNPS']
        for noun in nounlist:
                WeightRules[noun] = 3;

        stop_dict=defaultdict(bool)
        for word in nltk.corpus.stopwords.words('english'):
                stop_dict[word] = True
	resource = {}
	resource['rules'] = WeightRules
	resource['stop_words'] = stop_dict
        return resource

def LoadData(datalist):
	database = {}
	for datafile in datalist:
		f = open(datafile)
		line = f.readline()
		f.close()
		raw_data = json.loads(str(line.strip()))
		database = PushData(raw_data, database)
	return database

def PushData(data, database):
	last = len(database.keys())
	for pair in data:
		database[last] = pair['question'].split()
		last += 1
		database[last] = pair['answer'].split()		
		last += 1
	return database

def LoadDataPair(datalist):
        database = {}
	database['Q'] = {}
	database['A'] = {}

        for datafile in datalist:
                f = open(datafile)
                line = f.readline()
                f.close()
                raw_data = json.loads(str(line.strip()))
                database = PushDataPair(raw_data, database)
        return database

def PushDataPair(data, database):
        last = len(database['Q'].keys())
        for pair in data:
                database['Q'][last] = pair['question'].split()
                database['A'][last] = pair['answer'].split()
                last += 1
        return database

