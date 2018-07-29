# -*- coding: utf-8 -*-
import requests
from lxml import etree
import random
import time
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request
from fake_useragent import UserAgent
ua = UserAgent()
#ie浏览器的user agent
headers = {
        'User-Agent': ua.random,
        'Cookie':'cy=25; cye=tangshan; _lxsdk_cuid=1649144034fc8-047dfb5f06892d-16386952-13c680-1649144034f8f; _lxsdk=1649144034fc8-047dfb5f06892d-16386952-13c680-1649144034f8f; _hc.v=f643750e-028d-6e11-ed82-3806b0655e90.1531445511; dper=e227a513bb722dad9de2c87d596c813c651809ba085c9b43dc688501a92a93bbb66f22cdd52d2c92481dff623ae10a863bfa16e03a628837a53c958e6f14856cba59f6843174efa7b0118bc29d462b0a8f6418cdf6691f39e3ff7f6e392a78b3; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_2166800587; ctu=2dc6bd505210f4b26bbf0e102fce3b85025084dfe5472fdf113e911496830c79; uamo=15018326478; s_ViewType=10; JSESSIONID=DE23CC05252F3A913A753CC24E928290; Hm_lvt_185e211f4a5af52aaffe6d9c1a2737f4=1531445628; Hm_lpvt_185e211f4a5af52aaffe6d9c1a2737f4=1531445628; _lxsdk_s=16491440354-265-bde-c7f%7C%7C28',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Host':'www.dianping.com'
    }
urls=["http://www.dianping.com/shop/1917562",
"http://www.dianping.com/shop/3154648",
"http://www.dianping.com/shop/61433764",
"http://www.dianping.com/shop/2110222",
"http://www.dianping.com/shop/13884810",
"http://www.dianping.com/shop/67895574",
"http://www.dianping.com/shop/4671241",
"http://www.dianping.com/shop/69267654",
"http://www.dianping.com/shop/2682973",
"http://www.dianping.com/shop/18142169",
"http://www.dianping.com/shop/57841857",
"http://www.dianping.com/shop/2561284",
"http://www.dianping.com/shop/5204814",
"http://www.dianping.com/shop/3905491",
"http://www.dianping.com/shop/3167527",
"http://www.dianping.com/shop/2560327",
"http://www.dianping.com/shop/60334485",
"http://www.dianping.com/shop/32410537",
"http://www.dianping.com/shop/14701709",
"http://www.dianping.com/shop/61511940",
"http://www.dianping.com/shop/6114028",
"http://www.dianping.com/shop/58854190",
"http://www.dianping.com/shop/9313867",
"http://www.dianping.com/shop/58847517"]
#
#def get_ip_list(obj):
#    ip_text = obj.findAll('tr', {'class': 'odd'})   # 获取带有IP地址的表格的所有行
#    ip_list = []
#    for i in range(len(ip_text)):
#        ip_tag = ip_text[i].findAll('td')   
#        ip_port = ip_tag[1].get_text() + ':' + ip_tag[2].get_text() # 提取出IP地址和端口号
#        ip_list.append(ip_port)
#    print("共收集到了{}个代理IP".format(len(ip_list)))
#    print(ip_list)
#    return ip_list
#def valVer(proxys):
#    badNum = 0
#    goodNum = 0
#    good=[]
#    for proxy in proxys:
#        try:
#            proxy_host = proxy
#            protocol = 'https' if 'https' in proxy_host else 'http'
#            proxies = {protocol: proxy_host}
#            response = requests.get('http://www.baidu.com', proxies=proxies, timeout=2)
#            if response.status_code != 200:
#                badNum += 1
#                print (proxy_host, 'bad proxy')
#            else:
#                goodNum += 1
#                good.append(proxies)
#                print (proxy_host, 'success proxy')
#        except Exception as e:
#            print( e)
#            # print proxy_host, 'bad proxy'
#            badNum += 1
#            continue
#    print ('success proxy num : ', goodNum)
#    print( 'bad proxy num : ', badNum)
#    return good
#
#url = 'http://www.xicidaili.com/'
#headers = {
#    'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
#request = Request(url, headers=headers)
#response = urlopen(request)
#bsObj = BeautifulSoup(response, 'lxml')     # 解析获取到的html
#lists=get_ip_list(bsObj)
#go=valVer(lists)
#print ("一共多少个ip",len(go))
p=[]
s=[]
t=[]
n=[]
l=[]
for u in urls:
    for j in range(100):
        url="%s/review_all/p%d"%(u,j)
        response=requests.get(url,headers=headers,proxies=random.choice(go))
        selector=etree.HTML(response.text)
        print (111)
        ramnum = random.randint(1,10)
        time.sleep(3+ramnum)
        print (222)
        for i in range(20):
            pinglun=selector.xpath("""//*[@id="review-list"]/div[2]/div[1]/div[3]/div[3]/ul/li[%d]/div/div[3]/text()"""%i)
            score=selector.xpath("""//*[@id="review-list"]/div[2]/div[1]/div[3]/div[3]/ul/li[%d]/div/div[2]/span/@class"""%i)
            time=selector.xpath("""//*[@id="review-list"]/div[2]/div[1]/div[3]/div[3]/ul/li[%d]/div/div[6]/span[1]/text()"""%i)
            name=selector.xpath("""//*[@id="review-list"]/div[2]/div[1]/div[3]/div[3]/ul/li[%d]/div/div[1]/a/text()"""%i)
#            try:
#                href=selector.xpath("""//*[@id="review-list"]/div[2]/div[1]/div[3]/div[3]/ul/li[%d]/div/div[1]/a/@href"""%i)
#                href=os.path.join("http://www.dianping.com/",href[0][1:])
#                localresponse=requests.get(href,headers=headers)
#                localselector=etree.HTML(localresponse.text)
#                local=localselector.xpath("""/html/body/div[2]/div[1]/div/div/div/div[2]/div[2]/span[2]""")
#                l.append(local)
#            except IndexError:
#                pass
            p.append(pinglun)
            s.append(score)
            t.append(time)
            n.append(name)
            print ("pinglun,score,time,name",pinglun,score,time,name)
    info = {}
    info['comment'] = p
    info["name"]=n
    info["score"]=s
    info["time"]=t
#    info["local"]=l

    print(info)
    df = pd.DataFrame(info)
    df.to_csv(r"C:\Users\Administrator\Desktop\%s.csv" %u[29:], index=False, sep=',',encoding='utf-8')
    