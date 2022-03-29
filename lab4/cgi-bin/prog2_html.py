#!/usr/bin/python3
# import datetime

import sys
import re
t = sys.stdin.read()
json =t.split('\n')
t=""
for i in range(len(json)):
    t=t+" "+json[i]
t=re.sub('^\s','',t)
total = re.findall('\"total\" : (\d+),', t)
print("Content-type: text/html; charset=utf-8\n\n<html><body bgcolor=yellow>")
print("<b>Found: "+total[0]+"</b><hr><ol>")
title = re.findall('"title":"(.*?)",', t)
text = re.findall('"textBody":"(.*?)",', t)
url = re.findall('"URL":"(.*?)"', t)
for i in range(len(title)):
    doc_ind=i+1
    print("<li><b>"+": "+title[i]+"</b>")
    print("<br>"+text[i])
    print("<br><i>"+url[i]+"</i><br><hr>")
print("</ol></body></html>")
