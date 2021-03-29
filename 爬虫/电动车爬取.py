#coding=utf-8
import requests
from lxml import etree
from time import  sleep
import  os
import shutil


#百姓网
# import requests
# from lxml import etree
# from time import  sleep
# import  os
# import shutil
# cc=0
# url='https://suixi.baixing.com/ershoumotuoche/' #需要爬数据的网址
# headers = {
# "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36",
# "Cookie": "__trackId=158588490538339; _ga=GA1.2.2060601410.1585884908; __city=china; __admx_track_id=N39j6Z2hnJ6--oSB470mnQ; __admx_track_id.sig=KrN2PlaS5sgzmYnkDM-wmkGY678; _auth_redirect=https%3A%2F%2Fchina.baixing.com%2Fershoudiandongche%2F; _gid=GA1.2.1007541025.1587371441; Hm_lvt_5a727f1b4acc5725516637e03b07d3d2=1585884908,1585884989,1587106290,1587371441; __s=g5hlnt94t4t2uni3qu9qd0d5l1; __sense_session_pv=29; _gat=1; Hm_lpvt_5a727f1b4acc5725516637e03b07d3d2=1587372735"
# }
# html_date = requests.get(url, headers=headers).text
# # 使用xpath
# html = etree.HTML(html_date)
# # 获取每一页的总页数来判断要循环多少次
#
# ye_list=html.xpath('/html/body/section[2]/div[3]/section[2]/ul/li')
# pagenum=len(ye_list)
#
#
# for i in range(pagenum):
#     newurl=url+'?page=' + str(i+1)
#     html_date = requests.get(newurl, headers=headers).text
#     # 使用xpath
#     html = etree.HTML(html_date)
#     # 获取每一页的总页数来判断要循环多少次
#     carlist = html.xpath('/html/body/section[2]/div[3]/ul/li/a') #/html/body/section[2]/div[3]/ul/li[1]
#     print(len(carlist))
#     for car in carlist:
#         href=car.attrib['href'] #/html/body/section[2]/div[3]/ul/li/a
#         newurl = href
#         html_date = requests.get(newurl, headers=headers).text
#         # 使用xpath
#         html = etree.HTML(html_date)
#         piclist = html.xpath('//*[@id="swiper-container"]/div/div/img')
#
#         picnum=len(piclist)
#         for i in range(picnum-1):
#             img=piclist[i].attrib['data-src']
#             print(img)
#             im = requests.get(img, verify=False)
#
#             name= '/Users/chenchaocun/Downloads/摩托车/'+'mobile_'+str(cc)+'.jpg'
#             cc+=1
#             with open(name, 'wb') as f:
#                 f.write(im.content)
#             sleep(0.2)


#爬百度图片

import requests
import urllib.parse
import re,os

def get_pic_list(name,page):
    new_name = urllib.parse.quote(name)
    for i in range(30,page*30,30):
        url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&word={0}&pn={1}&rn=30'.format(new_name, i)
        html = requests.get(url).text
        #使用正则匹配json中的数据
        pic_list = re.findall('"hoverURL":"(.*?)"',html,re.S)
        down_pic(pic_list)
    print('完成~~~~~~~~~~~~~~~')


def down_pic(L):
    path = '/Users/chenchaocun/Downloads/test/'
    if not os.path.exists(path):
        os.mkdir(path)
    for i in L:
        if i:
            pic = requests.get(i)
            with open(path+'Mask'+'_'+i[-30:], 'wb+')as f:
                f.write(pic.content)
                print('图片'+'Mask'+'_'+i[-30:]+'下载成功')


if __name__ == '__main__':
    # 输入想要的图片名称
    name = '性感美女'
    # 参数5为需要下载的页数，每页30张
    get_pic_list(name, 1000)
