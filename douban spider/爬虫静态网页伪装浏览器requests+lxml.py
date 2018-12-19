# requests+lxml爬取静态网页并保存为csv文件
# 引入库
import requests
import sys,io 
from lxml import etree
import time
import csv
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') 
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
# 强制改变输出编码，防止输出时乱码
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
#伪装浏览器
with open(r'C:/Users/AOAO/Desktop/doubanMovie.csv','w',encoding='gb18030') as f:
	#将文件写入桌面文件doubanMovie中
	writer= csv.writer(f)#写入文件
	writer.writerow(('片名','评分','评语'))#取标题
	for i in range(10):#循环10个页面
		url = 'https://movie.douban.com/top250?start={}'.format(i*25)#页面网站，以25个电影为一页
		data = requests.get(url,headers=headers).text
		s = etree.HTML(data)
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
