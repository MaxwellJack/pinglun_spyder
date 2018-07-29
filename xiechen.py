import requests
from  bs4 import BeautifulSoup
n=[10558831,80969,10758276,80971,101132,84570,10758988,84577,80972,82733,84575,82046,82734,94466,83042,80966,82731,84567,18134138,10547757,18134134,83133,13675908]
place = ['西街', '遇龙河', '《印象刘三姐》山水实景演出', '大榕树', '世外桃源', '十里画廊', '遇龙河漂流', '九马画山', '月亮山', '天籁蝴蝶泉',
         '图腾古道',         '兴坪古镇', '聚龙潭', '工农桥', '黄布倒影', '遇龙桥', '阳朔公园', '富里桥', '漓江竹筏游杨堤段', '龙颈河漂流',
         '漓江竹筏游兴坪段','金水岩', '老寨山']
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive",
    "Host": "you.ctrip.com",
#www.meituan.com
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}
for name in n:
    num=0
    t=[]
    s=[]
    for i in range(1,502):
        url="http://you.ctrip.com/destinationsite/TTDSecond/SharedView/AsynCommentView?poiID=%s&districtId=702&districtEName=Yangshuo&pagenow=%d&order=3.0&star=0.0&tourist=0.0&resourceId=22079&resourcetype=2"%(name,i)
        html=requests.get(url,headers=headers)
        html.encoding="utf-8"
        soup=BeautifulSoup(html.content)
        block=soup.find_all(class_="comment_single")
        for j in block:
            text=j.find(class_="heightbox")
            try :
                start=j.find(class_="sblockline")
                st=start.text
            except AttributeError:
                st=""
            t.append(text.text)
            s.append(st)

    file=open(r"C:\Users\Administrator\Desktop\%s.txt" %place[0],"w",encoding='utf-8')
    num=num+1
    for i in range(len(t)):
        y=1
        file.write(t[i],"\n")
        file.write(s[i],"\n")
        y=y+1
    file.close()
