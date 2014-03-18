#!/usr/bin/etc python

threshold = 5
res_stat={'start':'sil', 'greeting':'greeting', 'engage':'sil','topicQ':'topicQ', 'topicA':'topicA', 'off':'topicQ', 'end':'end'}

import Understand
import Retrieval

def TaskTransit(TaskRules, stat, info, history = []):
	pre_stat = history[len(history)-1]
	history += [stat]

	(reach, in_topic, act) = info
	next_stat = TaskRules[(stat, reach, in_topic, act)]
	history += [next_stat]

	res_decision = res_stat[stat]
	while res_decision=='sil':
		next_next = TaskRules[(next_stat, reach, in_topic, act)]
	        res_decision = res_stat[next_stat]
		
		stat = next_stat
		next_stat = next_next
		history += [next_stat]

	return next_stat, res_decision, history

def FindResponse(database, resource, input_utter, history = []):
	meta_info = Understand.InfoExtractor(input_utter, resource)
	print "Understand"
	print meta_info
	print ""

	Candidates, TopicLevel = Retrieval.FreqMatch(meta_info, database)		
	return Candidates, TopicLevel

def FindResponsePair(database, resource, input_utter, history = []):
        meta_info = Understand.InfoExtractor(input_utter, resource)
        print "Understand"
        print meta_info
        print ""

        Candidates, TopicLevel = Retrieval.FreqPairMatch(meta_info, database)       
        return Candidates, TopicLevel

