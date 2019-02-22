import requests
import random
from lxml import etree


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
ip_url='http://www.xicidaili.com/nn/'
ip_data = requests.get(ip_url,headers=headers).text
r = etree.HTML(ip_data)
ip = r.xpath('//*[@id="ip_list"]/tr/td[2]/text()')
ip_list= []
for ips in ip:
	try:
		proxy = {'http':ips}
		text_url = 'https://www.baidu.com/'
		res = requests.get(text_url,headers=headers,proxies=proxy,timeout=1)
		ip_list.append(ips)
	except Exception as e:
		print(e)
with open(r'proxies.txt','w')as f:
	for proxy in ip_list:
             f.write('http://'+proxy+'\n')
