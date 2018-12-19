import requests
import json
import time
import sys,io
import csv

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #强制改编输出编码，防止乱码
#伪装浏览器
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
with open (r'C:/Users/AOAO/Desktop/doubanMovierange.csv','w',encoding='gb18030') as f:#with as 方式写入文件
    writer= csv.writer(f)#写入文件
    writer.writerow(('片名','评分','演员','链接'))#创建标题
    for a in range(5):#循环5个页面
        url_visit = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E5%8A%B1%E5%BF%97&start={}'.format(a*20)
        #指向的url网址，以20个单位为一个页面
        file = requests.get(url_visit,headers=headers).json()   #这里跟之前的不一样，因为返回的是 json 文件   静态网页用lxml
        time.sleep(2)#延时启动，防止爬虫被封

        for i in range(20):#循环20个单位的内容
            dict=file['data'][i]   #取出字典中 'data' 下第 [i] 部电影的信息
            urlname=dict['url']    #取得url标签
            title=dict['title']    #取得title标签
            rate=dict['rate']      #取得rate标签
            cast=dict['casts']     #取得casts标签
            #cover=dict['cover']    #取得cover标签
            f.write('{},{},{},{},{}\n'.format(title,rate,'  '.join(cast),urlname,cover))#写入文件
            