import requests
from bs4 import BeautifulSoup
import time
import random
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
num= 0 #初始化参数
for a in range(10): # 循环10个页面
	url = 'https://movie.douban.com/top250?start={}'.format(a*25) #爬取网页链接，以25个单位为一个页面
	html = requests.get(url,headers=headers,proxies=proxies).text #导入网页
	soup = BeautifulSoup(html,"html.parser") #解析网页parser方法
	ollist = soup.find('ol',attrs={'class':'grid_view'}) #找到class标签下的grid_view元素
	img = ollist.find_all('img') # 寻找img标签
	print(proxies)
	time.sleep(3) # 延迟3秒启动，防止爬虫被封
	# print(img)
	 
	for link in img: #循环图片地址
		cover = link.get('src') # 获取图片
		num = num+1 # 参数加一
		time.sleep(3) #延迟3秒启动，防止爬虫被封
		# print(cover)
		print(cover) #测试
		with open ('C:/Users/AOAO/Desktop/doubanMovie1/'+str(num)+'.jpg','wb') as f:
			# 保存到文件夹中，需要提前建立文件夹否则报错
			pictures= requests.get(cover).content
			# 取得图片
			f.write(pictures)
			#保存图片