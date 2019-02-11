
import requests
import time
import sys,io
import csv
from lxml import etree
import random
import re
#伪装浏览器
headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}
#代理ip网站
ip_url = 'http://www.xicidaili.com/nn/'
#获取ip数据
ip_data = requests.get(ip_url,headers=headers).text
#解析网页
r = etree.HTML(ip_data)
#lxml获取相对应的xpath
ip = r.xpath('//*[@id="ip_list"]/tr/td[2]/text()')
			#//*[@id="ip_list"]/tbody/tr[4]/td[2]
#建立一个空ip列表用来存储获得的ip
ip_list=[]

#测试ip是否可用
for ips in ip:
	try:
		proxy = {'http':ips}
		#循环列表的ip信息，向百度请求响应
		text_url = 'https://www.baidu.com/'
		#响应时间timeout=1，即在1秒内，未送到响应就断开连接
		res = requests.get(url=text_url,proxies=proxy,headers=headers,timeout=1)
		#将可用ip添加到ip列表ips_list中
		ip_list.append(ips)
	except Exception as e:
		print(e)
#在ip列表中随机选择ip
proxies = {'http':random.choice(ip_list)}
#将文件写入桌面文件doubanMovie中
with open(r'C:/Users/AOAO/Desktop/dy2018(regex).csv','w') as f:
	#写入csv文件
	writer = csv.writer(f)
	#第一行内容
	writer.writerow(('链接','标题'))
	#循环所有页面
	for i in range(1,303):
		#如果i为1，则url为https://www.dy2018.com/html/gndy/dyzz/index.html
		if i==1:
			url = 'https://www.dy2018.com/html/gndy/dyzz/index.html'
		#如果i不等于1，则url为https://www.dy2018.com/html/gndy/dyzz/index_{}.html'.format(i)
		else:
			url = 'https://www.dy2018.com/html/gndy/dyzz/index_{}.html'.format(i)
		print('正在抓取第{}页'.format(i))
		print(url)
		#获取网页内容
		data = requests.get(url,headers=headers,proxies=proxies).content.decode(encoding="gbk", errors="ignore")
		#print(data)
		#用正则表达式获取链接和标题，并将正则字符串编译成正则表达式对象
		pattern = re.compile('<table.*?tbspan.*?href="(.*?)".*?title="(.*?)".*?</table>',re.S)
		#搜索字符串，以列表形式返回全部能匹配的子串。
		results =re.findall(pattern, data) 
		# print(results)
		#等待一秒，防止爬虫过快
		time.sleep(1)
		#设置过滤关键词
		keyword = ['国产']
		#循环整个results，将列表数据单独取出
		for result in results:
			#为url和name赋值
			url,name = result
			#如果不含有关键词“国产”，则写入数据
			if all(string not in name for string in keyword) :
				# print(url,name)
				#写入数据
				f.write("{},{}\n".format('https://www.dy2018.com'+url,name))