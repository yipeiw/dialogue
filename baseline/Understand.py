#!/usr/bin/etc python

import nltk

from collections import defaultdict

topic_dict = defaultdict(bool)
topic_list=['movie', 'skyfall', 'actor', 'director']
for topic in topic_list:
	topic_dict[topic] = True

def AddWeight(tag_list, rules, stop_dict):
	result = []
	for token, pos in tag_list:
		if rules[pos]>0:
			result += [(token, pos, rules[pos])]
		else:
			if not stop_dict[token]:	
				result += [(token, pos, 1)]
	return result

#return [(token, pos_tag, weight)]
def InfoExtractor(utter, resource):
	rules = resource['rules']
	stop_dict = resource['stop_words']

	tag_list = nltk.pos_tag(nltk.word_tokenize(utter))
	return AddWeight(tag_list, rules, stop_dict)

def PredictAct(utter, info_list):
	if utter.find('?')!=-1:
		return "ques"
	return "other"
	
def CheckTopic(info_list):
	noun_list = ['NN', 'NNP', 'NNS', 'NNPS']
	for token, pos, weight in info_list:
		if pos in noun_list:
			if topic_dict[token]:
				return True
	return False

