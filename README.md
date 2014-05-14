dialogue project (2014 spring)
================
<b>Pipeline for conversation strategy</b>

text input-output system 
baseline/Interface.py

* NLU component
  <br>code: baseline/Understander.py</br>
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

Algorithm details can be refered to the slides

Dependencies

nltk http://www.nltk.org/
Tkinter https://wiki.python.org/moin/TkInter
