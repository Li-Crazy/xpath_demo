'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/4/12 21:54
@Software: PyCharm
@File    : demo2.py
'''
from lxml import etree
text = """
<table class="tablelist" cellpadding="0" cellspacing="0">
		    	<tbody><tr class="h">
		    		<td class="l" width="374">职位名称</td>
		    		<td>职位类别</td>
		    		<td>人数</td>
		    		<td>地点</td>
		    		<td>发布时间</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49408&amp;keywords=&amp;tid=87&amp;lid=0">24012-游戏社交Android高级开发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-04-13</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49406&amp;keywords=&amp;tid=87&amp;lid=0">24012-游戏社交高级后台开发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-04-13</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49407&amp;keywords=&amp;tid=87&amp;lid=0">24012-游戏社交IOS高级开发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-04-13</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49396&amp;keywords=&amp;tid=87&amp;lid=0">GY0-【国际业务部】推荐算法资深工程师(深圳) </a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-04-13</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49392&amp;keywords=&amp;tid=87&amp;lid=0">22989-大数据及人工智能web前端开发</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-04-13</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49393&amp;keywords=&amp;tid=87&amp;lid=0">22989-大数据及人工智能web前端开发</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-04-13</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49394&amp;keywords=&amp;tid=87&amp;lid=0">29777-腾讯云工业行业方案架构师（深圳）</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-04-13</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49388&amp;keywords=&amp;tid=87&amp;lid=0">GY0-【国际业务部】iOS客户端开发工程师(深圳)</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-04-13</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49389&amp;keywords=&amp;tid=87&amp;lid=0">22989-腾讯云SDN控制器开发工程师</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-04-13</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=49385&amp;keywords=&amp;tid=87&amp;lid=0">CSIG15-智能平台部NLP算法高级工程师(北京)</a></td>
					<td>技术类</td>
					<td>3</td>
					<td>北京</td>
					<td>2019-04-13</td>
		    	</tr>
		    			    	<tr class="f">
		    		<td colspan="5">
		    			<div class="left">共<span class="lightblue total">1520</span>个职位</div>
		    			<div class="right"><div class="pagenav"><a href="javascript:;" class="noactive" id="prev">上一页</a><a class="active" href="javascript:;">1</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=10#a">2</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=20#a">3</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=30#a">4</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=40#a">5</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=50#a">6</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=60#a">7</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=70#a">...</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=1510#a">152</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=10#a" id="next">下一页</a><div class="clr"></div></div></div>
		    			<div class="clr"></div>
		    		</td>
		    	</tr>
		    </tbody></table>
"""
#使用lxml解析HTML代码，自动补全
def parse_text():
    htmlElement = etree.HTML(text)#htmlElement并不是字符串，而是一个对象
    print(type(htmlElement))
    print(etree.tostring(htmlElement,encoding='utf-8').decode('utf-8'))#转换成html代码

#只解析HTML代码
def parse_text_file():
    htmlElement = etree.parse("text.html")#默认XML解析器
    print(etree.tostring(htmlElement,encoding='utf-8').decode('utf-8'))#转换成html代码

def parse_lagou_file():
    parser = etree.HTMLParser(encoding='utf-8')#更改HTML解析器,解决不规范的HTML代码的解析问题
    htmlElement = etree.parse("lagou.html",parser=parser)#指定解析器
    print(etree.tostring(htmlElement,encoding='utf-8').decode('utf-8'))#转换成html代码

if __name__ == '__main__':
    parse_text()
    parse_text_file()
    parse_lagou_file()