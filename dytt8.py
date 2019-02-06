
import requests
import time
import sys,io
import csv
import random
from lxml import etree
import codecs

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
with open(r'C:/Users/AOAO/Desktop/dy2018.csv','w') as f:
	#写入csv文件
	writer = csv.writer(f)
	#第一行内容
	writer.writerow(('标题'))
	for i in range(1,189):
		url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'.format(i)
		print(url)
		data = requests.get(url,headers=headers,proxies=proxies).content.decode(encoding="gbk", errors="ignore")
		s = etree.HTML(data) 
		movie = s.xpath("//table[@class='tbspan']//a/text()")
		time.sleep(1)
		for name in movie:
			print(name)
			f.write("{}\n".format(name))
