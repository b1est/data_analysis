import sys
import re
import csv

def agregation_console_edition():
    t = sys.stdin.read() 
    
    json =t.split('\n') 
    t="" 
    for i in range(len(json)): 
        t=t+" "+json[i]
    t=re.sub('^\s','',t) 
    days = re.findall('"key_as_string" : "(.+?)T', t) 
    count = re.findall('"doc_count" : (\d+)', t)
    with open('rss.csv', 'w') as f:
        for i in range(len(days)): 
            f.write(days[i]+";"+count[i]+"; \n")

def agregation_file_edition():
    f = open('agregation.json', 'r')
    t = f.read()
    f.close()
    json =t.split('\n') 
    t="" 
    for i in range(len(json)): 
        t=t+" "+json[i]
    t=re.sub('^\s','',t) 
    days = re.findall('"key_as_string" : "(.+?)T', t) 
    count = re.findall('"doc_count" : (\d+)', t)
    with open('rss.csv', 'w') as f:
        
        for i in range(len(days)): 
            f.write(days[i]+";"+count[i]+"; \n")

if __name__ == "__main__":
    agregation_file_edition()