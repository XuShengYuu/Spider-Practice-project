import requests
from bs4 import BeautifulSoup
import time

num= 0 #初始化参数
for a in range(10): # 循环10个页面
	url = 'https://movie.douban.com/top250?start={}'.format(a*25) #爬取网页链接，以25个单位为一个页面
	html = requests.get(url).text #导入网页
	soup = BeautifulSoup(html,"html.parser") #解析网页parser方法
	ollist = soup.find('ol',attrs={'class':'grid_view'}) #找到class标签下的grid_view元素
	img = ollist.find_all('img') # 寻找img标签
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