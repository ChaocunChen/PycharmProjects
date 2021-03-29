import os,shutil
names = os.listdir('/Users/chenchaocun/Downloads/Gallery-2')

f =open('/Users/chenchaocun/Desktop/c.rtf', 'w+')

for i in names:

    print(i)
    Fold_name=i.split('.jpg')[0]
    print(Fold_name)
    os.mkdir('/Users/chenchaocun/Desktop/c1/'+str(Fold_name))
    shutil.copy('/Users/chenchaocun/Downloads/Gallery-2/'+i,'/Users/chenchaocun/Desktop/c1/'+str(Fold_name))

for j in os.listdir('/Users/chenchaocun/Desktop/c1'):

    #with open('/Users/chenchaocun/Desktop/c.rtf', 'w') as f:
    f.write('/Users/chenchaocun/Desktop/c1/' + str(j) + '/' + str(j) + ' ' + str(j) + '\n')
    #for j in os.listdir('/Users/chenchaocun/Desktop/c1/'+i):
f.close()


import json
import urllib3
TEST_URL = 'http://127.0.0.1:10021/request/makebase'
path = "/opt/gemfield/bin/data/Gallery.txt"
name = "Gallery"

req_dict = dict()
req_dict["file_path"]=path
req_dict["base_name"]=name
data_str = json.dumps(req_dict)
http_conn = urllib3.PoolManager()
txt_audit_resp =http_conn.request('POST',TEST_URL,body=data_str)
print(txt_audit_resp.data.decode('utf8'))

import os,time,json
import urllib3

TEST_URL = 'http://127.0.0.1:10021/request/image'
path = "/root/Probe"
path1 = "/opt/gemfield/bin/data/Probe"
for i,file in enumerate(os.listdir(path)):
    star =time.time()
    req_dict = dict()
    print(file)
    req_dict["file_id"] = "{}".format(i)
    req_dict["file_path"] = path1+ '/' + file
    req_dict["base_name"] = "source"
    data_str = json.dumps(req_dict)
    http_conn = urllib3.PoolManager()
    txt_audit_resp = http_conn.request('POST', TEST_URL, body=data_str)
    end = time.time()
    print(end-star)

    print(txt_audit_resp.data.decode('utf8'))
