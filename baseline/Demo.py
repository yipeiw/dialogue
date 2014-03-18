#!/usr/bin/env python

import sys

import Loader
import Understand
import Control
import NLG
#import Log

"""
config=sys.argv[1]
filelist{}
for line in open(config):
	(name, filepath) = line.strip().split(',')
	filelist[name] = filepath
"""

rulefile = 'knowledge.txt'

print "importing resource ..."
weight_rules,stop_dict = Loader.LoadLanguageResource()
TaskRules = Loader.LoadTaskRule(rulefile)

print "complete loading"
#print TaskRules
#print weight_rules

threshold = 4
#initialize
init_stat='start'
reach_goal = 0
act='none'
in_topic = 0
history=['none']
current_stat, res_decision, history = Control.TaskTransit(TaskRules, init_stat, (reach_goal, in_topic, act), history)
turns=0
output = NLG.Response(res_decision)
print "Agent: " + output

while True:
	#take input from user and perform understanding
	user_utter = raw_input()
	info_list = Understand.InfoExtractor(user_utter, weight_rules, stop_dict)
	print info_list
	act = Understand.PredictAct(user_utter, info_list)	
	in_topic = Understand.CheckTopic(info_list)
	print act, in_topic

	#Decide the next state and response strategy
	next_stat, res_decision, history = Control.TaskTransit(TaskRules, current_stat, (reach_goal, in_topic, act), history)
	print "next stat: ", next_stat 
	print "response decision: ", res_decision
	print "history: ", history

	#Generate Response
	output = NLG.Response(res_decision, info_list)
	print "Agent: ", output

	#update state
	turns += 1
	reach_goal = (turns > threshold)
	if reach_goal and stat=='start':
		print "Agent: Thank you. The task complete."
		break
	#Log.write()
	current_stat = next_stat

print history
