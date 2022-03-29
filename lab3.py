from lab1 import *
from itertools import groupby
from datetime import datetime
from dateutil.parser import parse
import re

def convert_to_json_edit():
    for filename in rss.keys():
        f = open(f'{filename}.xml', 'r', encoding = 'utf-8')
        t = f.read()
        f.close()
        _rss = t.split('\n')
        t = ""
        for i in range(len(_rss)):
            t = t+" "+_rss[i]
        t = re.sub('^\s','', t)
        title = re.findall('<title>(.+?)<\/title>', t)
        title = [el for el, _ in groupby(title)]
        source = title[0]
        source = re.sub('[\s\-]*$', '', source)
        source = re.sub('\"', '', source)
        source = re.sub('\'', '', source)
        text = re.findall('<description>(.*?)<\/description>', t)
        link = re.findall('<link>(.+?)<\/link>', t)
        now = datetime.now()
        tim = now.strftime("%Y-%m-%dT%H:%M:00Z")
        with open('rss.sh', 'a+', encoding='utf-8') as f:
            if filename == list(rss.keys())[0]:
                f.write("#! /bin/bash\n")
            for i in range(1, len(title)):
                title[i] = re.sub('\"', '', title[i])
                title[i] = re.sub('\'', '', title[i])
                f.write("curl -XPOST 'http://localhost:9200/test/_doc/' -H 'Content-Type: application/json' -d '\n{\n\"title\":\""+title[i]+"\",\n")
                text[i] = re.sub('[\s\-]*$', '', text[i])
                text[i] = re.sub('\"', '&quot;', text[i])
                text[i] = re.sub('\'', '&amp;', text[i])
                f.write("\"textBody\":\""+text[i]+"\",\n")
                f.write("\"source\":\""+source+"\",\n")
                f.write("\"PubDate\":\""+tim+"\",\n")
                f.write("\"URL\":\""+link[i]+"\"\n}'\n") 
    os.system('rm *.xml')
    os.system('chmod u+x rss.sh')
    os.system('./rss.sh')
    os.system('rm rss.sh')

def convert_to_json_kibana_console_edition():
    
    f = open(f'rss/rss.xml', 'r', encoding = 'utf-8')
    t = f.read()
    f.close()
    _rss = t.split('\n')
    t = ""
    for i in range(len(_rss)):
        t = t+" "+_rss[i]
    t = re.sub('^\s','', t)
    title = re.findall('<title>(.+?)<\/title>', t)
    title = [el for el, _ in groupby(title)]
    
    
    text = re.findall('<description>(.*?)<\/description>', t)
    link = re.findall('<link>(.+?)<\/link>', t)
    dts = re.findall('<pubDate>(.+?)<\/pubDate>', t)
    source = re.findall('<author>(.+?)<\/author>', t)
    
    with open('rss/rss.txt', 'a+', encoding='utf-8') as f:
            
        for i in range(1, len(title)):
            title[i] = re.sub('\"', '', title[i])
            title[i] = re.sub('\'', '', title[i])
            f.write("POST /lab5/_doc/ \n{\n\"title\":\""+title[i]+"\",\n")
            text[i] = re.sub('[\s\-]*$', '', text[i])
            text[i] = re.sub('\"', '&quot;', text[i])
            text[i] = re.sub('\'', '&amp;', text[i])
            f.write("\"textBody\":\""+text[i]+"\",\n")
            source[i] = re.sub('[\s\-]*$', '', source[i])
            source[i] = re.sub('\"', '', source[i])
            source[i] = re.sub('\'', '', source[i])
            f.write("\"source\":\""+source[i]+"\",\n")
            f.write("\"PubDate\":\""+parse(dts[i]).strftime("%Y-%m-%dT%H:%M:00Z")+"\",\n")
            f.write("\"URL\":\""+link[i]+"\"\n}\n")
 
 
 
if __name__ == "__main__":
    convert_to_json_kibana_console_edition()
        