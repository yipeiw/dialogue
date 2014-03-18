#!/usr/bin/etc python

import nltk
from collections import defaultdict

def LoadLanguageResource():
	WeightRules=defaultdict(int)
	nounlist = ['NN', 'NNS', 'NNP', 'NNPS']
	for noun in nounlist:
        	WeightRules[noun] = 3;

	stop_dict=defaultdict(bool)
	for word in nltk.corpus.stopwords.words('english'):
        	stop_dict[word] = True
	return WeightRules, stop_dict

def GenerateCases(stat, next_stat, reach_goal, in_topic, act):
	stats=['start','greeting','engage','topicA', 'topicQ','end','off']
	vals=[0,1]
	acts=['ques', 'other', 'none']
	
	result = []
	
	if stat=='all':
		stat_list = stats
	else:
		stat_list = [stat]
	if next_stat=='all':
		next_list = stats
	else:
		next_list = [next_stat]
	if reach_goal==-1:
		reach_list = vals
	else:
		reach_list = [reach_goal]
	if in_topic==-1:
		in_list = vals
	else:
		in_list = [in_topic]
	if act=='all':
		act_list = acts
	else:
		act_list = [act]

	for stat in stat_list:
		for next_stat in next_list:
			for reach in reach_list:
				for in_topic in in_list:
					for act in act_list:
						result += [ ((stat, reach, in_topic, act), next_stat) ]
	return result


"""
format: current_stat,pre_stat,next_stat,response,reach_goal, in_topic 
"none", "all" state for representation simplification
"""
def LoadTaskRule(rulefile):
	TaskRules = {}
	f = open(rulefile)
	head = f.readline()
	while True:
		line = f.readline()
		if not line:
			break
		stat, next_stat, reach_goal, in_topic, act = line.strip().split(',')
		for case, decision in GenerateCases(stat, next_stat, int(reach_goal), int(in_topic), act):
			TaskRules[case] = decision
	return TaskRules 
