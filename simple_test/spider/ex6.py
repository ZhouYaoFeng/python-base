import re
import requests
import os
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    headers={'user-agent':'Mozilla/5.0'}
    try:
        r=requests.get(url,headers=headers)
        r.raise_for_status
        r.encoding=r.apparent_encoding
    except BaseException as e:
        print(e)
        return ""
    return r.text

def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[3].string])

def printUnivList(ulist,num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名","学校","分数"))
    for i in range(20):
        u=ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))
    # print(ulist)

def main():
    uinfo=[]
    url='http://www.zuihaodaxue.com/Greater_China_Ranking2019_0.html'
    html=getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)

main()
