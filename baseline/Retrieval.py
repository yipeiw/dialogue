#!/usr/bin/env python

"""
find answer in database and by search engine
"""

from collections import defaultdict

def UpdateCandidate(utter, score, Candidate, select):
	add = False
	if len(Candidate) < select:
		Candidate += [(score, utter)]
		add = True
	else:
		if score > Candidate[select-1][0]:
			Candidate[select-1] = (score, utter)
			add = True
	if add:
		return sorted(Candidate, key=lambda item:item[0], reverse=True)
	else:
		return Candidate

def FreqMatch(info, database, select=3):
	occur_dict = defaultdict(bool)
	occur_dict.clear()
	info_dict = {}
	for word, pos, weight in info:
		occur_dict[word] = True
		info_dict[word] = (pos, weight)

	Candidate = []
	for utter in database.values():
		score = 0
		for token in utter:
			if occur_dict[token]:
				score += info_dict[token][1]	#weight
		score = float(score)/len(utter)
		if score > 0:
			Candidate = UpdateCandidate(utter, score, Candidate, select)
	if len(Candidate)>0:
		topiclevel = 1
	else:
		topiclevel = -1	
	return Candidate, topiclevel

def FreqPairMatch(info, database, select=3):
        occur_dict = defaultdict(bool)
        occur_dict.clear()
        info_dict = {}
        for word, pos, weight in info:
                occur_dict[word] = True
                info_dict[word] = (pos, weight)

        Candidate = []
        for idx, utter in database['Q'].items():
                score = 0
                for token in utter:
                        if occur_dict[token]:
                                score += info_dict[token][1]    #weight
                score = float(score)/len(utter)
                if score > 0:
                        Candidate = UpdateCandidatePair(idx, database, score, Candidate, select)

        if len(Candidate)>0:
                topiclevel = 1
        else:
                topiclevel = -1

        return Candidate, topiclevel

def UpdateCandidatePair(idx, database, score, Candidate, select):
        add = False
        if len(Candidate) < select:
                Candidate += [(score, database['Q'][idx], database['A'][idx])]
                add = True
        else:
                if score > Candidate[select-1][0]:
                        Candidate[select-1] = (score, database['Q'][idx], database['A'][idx])
                        add = True
        if add:
                return sorted(Candidate, key=lambda item:item[0], reverse=True)
        else:
                return Candidate

def SearchEngine(info):
	return candidate
