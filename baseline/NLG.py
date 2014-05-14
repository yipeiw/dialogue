#!/usr/bin/env python

import random

def GenerateResponsePair(TopicLevel, Candidates, refine_strategy=-1):
        if TopicLevel==-1: #off topic
                output = 'Ok. Tell me more about yourself.'
        else:
		select = random.choice(Candidates)
		pair = [select[1], select[2]]
                output = [" ".join(pair[0]), " ".join(pair[1])]

        return output

def FillTemplate(TemplateLib, TopicLib, template, answer=[]):
	answerString = ' '.join(answer)

	sent_list = []
	for item in template:
		for unit in item.split(','):
			if unit=='answer':
				sent_list.append(answerString)		
			elif unit=='topic':
				sent_list.append(random.choice(TopicLib))
			else:
				sent_list.append(random.choice(TemplateLib[unit]))
	print "template answer ", sent_list
	return ' '.join(sent_list)
