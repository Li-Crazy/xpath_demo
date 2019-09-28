'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/4/12 21:54
@Software: PyCharm
@File    : demo2.py
'''
from lxml import etree

parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse('text.html',parser=parser)
# 1.获取所有tr标签
#//tr
#xpath函数返回的是一个列表
trs = html.xpath("//tr")
for tr in trs:
    print(tr)
    print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))

# 2.获取第二个tr标签
tr2 = html.xpath("//tr[2]")[0]#取出列表中的第一个元素
print(etree.tostring(tr2,encoding='utf-8').decode('utf-8'))

# 3.获取所有class=even的tr标签
trs = html.xpath("//tr[@class='even']")
for tr in trs:
    print(tr)
    print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))

# 4.获取所有a标签的href属性
aList = html.xpath("//a/@href")
for a in aList:
    print("http://hr.tencent.com/"+a)

# 5.获取所有职位信息（纯文本）
trs = html.xpath("//tr[position()>1]")#获取除第一个tr标签之外的tr标签
positions = []
for tr in trs:
    # print(tr)
    # print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))
    href = tr.xpath(".//a/@href")[0]#.//a在当前tr标签下获取，//a忽视当前标签，查找全部
    fullurl = "http://hr.tencent.com/" + href
    # title = tr.xpath(".//a/text()")[0]#text()获取标签后面的文本
    title = tr.xpath("./td[1]//text()")[0]
    category = tr.xpath("./td[2]//text()")
    nums = tr.xpath("./td[3]//text()")
    adress = tr.xpath("./td[4]//text()")
    pubtime = tr.xpath("./td[5]//text()")

    position = {
        'url': fullurl,
        'title': title,
        'category': category,
        'nums': nums,
        'adress':adress,
        'time':pubtime
    }
    positions.append(position)
print(positions)