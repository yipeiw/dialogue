#!/usr/bin/etc python

import Understand
import Retrieval
import random

def Init():
	Tree = ConstructTree()
	Template = ConstructTemplate()
	return Tree, Template


def FindCandidate(database, resource, input_utter, history = []):
        meta_info = Understand.InfoExtractor(input_utter, resource)
        print "Understand"
        print meta_info
        print ""

        Candidates, TopicLevel = Retrieval.FreqPairMatch(meta_info, database)      
	relavance, answer,tag = Retrieval.Select(Candidates) 
	print "answer from ", tag

        return relavance, answer

def SelectState(relavance, TreeState):
	branch_idx = TreeState.keys()[0]
	branch = TreeState[branch_idx]['node']
	if relavance >= branch['threshold']:
		return random.choice(TreeState[branch_idx][True])
	else:
		return random.choice(TreeState[branch_idx][False])

def ConstructTree():
        Tree = {}
        branch = {'tag':'criteria', 'name':'relavance', 'threshold':0.25}
        switch_state = {'tag':'state', 'name':'switch'}
        end_state = {'tag':'state', 'name':'end'}
        continue_state  = {'tag':'state', 'name':'continue'}
        expand_state = {'tag':'state', 'name':'expand'}

        Tree[0] = {'node':branch}
        Tree[0][True] = [continue_state, expand_state]
        Tree[0][False] = [switch_state, end_state]
        return Tree

def ConstructTemplate():
        template = {}
        template['switch'] = ['template_end', 'template_new,topic']
        template['end'] = ['answer', 'template_open']
        template['continue']=['answer']
        template['expand'] = ['answer', 'template_expand']
        return template
		
