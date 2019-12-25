import requests
from lxml import etree

home = 'https://nb.lianjia.com/ershoufang/'

headers = {
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }
page = requests.get(url=home,headers=headers)
area = etree.HTML(page.text.encode('utf-8'))

pagelink = area.xpath('//div[@class="position"]/dl[2]/dd/div[1]/div[1]/a')
print(type(pagelink))
print(len(pagelink))