import requests
from lxml import etree
from area_link import AreaLink as al

class Houses(object):

    def gethouselink(self):
        page_link = al.getershoulink()
        headers = al.getheaders()
        for i in page_link:
            arealink = requests.get(url=i[1],headers=headers)
            page = etree.HTML(arealink.text.encode('utf-8'))
            return arealink

if __name__ == '__main__':
    h = Houses()
    h.gethouselink()
