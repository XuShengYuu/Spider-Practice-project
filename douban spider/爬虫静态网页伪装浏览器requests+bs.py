import requests
from bs4 import BeautifulSoup
import time
import sys,io 
import csv
#强制改变编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
#伪装浏览器
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
with open (r'C:/Users/AOAO/Desktop/dooubanMovie1.csv','w',encoding='gb18030') as f:
	#保存文件
	writer = csv.writer(f) 
	#写入文件
	writer.writerow(('片名','评分','评语'))
	#标题
	for i in range(10): #循环10个页面
		url='https://movie.douban.com/top250?start={}'.format(i*25)#爬取url，以25个单位为一个页面
		html=requests.get(url,headers=headers).text # 获取网页
		soup=BeautifulSoup(html,"html.parser") # 解析网页parser方法
		ollist = soup.find('ol',attrs={'class':'grid_view'})#找到ol下class标签
		time.sleep(2)#延迟2秒启动，防止爬虫被封
		# print (ollist)
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

