import requests
from bs4 import BeautifulSoup
import time
import random
import csv
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
ip_url = 'http://www.xicidaili.com/nn/'
#导入网页
ip_html = requests.get(ip_url,headers=headers).text
#解析网页，parser方法
soup = BeautifulSoup(ip_html,"html.parser")
#查找tr便签下的odd元素
trs = soup.find_all('tr',attrs={'class':'odd'})
#列表用来存储ip
ip_list=[]
#循环trs，1表示从第几位开始截取
for i in range(1,len(trs)):
	#将所有元素分成单独的列表
	ip_info=trs[i]
	#找到ip_info里面的td标签
	tds = ip_info.find_all('td')
	#取得标签的第2个文本（即ip）
	ip = tds[1].text
	#将ip添加到列表中
	ip_list.append(ip)
"""
这里不用
trs = soup.find_all('tr',attrs={'class':'odd'}
tds= trs.find_all('td')
for i in tds:
	ip= tds[1].text
是因为在这里tds里面的所有信息为一个列表，
此时ip= tds[1].text能获取到的只是列表中的第一个ip
所以，要用ip_info=trs[i]来将每个tr的内容独立成一个列表
再从tr里面寻找td，获取每个ip
"""
#验证ip是否可拥
for ips in ip_list:
	try:
		proxy = {'http':ips}
		#用来测试ip的网站
		text_url = 'https://www.baidu.com/'
		#用ip访问网站，时间超过一秒则断开
		res = requests.get(url=text_url,proxies=proxy,headers=headers,timeout=1)
	except Exception as e:
		#将时间超过一秒的ip移出列表
		ip_list.remove(ips)
#随机选择一个ip
proxies={'http':random.choice(ip_list)}
with open (r'C:/Users/AOAO/Desktop/dooubanMovie1.csv','w') as f:
	#保存文件
	writer = csv.writer(f) 
	#写入文件
	writer.writerow(('片名','链接'))
	for i in range(1,10):
		#如果i为1，则url为https://www.dy2018.com/html/gndy/dyzz/index.html
		if i==1:
			url = 'https://www.dy2018.com/html/gndy/dyzz/index.html'
		#如果i不等于1，则url为https://www.dy2018.com/html/gndy/dyzz/index_{}.html'.format(i)
		else:
			url = 'https://www.dy2018.com/html/gndy/dyzz/index_{}.html'.format(i)
		html = requests.get(url,headers=headers,proxies=proxies).content.decode(encoding="gbk", errors="ignore")
		soup = BeautifulSoup(html,"lxml") #解析网页parser方法
		print(url)
		tables = soup.find_all('table', class_='tbspan')
		time.sleep(1) 
		for table in tables:
			a = table.find('a')
			# name = table.find('a').getText()
			name = a.text
			url = 'https://www.dy2018.com'+a['href']
			# print(url,name)
			keyword = ['国产']
			if all(string not in name for string in keyword) :
				f.write("{},{}\n".format(name,url))


