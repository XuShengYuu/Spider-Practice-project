import requests
from lxml import etree
import time
import random

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
#伪装浏览器
ip_url = 'http://www.xicidaili.com/nn/'
#ip获取网站
ip_data = requests.get(ip_url,headers=headers).text
#请求响应网站，必须有headers伪装浏览器，否则无法爬取
r = etree.HTML(ip_data)
#解析网页
ip = r.xpath('//*[@id="ip_list"]/tr/td[2]/text()')
#xpath获取ip路径
ip_list=[]
#ip列表，用来存储ip
for ips in ip :#测试ip是否可用
    try:
        proxy = {'http':ips}
        text_url = 'https://www.baidu.com/'#测试ip的网站
        res = requests.get(url=text_url,proxies = proxy,headers=headers,timeout=1)
        #请求响应网站，响应超过一秒则断开
        ip_list.append(ips)
        #将可用的ip添加到ip_list中
    except Exception as e:
        print(e)
proxies={'http':random.choice(ip_list)}#随机选择一个ip
num=0#初始化参数用来保存图片名
for i in range(10):#循环10个页面，以20个为基准
    url='https://movie.douban.com/top250?start={}'.format(i*20)#页面地址
    r=requests.get(url,headers=headers,proxies=proxies).content#图片用content
    s=etree.HTML(r)
    imgs=s.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[1]/a/img/@src', stream=True)#取得图片地址,stream=True表示取得原始数据

    time.sleep(1)#延迟启动，防止爬虫被封
    
    for img in imgs:#循环每个图片
        num=num+1#参数加1
        with open('C:/Users/AOAO/Desktop/doubanMovie/'+str(num)+'.jpg', 'wb') as fd:#将图片以jpg格式保存到文件夹中，需要提前建文件夹，否则报错
            picture=requests.get(img).content
            fd.write(picture)