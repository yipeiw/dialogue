#!/usr/bin/env python

from Retrieval import *

def GenerateResponse(TopicLevel, Candidates, refine_strategy=-1):
	if TopicLevel==-1: #off topic
		output = 'Ok. Tell me more about yourself.'
	else:
		output = " ".join(Refine(Candidates, refine_strategy))
        return output


def GenerateResponsePair(TopicLevel, Candidates, refine_strategy=-1):
        if TopicLevel==-1: #off topic
                output = 'Ok. Tell me more about yourself.'
        else:
		pair = [Candidates[0][1], Candidates[0][2]]
                output = [" ".join(pair[0]), " ".join(pair[1])]

        return output


def Refine(candidates, refine_strategy=-1):
	"""
	to do
	add connect word: agree, diagree, disengage topic
	"""
	return candidates[0][1]
