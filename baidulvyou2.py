import requests
from bs4 import  BeautifulSoup
from lxml import etree
import lxml
import pandas as pd
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive",
    "Host": "lvyou.baidu.com",
#www.meituan.com
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:55.0) Gecko/20100101 Firefox/55.0"
}
# url="https://lvyou.baidu.com/user/ajax/remark/getsceneremarklist?xid=8a34b2cc70c0c1ecdeb82ff8&score=0&pn=15&rn=15&style=hot&format=ajax&flag=1&t=1531294277664"
url="https://lvyou.baidu.com/yinxiangliusanjie/remark/?rn=15&pn=15&style=hot#remark-container"

html=requests.get(url)
html.encoding="utf-8"
selecter=etree.HTML(html.text)
numsum=selecter.xpath("""//*[@id="remark-container"]/div[2]/div[2]/a[1]/span/text()""")[0][1:-1]
time=selecter.xpath("""//*[@id="remark-container"]/div[3]/div[1]/div[2]/div[1]/div[2]/text()""")
print ("numsum=",numsum)
print ("time=",time)
