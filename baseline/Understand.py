#!/usr/bin/etc python

import nltk

from collections import defaultdict


def AddWeight(tag_list, rules, stop_dict):
	result = []
	for token, pos in tag_list:
		if rules[pos]>0:
			result += [(token, pos, rules[pos])]
		else:
			if pos==".":
				continue
			if not stop_dict[token]:	
				result += [(token.lower(), pos, 1)]
	return result

#return [(token, pos_tag, weight)]
def InfoExtractor(utter, resource):
	rules = resource['rules']
	stop_dict = resource['stop_words']

	tag_list = nltk.pos_tag(nltk.word_tokenize(utter))
	return AddWeight(tag_list, rules, stop_dict)

