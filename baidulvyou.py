import requests
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
place=['yueliangshan','yulonghe','shiwaitaoyuan','darongshu','xingpingguzhen','jiumahuashan','yangshuohudiequan','tutenggudao','julongtan','yangdi','yulongqiao','yangshuogongyuan','yulonghepiaoliuchaoyangmatou','yulonghepiaoliujinlongqiaomatou','wenhuagujishanshuiyuan','yangshuolongjinghepiaoliu','lishuiguyue','gongnongqiao','tianlaihudiequan','jiumahuashanxiagupiaoliu','fuliqiao','yulonghepiaoliuyulongqiaoxinzhaimatou']
for name in place:
    s=[]
    score=[]
    for i in range(0,1500,15):
        url="https://lvyou.baidu.com/%s/remark/?rn=15&pn=%d&style=hot#remark-container" %(name,i)
        # url="https://lvyou.baidu.com/xijie/remark/?rn=15&pn=%d&style=hot#remark-container" %i
        print ("url=",url)
        print ('i=',i)
        try :
            html=requests.get(url,headers=headers)
        except :
            pass
        else:
            print ("html=",html)
            if str(html)=="<Response [200]>":
                # print (html)
                html.encoding="utf-8"
                selecter=etree.HTML(html.text)
                # pinglun=selecter.xpath("""normalize-space(//*[@id="remark-container"]/div[3]/div/div[2]/div[2]/div[1]/text())""")
                # etree.tostring(pinglun[0],print_pretty=True, method='html')
                for j in range(1,16):
                    numsum=selecter.xpath("""//*[@id="remark-container"]/div[1]/span/text()""")
                    print (numsum)
                    p=selecter.xpath("""//*[@id="remark-container"]/div[3]/div[%d]/div[2]/div[2]/div[1]/node()"""%j)
                    try :
                        c=selecter.xpath("""//*[@id="remark-container"]/div[3]/div[%d]/div[2]/div[1]/div[1]/div/@class"""%j)
                        print (c)
                        c=c[0][-1]
                    except IndexError:
                        pass
                    # print (j)
                    st=""
                    for i in p:
                        # print ("p=",p)
                        if type(i)==lxml.etree._Element:
                            i=i.text
                        try:
                            st=st+i
                        except TypeError:
                            pass
                    s.append(st)
                    score.append(c)
                    print ("st=",st)

            else:
                print ("url is unable")
                pass
        while '' in s:
            s.remove('')
        # print(s)
    info = {}
    info['pinglun'] = s
    info["start"]=score[:len(s)]
    print(info)
    df = pd.DataFrame(info)
    df.to_csv(r"C:\Users\Administrator\Desktop\%s.csv" %name, index=False, sep=',',encoding='utf-8')

    # file=open(r"C:\Users\Administrator\Desktop\%s.txt" %name,"w",encoding='utf-8')
    # for i in s:
    #     y=1
    #     file.write(i+"\n")
    #     y=y+1
    # file.close()