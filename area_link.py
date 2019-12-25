import requests
from lxml import etree

class AreaLink(object):
    def __init__(self):
        self.home = 'https://nb.lianjia.com'
    #请求头
    def getheaders(self):
        headers = {
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }
        return headers
    #二手房链接
    def gethome(self):
        home = 'https://nb.lianjia.com/ershoufang/'
        return home
    #get网页并text
    def getershoulink(self):
        area_list = []
        url = self.gethome()
        headers = self.getheaders()
        ershoulink = requests.get(url = url,headers = headers)
    #获取区链接
        page = etree.HTML(ershoulink.text.encode('utf-8'))
        page_list = page.xpath('//div[@class="position"]/dl[2]/dd/div[1]/div[1]/a')
        for i in range(1,len(page_list)+1):
            #获取链接
            getpage_link = page.xpath("//div[@class='position']/dl[2]/dd/div[1]/div[1]/a[" + str(i) +"]/@href")
            page_link = self.home + getpage_link[0]
            #获取地区名
            getpage_name = page.xpath("//div[@class='position']/dl[2]/dd/div[1]/div[1]/a[" + str(i) + "]/text()")
            page_name = getpage_name[0]

            area_list.append([page_name,page_link])
        return area_list

# if __name__ == '__main__':
#     a = AreaLink()
#     print(a.getershoulink())
