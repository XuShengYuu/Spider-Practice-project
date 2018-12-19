# requests+lxml爬取静态网页并保存为csv文件
# 引入库
import requests
import sys,io 
from lxml import etree
import time
import csv
import random


# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') 
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
# 强制改变输出编码，防止输出时乱码
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
#伪装浏览器,代理网站有反爬虫必须伪装浏览器才能获取ip
ip_url='http://www.xicidaili.com/nn/'#ip获取网站
ip_data=requests.get(ip_url,headers=headers).text
#请求响应网站，必须有headers伪装浏览器，否则无法爬取
r = etree.HTML(ip_data)
#解析网页
ip = r.xpath('//*[@id="ip_list"]/tr/td[2]/text()')
#xpath获取ip路径
ip_list=[]#ip列表，用来存储ip

for ips in ip:#测试ip的网站
	try:
		proxy = {'http':ips}
		text_url = 'https://www.baidu.com/'
		#遍历时，利用访问百度，设定timeout=1,即在1秒内，未送到响应就断开连接
		res = requests.get(url=text_url,proxies=proxy,headers=headers,timeout=1)
		#打印检测信息，elapsed.total_seconds()获取响应的时间
		ip_list.append(ips)
		# print(ip_list)
		# print(ips +'--',res.elapsed.total_seconds())
	except BaseException as e:
		print(e)
proxies= {'http':random.choice(ip_list)}
# proxies = random.choice(ip_list)
with open(r'C:/Users/AOAO/Desktop/doubanMovie.csv','w',encoding='gb18030') as f:
	#将文件写入桌面文件doubanMovie中
	writer= csv.writer(f)#写入文件
	writer.writerow(('片名','评分','评语'))#取标题
	for i in range(10):#循环10个页面
		url = 'https://movie.douban.com/top250?start={}'.format(i*25)#页面网站，以25个电影为一页
		data = requests.get(url,headers=headers,proxies=proxies).text
		s = etree.HTML(data)
		print(proxies)#测试是否使用随机ip
		movie = s.xpath('//*[@id="content"]/div/div[1]/ol/li/div')#取得xpath链接
		time.sleep(1)#延迟，防止爬虫被封

		for div in movie :#在单个项目循环，取得name,score,scribe等
			name=div.xpath("./div[2]/div[1]/a/span[1]/text()")[0]
			score= div.xpath("./div[2]/div[2]/div/span[2]/text()")[0]
			scribe= div.xpath("./div[2]/div[2]/p[2]/span/text()")
            
			if len(scribe)>0:#如果scibe存在则打印三个
				f.write("{},{},{}\n".format(name,score,scribe[0]).encode('utf8', 'ignore').decode('utf8'))#写入name,score,scribe，“，”逗号表示在csv中分列表示
			else:#如果不存在则打印两个
				f.write("{},{}\n".format(name,score).encode('utf8', 'ignore').decode('utf8'))
				f.flush()#写入缓存 
