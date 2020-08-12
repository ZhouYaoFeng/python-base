import requests

# import socks
# import socket
# socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 1080)
# socket.socket = socks.socksocket

pxs={'http':'socks5://127.0.0.1:1080','https':'socks5://127.0.0.1.1080'}
# url='https://item.jd.com/100002534951.html#crumb-wrap'
# url='https://www.amazon.cn/dp/B07S264ZB6?ref_=Oct_DotdV2_PC_4_GS_DOTD_2b783bfd&pf_rd_r=BVQB1BM54MFTX1DMNXGH&pf_rd_p=a91e91fd-4186-4d50-bbac-2a27a7729f0f&pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-2'
url='http://www.baidu.com/s'
headers={'user-agent':'Mozilla/5.0'}
params={'wd':'Python'}
try:
    r=requests.get(url,headers=headers,params=params)
    print(r.request.headers)
    print(r.request.url)
    print(r.status_code)
    print(len(r.text))
    r.encoding=r.apparent_encoding
    print(r.text)
except:
    print('爬取失败')