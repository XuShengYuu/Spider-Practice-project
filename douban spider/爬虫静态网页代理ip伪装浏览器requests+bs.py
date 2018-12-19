import requests
from bs4 import BeautifulSoup
import time
import sys,io 
import csv
import random
#强制改变编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
#伪装浏览器
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
#获取ip网址
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
with open (r'C:/Users/AOAO/Desktop/dooubanMovie1.csv','w',encoding='gb18030') as f:
	#保存文件
	writer = csv.writer(f) 
	#写入文件
	writer.writerow(('片名','评分','评语'))
	#标题

	for i in range(10): #循环10个页面
		url='https://movie.douban.com/top250?start={}'.format(i*25)#爬取url，以25个单位为一个页面
		html=requests.get(url,headers=headers,proxies=proxies).text # 获取网页
		soup=BeautifulSoup(html,"html.parser") # 解析网页parser方法
		ollist = soup.find('ol',attrs={'class':'grid_view'})#找到ol下class标签
		time.sleep(2)#延迟2秒启动，防止爬虫被封
		# print (ollist)
		# print(proxies)测试是否有用随机ip
		for lilits in ollist.find_all('li'):#循环ollist列表，找到li标签
			data = [] #建立列表，保存数据
			hd = lilits.find('div',attrs={'class':'hd'}) #找到div标签下class的属性hd
			name = hd.find('span',attrs={'class':'title'}).getText() #同上
			data.append(name) #将找到的内容添加到列表中
			score = lilits.find('span',attrs={'class':'rating_num'}).getText() #找到span标签下class的属性rating_num
			data.append(score) # 将找到的内容添加到列表中
			comment = lilits.find('span',attrs={'class':'inq'}).getText()
			data.append(comment)
			if len(comment)>0: #判断comment是否存在
				f.write("{},{},{}\n".format(data[0],data[1],data[2]))#存在则打印3个内容
				#print ("{},{},{}\n".format(data[0],data[1],data[2]))
			else: # 不存在则打印两个内容
				f.write("{},{}\n".format(data[0],data[1]))


