# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from lxml import etree
import pandas as pd
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive",
    "Host": "www.tripadvisor.cn",
#www.meituan.com
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:55.0) Gecko/20100101 Firefox/55.0"
}
# place=['yueliangshan','yulonghe','shiwaitaoyuan','darongshu','xingpingguzhen','jiumahuashan','yangshuohudiequan','tutenggudao','julongtan','yangdi','yulongqiao','yangshuogongyuan','yulonghepiaoliuchaoyangmatou','yulonghepiaoliujinlongqiaomatou','wenhuagujishanshuiyuan','yangshuolongjinghepiaoliu','lishuiguyue','gongnongqiao','tianlaihudiequan','jiumahuashanxiagupiaoliu','fuliqiao','yulonghepiaoliuyulongqiaoxinzhaimatou']
place=[["d548919","Yangshuo_Park-Yangshuo"],["d1834698","West_Street-Yangshuo"],["d1771883","Yulong_River-Yangshuo"],
       ["d1834787","Guilin_Laozhai_Mountain-Yangshuo"],["d1741379","Impression_Sanjie_Liu_Evening_Showtime-Yangshuo"],
       ["d1834822","Guilin_Butterfly_Spring-Yangshuo"],["d548007","Moon_Hill-Yangshuo"],["d1770110","Bamboo_Rafting-Yangshuo"],
       ["d2315352","Xing_Ping-Yangshuo"],["d1856461","Yangshuo_Historic_Landscape_Park-Yangshuo"],
       ["d1834071","Julong_Lake_of_Yangshuo-Yangshuo"],["d503004","Tall_Banyan-Yangshuo"],["d550278","Shiwai_Taoyuan-Yangshuo"],["d1834789","Longjin_Rafting-Yangshuo"],
       ['d1834824',"Yangti_Dyke-Yangshuo"],["d1834788","Jiuma_Mountain-Yangshuo"],
       ["d1834208","Totem_Ancient_Trail-Yangshuo"],['d1491908',"The_Assembled_Dragon_Cave-Yangshuo"],["d1833817","Yulong_Bridge-Yangshuo"]]
a=[x[0] for x in place]
b=[x[1] for x in place]
for name in range(len(place)):
    n=[]
    t=[]
    s=[]
    # for i in range(0,1500,15):
    url1="https://www.tripadvisor.cn/Attraction_Review-g303712-%s-Reviews-or00-%s_County_Guangxi.html"%(a[name],b[name])
    # url="https://lvyou.baidu.com/xijie/remark/?rn=15&pn=%d&style=hot#remark-container" %i
    print (url1)
    
    # print (i)
    try :
        html1=requests.get(url1,headers=headers)
    except :
        pass
    html1.encoding="utf-8"
    select=etree.HTML(html1.content)
    num=select.xpath("""//*[@id="taplc_location_review_filter_controls_responsive_0_form"]/div[4]/ul/li[3]/label/span/text()""")[0][1:-1]
    for pagnum in range(0, int(num), 10):
        print (b[name])
        url="https://www.tripadvisor.cn/Attraction_Review-g303712-%s-Reviews-or%d-%s_County_Guangxi.html"%(a[name],pagnum,b[name])
        try:
            html = requests.get(url, headers=headers)
        except:
            pass
        html.encoding = "utf-8"
        soup=BeautifulSoup(html.content)
        neirong=soup.find_all(class_="partial_entry")
        title=soup.find_all(class_="noQuotes")
        start=soup.find_all(class_="rating reviewItemInline")
        for j in range(2,len(neirong)):
#            print (title[j-2].text)
            t.append(title[j-2].text)
            n.append(neirong[j].text)
            s.append(start[j-2].span["class"][1][7:])
    info = {}
    info['neirong'] = n
    info['title'] =t
    info["start"]=s
    print(len(n),len(t),len(s))
    names = ['评论内容','评论题目','星级']
    print(info)
    df = pd.DataFrame(info)
    df.to_csv(r"C:\Users\Administrator\Desktop\%s.csv" %b[name], index=False, sep=',',encoding='utf-8')
#df.to_csv("/Users/pluto/Desktop/price.csv",encoding='gbk');
#df  = pd.DataFrame([userId,comment,commentTime,star,picUrls],index=['用户ID','评论内容','评论时间','评分','图片'])

#    file=open(r"C:\Users\Administrator\Desktop\%s.txt" %b[name],"w",encoding='utf-8')
#    for i in range(len(t)):
#        file.write(str(t[i])+"\n")
#        file.write(str(n[i])+"\n")
#        file.write(str(s[i])+"\n")
#    file.close()
