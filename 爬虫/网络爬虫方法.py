from bs4 import BeautifulSoup
import requests
from lxml import etree
from time import  sleep
import  os
import shutil

#绍兴E网
# cc=0
# url='https://secondhand.e0575.com/list.php?cIx=14' #需要爬数据的网址
# headers = {
# "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
# "Cookie": "Hm_lvt_dd009de765b2fae8e1db01f30d425054=1587727862,1588045698; PHPSESSID=nqeqmema5l9521b1up0sbssh60; Hm_lpvt_dd009de765b2fae8e1db01f30d425054=1588045969"
# }
# html_date = requests.get(url, headers=headers).text
#
# # 使用xpath
# html = etree.HTML(html_date)
# # 获取每一页的总页数来判断要循环多少次
# for i in range(10):
#       newurl=url+'&page=' + str(i+1)
#       #print(newurl)
#       html_date = requests.get(newurl, headers=headers).text
#       # 使用xpath
#       html = etree.HTML(html_date)
#       #piclist = html.xpath('/html/body/div[5]/div[1]/ul/li')
#       piclist = html.xpath('/html/body/div[5]/div[1]/ul/li/div[1]/a')
#
#       list = len(piclist)
#
#
#
#       for car in piclist:
#
#
#           #print(type(car))
#           newad = 'https://secondhand.e0575.com/'+car.attrib['href']
#           # print(newad)
#           req = requests.get(url=newad, headers=headers)
#           req.encoding = 'gb2312'
#           html = req.text
#           bf = BeautifulSoup(html, 'lxml')
#           targets_url = bf.find('div', class_='es_show1_d1_p').children
#           for ch in targets_url:
#               ad = str(ch)
#               if not 'img' in ad:
#                   continue
#               ul = ad.split(' ')
#               #print(ul)
#               img_url = ul[-1].split('"')[1]
#               print(img_url)
#
#               img_req = requests.get(url=img_url, headers=headers)
#               path = '/Users/chenchaocun/Downloads/1/'
#               filename = path + 'E_wang_' + str(cc) + '.jpg'
#               f = open(filename, 'wb')
#               f.write(img_req.content)
#               f.close()
#               cc += 1
#               # try:
#               #     img_req = requests.get(url=img_url, headers=headers)
#               #     path = '/Users/chenchaocun/Downloads/1/'
#               #     filename = path + 'E_wang_'+str(cc) + '.jpg'
#               #     f = open(filename, 'wb')
#               #     f.write(img_req.content)
#               #     f.close()
#               #     cc += 1
#               # except:
#               #     continue




