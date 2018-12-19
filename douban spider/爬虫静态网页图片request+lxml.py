import requests
from lxml import etree
import time

num=0#初始化参数用来保存图片名
for i in range(10):#循环10个页面，以20个为基准
    url='https://movie.douban.com/top250?start={}'.format(i*20)#页面地址
    r=requests.get(url).content#图片用content
    s=etree.HTML(r)
    imgs=s.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[1]/a/img/@src', stream=True)#取得图片地址,stream=True表示取得原始数据

    time.sleep(1)#延迟启动，防止爬虫被封
    
    for img in imgs:#循环每个图片
        num=num+1#参数加1
        with open('C:/Users/AOAO/Desktop/doubanMovie/'+str(num)+'.jpg', 'wb') as fd:#将图片以jpg格式保存到文件夹中，需要提前建文件夹，否则报错
            picture=requests.get(img).content
            fd.write(picture)