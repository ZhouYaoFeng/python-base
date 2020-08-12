import requests

ip='115.217.160.148'
url='http://www.ip138.com/iplookup.asp?ip='
headers={'user-agent':'Mozilla/5.0'}
params={'ip':'ip','action':'2'}


try:
    r=requests.get(url+ip,headers=headers)
    print(r.request.headers)
    print(r.request.url)
    print(r.status_code)
    print(len(r.text))
    r.encoding=r.apparent_encoding
    print(r.text)
except:
    print('爬取失败')