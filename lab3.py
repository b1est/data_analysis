from lab1 import *
from itertools import groupby
from datetime import datetime
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
        tim = now.strftime("%Y-%m-%dT%H:%M")
        with open('elinput.sh', 'a+', encoding='utf-8') as f:
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
    print('Convert: Done!')
    # os.system('sudo chmod u+x elinput.sh')
    os.system('chmod u+x elinput.sh')
    os.system('./elinput.sh')
    os.system('rm *.sh')

    if __name__ == '__main__':
        convert_to_json_edit()
        
        