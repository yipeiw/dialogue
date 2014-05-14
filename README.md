dialogue project (2014 spring)
================
Pipeline for conversation strategy

text input-output system 
baseline/Interface.py

* NLU component
  code: baseline/Understander.py
* Retrival component
  code: basedline/Retrieval.py
  (reverse index can be used when database increased)
 
  The conversation databased we collected is here:
  https://drive.google.com/file/d/0B7XJjU2\_aDgsTnVZM0FjbVk0UTQ/edit

* Dialogue Management component
  code: baseline/Control.py
* NLG coponent
  code: baseline/NLG.py
  The templates and topic words are in baseline/resouce

Dependencies
nltk http://www.nltk.org/
Tkinter https://wiki.python.org/moin/TkInter
