dialogue project (2014 spring)
================
<b>Pipeline for conversation strategy</b>

text input-output system 
<br>baseline/Interface.py</br>

* NLU component
  <br>code: baseline/Understander.py</br>
* Retrival component
  <br>code: basedline/Retrieval.py</br>
  <br>(reverse index can be used when database increased)</br>
 
  The conversation databased we collected is here:
  <br>https://drive.google.com/file/d/0B7XJjU2\_aDgsTnVZM0FjbVk0UTQ/edit</br>

* Dialogue Management component
  <br>code: baseline/Control.py</br>
* NLG coponent
  <br>code: baseline/NLG.py</br>
  <br>The templates and topic words are in baseline/resouce</br>

* Using Google API
  <br>Python Wrapper for jar pacakge based on Google API, testing the result from Google API</br>
  <br>code: analysis/Google.py</br>

Algorithm details can be refered to the slides

<b>Dependencies</b>
<br>nltk http://www.nltk.org/</br>
<br>Tkinter https://wiki.python.org/moin/TkInter</br>
