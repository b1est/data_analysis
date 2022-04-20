#!/usr/bin/python3

import re
import json
import cgi
import subprocess
#Виклик CGI-процедури i приймання параметрiв
form = cgi.FieldStorage()
query = form.getfirst("query", "")
src = form.getfirst("src", "")
#Опрацьовуємо параметри i формуємо частину запиту вiдповiдно до того
#за якими параметрами виконується пошук
if query!="" and src!="":
    st = '{{"query": {{"bool": {{"must": [{{"multi_match": {{"query": {}, "fields":["textBody", "title"]}}}}],"filter": [{{"match": {{"source": {}}}}}]}}}}}}'.format(json.dumps(query), json.dumps(src))
elif query!="" and src=="":
    st = '{{"query": {{"bool": {{"must": [{{"multi_match": {{"query": {}, "fields": ["textBody", "title"]}}}}],"filter": []}}}}}}'.format(json.dumps(query))
elif query=="" and src!="":
    st = '{{"query": {{"bool": {{"filter": [{{"match": {{"source": {}}}}}]}}}}}}'.format(json.dumps(src))
else:
    st = '{{"query": {{"bool": {{"must": [],"filter": []}}}}}}'
st = re.sub('"', '\\"', st)
#Надсилаємо запит до Elasticsearch з проханням знайти новини
response = subprocess.run('curl -X GET\"http://localhost:9200/_all/_search?pretty=true&size=100\" -H\"Content-Type: application/json\" -d ' + f'"{st}"', capture_output=True, shell=True)
#Декодуємо вiдповiдь для подальшої роботи з нею
filtered_data = response.stdout.decode('utf-8')
#Форматування вiдповiдi вiд Elasticsearch
json =filtered_data.split('\n')
t=""
for i in range(len(json)):
    t=t+" "+json[i]
t=re.sub('^\s','',t)
total = re.findall('\"took\" : (\d+),', t)
title = re.findall('"title" : "(.*?)",', t)
text = re.findall('"textBody" : "(.*?)",', t)
url = re.findall('"URL" : "(.*?)"', t)
#Формуємо вивiд знайдених новин на сторiнку
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print('<meta http-equiv="Content-Type" charset=utf-8" />')
print("</head>")
print ("<body bgcolor=#66ff99>")
print ("<b>Found: "+str(len(title))+"</b><hr><ol>")
for i in range(len(title)):
    doc_ind=i+1
    print ("<li><b>"+": "+title[i]+"</b>")
    print ("<br>"+text[i])
    print ("<br><i>"+url[i]+"</i><br /><hr>")
print ("</ol></body></html>")