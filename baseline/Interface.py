#!/usr/bin/env python

import sys
import os.path as path

import Tkinter as tk

import Loader
import Understand
import Control
import NLG

import time

listfile = '/home/yipeiw/Documents/dialogue/cnn_qa.list'

rescource_root = '/home/yipeiw/Documents/dialogue/baseline/resource'
template_list=['template/template_new.txt', 'template/template_end.txt', 'template/template_open.txt', 'template/template_expand.txt']

template_list = [path.join(rescource_root, name) for name in template_list]

topicfile = path.join(rescource_root, 'topic.txt')

def Init(listfile, template_list):
	global database, resource, TemplateLib, TopicLib
	datalist=[line.strip() for line in open(listfile)]

	start_time = time.time()
	print "loading resource and database"
	database = Loader.LoadDataPair(datalist)
	resource = Loader.LoadLanguageResource()
	TemplateLib = Loader.LoadTemplate(template_list)
	TopicLib = Loader.LoadTopic(topicfile)
	print "complete successfully ", time.time()-start_time
	#print "data pair %s" % (len(database['Q'].values()))

	global TreeState, Template
	TreeState, Template = Control.Init()

def Response(content):
	global database, resource, TemplateLib, TopicLib
	global TreeState, Template

	relavance, answer = Control.FindCandidate(database, resource, content)
	state = Control.SelectState(relavance, TreeState)
	print 'state:', state['name']
	print "candidate answer ", relavance, answer
	output = NLG.FillTemplate(TemplateLib, TopicLib, Template[state['name']], answer)	
	#output = NLG.GenerateResponsePair(TopicLevel, Candidates)
	return output

def getText(event):
	global input_editor
	content = input_editor.get("1.0", 'end')
	UpdateDialogue(content.strip(), 'user')
	input_editor.delete("1.0", 'end')	
	output = Response(content)
	UpdateDialogue(output, 'agent')

def UpdateDialogue(output, role):
	global conversation
	conversation.config(state='normal')
	conversation.insert('end', "\n%s: %s\n" % (role, output))
	conversation.config(state='disabled')
	conversation.yview_pickplace("end")
	
root = tk.Tk()
root.title('dialogue')
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side='right', fill='y')

conversation = tk.Text(root, width=root.winfo_screenwidth(), font=14)
conversation.config(state='disabled', yscrollcommand=scrollbar.set)
conversation.pack()

scrollbar.config(command=conversation.yview)

linput = tk.Label(root, font=20, width=root.winfo_screenwidth()) 
linput.config(text="Type to the Agent in the window below")
linput.pack()

input_editor = tk.Text(root, height=4, width=root.winfo_screenwidth(), font=14)
input_editor.bind('<Return>', getText)
input_editor.pack()

logtext = tk.StringVar()
log = tk.Label(root, font=20, width=root.winfo_screenwidth(), textvariable=logtext)
log.pack()

Init(listfile, template_list)
logtext.set('Complete Initialization successfully\n Welcome to use our System')

root.mainloop()
