#!/usr/bin/env python

import Loader
from collections import defaultdict
import nltk

listfile = '/home/yipeiw/Documents/dialogue/cnn_qa.list'

datalist=[line.strip() for line in open(listfile)]
database = Loader.LoadDataPair(datalist)

freq_dict = defaultdict(int)

noun_list=['NN', 'NNP', 'NNS', 'NNPS']
for idx, word_list in database['Q'].items():
	tag_list = nltk.pos_tag(nltk.word_tokenize(" ".join(word_list)))
	print "Q", idx
	for token, tag in tag_list:
		if tag in noun_list:	
			freq_dict[token] += 1

for idx, word_list in database['A'].items():
	tag_list = nltk.pos_tag(nltk.word_tokenize(" ".join(word_list)))
	print "A", idx
        for token, tag in tag_list:
                if tag in noun_list:
                        freq_dict[token] += 1

stop_dict=defaultdict(bool)
for word in nltk.corpus.stopwords.words('english'):
	stop_dict[word] = True

outputfile = '/home/yipeiw/Documents/dialogue/baseline/resource/topictest.txt'
fout = open(outputfile, 'w')
for word, freq in sorted(freq_dict.items(), key=lambda item:item[1], reverse=True):
	if not stop_dict[word]:
		fout.write("%s %s\n" % (word, freq))
fout.close()

