import requests
import os

# import socks
# import socket
# socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 1080)
# socket.socket = socks.socksocket

pxs={'http':'socks5://127.0.0.1:1080','https':'socks5://127.0.0.1.1080'}
# url='https://item.jd.com/100002534951.html#crumb-wrap'
# url='https://www.amazon.cn/dp/B07S264ZB6?ref_=Oct_DotdV2_PC_4_GS_DOTD_2b783bfd&pf_rd_r=BVQB1BM54MFTX1DMNXGH&pf_rd_p=a91e91fd-4186-4d50-bbac-2a27a7729f0f&pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-2'
# url='http://www.baidu.com/s'
url='https://pics.javbus.com/cover/7jz2_b.jpg'
parent=r'E:\temp\javbus\\'
path=parent+url.split('/')[-1]
headers={'user-agent':'Mozilla/5.0'}

print(path)

def mkdir(path):
    dir=os.path.exists(path)
    if not dir:
        os.makedirs(path)
    else:
        print('文件夹已存在')

try:
    mkdir(parent)
    r=requests.get(url,headers=headers)
    print(r.status_code)
    with open(path,'wb') as f:
        f.write(r.content)
        f.close()
        print("文件写入完成，已关闭")
    
except BaseException as e:
    print('爬取失败')
    print(e)



    