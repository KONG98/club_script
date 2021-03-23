from urllib import request
import chardet
import ssl
import json
from bs4 import BeautifulSoup
import re
import time
url = "https://www.solidot.org/"

#得到htlm
def gethtlm(scr):
    response = request.urlopen(scr)
    html = response.read()
    charset = chardet.detect(html)# {'language': '', 'encoding': 'utf-8', 'confidence': 0.99}
    html = html.decode(str(charset["encoding"]))  # 解码
    return html


def parse(html):
    soup = BeautifulSoup(html,'html.parser')
    news = soup.select('.block_m')
    for new in news:
        title = new.select('a')[0].string
        scr=url+new.select('a')[0]['href']
        if len(title)<6:
            title+=':'+new.select('a')[1].string
            scr=url+new.select('a')[1]['href']
        contentPlant = str(new.select('.p_mainnew')[0])
        contentMid=re.sub('<[\\s\\S]*?>','',contentPlant)
        content=contentMid.strip().split('。')[0]
        time=gettime(scr)
        image = None
        dict = {'title':title,'date':time,'source':scr,'brief': content,'image':image }
        print(dict)

def gettime(scr):
    html=gethtlm(scr)
    soup = BeautifulSoup(html,'html.parser')
    news = json.loads(soup.find('script',{'type': 'application/ld+json'}).get_text())["pubDate"]
    return news

if __name__ == "__main__":
    ssl._create_default_https_context = ssl._create_unverified_context
    obj = gethtlm(url)
    content = parse(obj)
    while True:
        time.sleep(24*3600)
        ssl._create_default_https_context = ssl._create_unverified_context
        obj = gethtlm(url)
        content = parse(obj)