#58同城
cc=0
url='https://sz.58.com/danche/0/' #需要爬数据的网址
#url='https://sz.58.com/diandongche/0/'
headers = {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36",
"Cookie": "f=n; commontopbar_new_city_info=4%7C%E6%B7%B1%E5%9C%B3%7Csz; f=n; commontopbar_new_city_info=4%7C%E6%B7%B1%E5%9C%B3%7Csz; userid360_xml=520EA0D94B4A0E1E32DDF3456CE510B1; time_create=1589960860927; timeOver=1587404866903; myLat=""; myLon=""; id58=X2Cjzl6ZVLRJuHhua+Xo9A==; mcity=sz; f=n; city=sz; 58home=sz; 58tj_uuid=55869051-018c-4fa2-b636-8dce2c77d8a1; als=0; wmda_uuid=9dabcd4e67c06962a00d34c2e696309e; wmda_new_uuid=1; xxzl_deviceid=g8VcwsJhYzjexG9QC1ywswiuI2XoIBGvWc6hT5xYynVKm7PtTSMX6gqK7CkhS0f0; sessionid=b027df62-93dc-4067-a6dc-4da6ae44f58f; wmda_visited_projects=%3B11187958619315%3B1409632296065; gr_user_id=ff7a8187-9ab8-4a80-aa26-f85d258288d3; Hm_lvt_3bb04d7a4ca3846dcc66a99c3e861511=1587107017; Hm_lvt_e15962162366a86a6229038443847be7=1587107018; Hm_lvt_e2d6b2d0ec536275bb1e37b421085803=1587107028; wmda_session_id_1409632296065=1587359565217-1a1363b8-33ef-dc6f; new_uv=3; utm_source=; spm=; init_refer=https%253A%252F%252Fsz.58.com%252Fdiandongche%252F%253FPGTID%253D0d3002e0-0000-4e2e-5a85-b13346415f02%2526ClickID%253D1; new_session=0; commontopbar_new_city_info=4%7C%E6%B7%B1%E5%9C%B3%7Csz; commontopbar_ipcity=sz%7C%E6%B7%B1%E5%9C%B3%7C0; gr_session_id_98e5a48d736e5e14=192e1911-fbb1-4e21-b0a0-d73ff984f83b; gr_session_id_98e5a48d736e5e14_192e1911-fbb1-4e21-b0a0-d73ff984f83b=true; wmda_session_id_11187958619315=1587368845635-6016b206-2953-8edd; xxzl_cid=dfc7d69015ab410fa4c825e781d3d44d; xzuid=93dcd5a7-ad5a-4241-a254-86a6c6837c65; Hm_lpvt_e2d6b2d0ec536275bb1e37b421085803=1587368901; ppStore_fingerprint=BB554B878D1F8B52C0E64DA0F984D661E1D33B68E6E4A49C%EF%BC%BF1587368901239; final_history=36727631787396%2C36760339307019%2C41875017187605%2C37732667205636%2C41874024836773; Hm_lpvt_3bb04d7a4ca3846dcc66a99c3e861511=1587369252; Hm_lpvt_e15962162366a86a6229038443847be7=1587369252; xzfzqtoken=wlR2Sx5n%2Bmxg1UvqqYr74iYUS3UC3SFwMi3M0OZBrVnrOZZXrcigF5L7vgtwa6FSin35brBb%2F%2FeSODvMgkQULA%3D%3D"
}
html_date = requests.get(url, headers=headers).text

# 使用xpath
html = etree.HTML(html_date)
# 获取每一页的总页数来判断要循环多少次
ye_list=html.xpath('//*[@id="infolist"]/div[4]/a/span') #/html/body/div[5]/section/div[4]/table/tbody/tr[3]
#print(len(ye_list))

pagenum=len(ye_list)
#allnum=int(ye_list[pagenum].text)
#print(allnum)
for i in range(pagenum):
     newurl=url+'pn' + str(i+1)
     print(newurl)
     html_date = requests.get(newurl, headers=headers)#.text

     html_date.encoding = 'gb2312'
     html = html_date.text


     bf = BeautifulSoup(html, 'lxml')
     #targets_url = bf.find('td', class_='t').children
     #targets_url = bf.find('tr').children
     gets_url = bf.find('table',class_='small-tbimg ac_container').children
     flag=0
     for ch in gets_url:
         for  c in ch:
             ad = str(ch)
             if not 'https' in ad:
                 continue
             print(ad)
             img_url = ad.split('href=')[1].split('"')[1]
             print(img_url)
             #img_url = ul[3].split('"')[1]
             #print(img_url)
             img_req = requests.get(url=img_url, headers=headers)
             img_req.encoding = 'gb2312'
             html = img_req.text
             bf = BeautifulSoup(html, 'lxml')
             try:
                 targets_url = bf.find('ul', class_='switch__big-img _main_img').children
                 print(targets_url)
                 for img in targets_url:
                     ab= str(img)
                     print(ab)
                     if not 'src' in ab:
                         continue
                     ul=ab.split(' ')
                     print(ul)
                     img_url = ul[2].split('"')[1]
                     print(img_url)
                     img_req = requests.get(url='https:'+img_url, headers=headers)
                     print(img_req)
                     path = '/Users/chenchaocun/Downloads/3/'
                     filename = path + '58_D_wang_' + str(cc) + '.jpg'
                     f = open(filename, 'wb')
                     f.write(img_req.content)
                     f.close()
                     cc += 1
             except:
                 continue

             flag += 1
     print(flag)

