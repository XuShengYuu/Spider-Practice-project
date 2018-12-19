import json
import requests
import time
import sys,io


# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #强制改编输出编码，防止乱码

num=0#初始化参数
for a in range(5):#循环5个页面
    url_visit = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E5%8A%B1%E5%BF%97&start={}'.format(a*20)
    #指向的url网址，以20个单位为一个页面
    file = requests.get(url_visit).json()   #这里跟之前的不一样，因为返回的是 json 文件   静态网页用lxml
    time.sleep(2)#延时启动，防止爬虫被封
    
    for i in range(20):#循环20个单位的内容
        dict=file['data'][i]   #取出字典中 'data' 下第 [i] 部电影的信息
        cover=dict['cover']
        covers=[]#建立covers列表
        covers.append(cover)#将cover字典添加到covers列表中
        print(covers)
        for img in covers:#循环covers列表
            num=num+1#参数加一
        with open('C:/Users/AOAO/Desktop/doubanMovie/'+str(num)+'.jpg','wb')as f:
        #以jpg格式写入文件到douban文件夹中，需要先建立文件夹否则报错
            pricture=requests.get(img)
            #获取img
            f.write(pricture.content)
            #写入文件        

