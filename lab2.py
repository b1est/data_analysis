import re
import subprocess
from lab1 import rss, os
import subprocess
from itertools import groupby
from datetime import datetime, timedelta

def convert_to_json():
    term = subprocess.check_output('dir').decode('utf-8').split('\n')
    for line in term:
        if 'rss.json' in line:
            rssexist = True
            break
        else:
            rssexist = False
    if rssexist:
        f = open(f'rss.json', 'r', encoding = 'utf-8')
        t = f.read()
        f.close()
        f = open(f'rss.json', 'w')
        f.close()
        f = open(f'rss.json', 'w', encoding = 'utf-8')
        f.write(t[:-2])
        f.close()
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
            source = re.sub('"', '\"', source)
            text = re.findall('<description>(.*?)<\/description>', t)
            link = re.findall('<link>(.+?)<\/link>', t)
            now = datetime.now()
            tim = now.strftime("%Y-%m-%dT%H:%M")
            with open('rss.json', 'a+', encoding='utf-8') as f:
                f.write('\n,\n')
                for i in range(1, len(title)):
                    
                    f.write("{\n\"title\":\""+title[i]+"\",\n")
                    text[i] = re.sub('[\s\-]*$', '', text[i])
                    text[i] = re.sub('"', '\"', text[i])
                    text[i] = re.sub('\'', '&amp;', text[i])
                    f.write("\"textBody\":\""+text[i]+"\",\n")
                    f.write("\"source\":\""+source+"\",\n")
                    f.write("\"PubDate\":\""+tim+"\",\n")
                    f.write("\"URL\":\""+link[i]+"\"\n}")
                    if i < len(title)-1:
                        f.write("\n,\n")                  
                if list(rss.keys())[-1] == filename:
                    f.write("\n]\n")  
    else:   
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
            source = re.sub(' &gt; ', '', title[0])
            source = re.sub('[\s\-]*$', '', source)
            source = re.sub('"', '\"', source)
            text = re.findall('<description>(.*?)<\/description>', t)
            link = re.findall('<link>(.+?)<\/link>', t)
            now = datetime.now()
            tim = now.strftime("%Y-%m-%dT%H:%M")
            with open('rss.json', 'a+', encoding='utf-8') as f:
                if filename == list(rss.keys())[0]:
                    f.write('[\n')
                else:
                    f.write(',\n')
                for i in range(1, len(title)):
                    f.write("{\n\"title\":\""+title[i]+"\",\n")
                    text[i] = re.sub('[\s\-]*$', '', text[i])
                    text[i] = re.sub('"', '\"', text[i])
                    text[i] = re.sub('\'', '&amp;', text[i])
                    f.write("\"textBody\":\""+text[i]+"\",\n")
                    f.write("\"source\":\""+source+"\",\n")
                    f.write("\"PubDate\":\""+tim+"\",\n")
                    f.write("\"URL\":\""+link[i]+"\"\n}")
                    if i < len(title)-1:
                        f.write("\n,\n")             
                if list(rss.keys())[-1] == filename:
                    f.write("\n]\n")
    os.system('rm *.xml')
    print('Convert: Done!')

    if __name__ == '__main__':
        convert_to_json()