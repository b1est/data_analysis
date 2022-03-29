import os

rss = {
'skynews': 'https://feeds.skynews.com/feeds/rss/technology.xml',
'nytimestech': 'https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/technology/rss.xml',
'nytimesscience': 'https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/science/rss.xml'
}


def download():
    files = ''
    for k in rss.keys():
        files += f'{k}.xml '
    for k in rss.keys():
        os.system(f'wget -O {k}.xml {rss[k]}')

if __name__ == '__main__':
    download()
