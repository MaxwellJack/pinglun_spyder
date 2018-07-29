# -*- coding: utf-8 -*-
import re
import requests
import sys

import urllib
url="http://www.lvmama.com/lvyou/home/ajaxGetCommentPage?page=3&list_type=CommentBestNew&type=N&dest_id=104986"
url="http://www.lvmama.com/lvyou/ajax/ajaxGetComDataNew?d_id=100144"
# 设置编码
html=requests.get(url)
print (html.encoding)
for i in html.content:
    print (i)

# # 获得系统编码格式
# type = sys.getfilesystemencoding()
# r = urllib.urlopen("http://www.baidu.com")
# # 将网页以utf-8格式解析然后转换为系统默认格式
# a = r.read().decode('utf-8').encode(type)
