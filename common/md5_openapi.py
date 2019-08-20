# coding: utf-8
import json
import time
import hashlib
import uuid
import requests
from information.read_method import AppId, URL, SECRET


class openApi():
    def __init__(self, app_Id=None, base_url=None, secret=None):
        if app_Id:
            self.app_Id=app_Id
        else:
            self.app_Id=AppId
        if base_url:
            self.base_url=base_url
        else:
            self.base_url=URL
        if secret:
            self.secret=secret
        else:
            self.secret=SECRET

    def signature(self):
        content=(self.app_Id + self.secret + str(int(time.time() * 1000)) + self.body).encode('utf-8')
        return hashlib.md5(content).digest().hex()

    def url(self, path):
        return self.base_url + path

    def call(self, data, path):
        self. headers ={"Content-Type": "application/json",
                      "sign": "",
                      "appId": self.app_Id,
                      "contextId": uuid.uuid4().hex,
                      "timestamp": str(int(time.time() * 1000))
                      }
        url=self.base_url + path
        self.body=json.dumps([data], ensure_ascii=False)
        print(type(self.body))
        self.headers["sign"]=self.signature()

        self.r=requests.post(url, data=self.body.encode('utf-8'), headers=self.headers).content
        return self.r

    def is__success(self, i):
        if i in str(self.r):
            return True
        else:
            print("返回的数据不存在%d" % i)
            return False


if __name__ == '__main__':
    x=openApi()
    data={
        "parcelNoType": "1000",
        "parcelNo": "e1299ea376564485961898a991457b15",
        "relatedNo": "20190428111"
    }
    r=x.call(data, "open/api/v1/provider/parcel/international/delivery/no")
    x.is__success("success")

# appId="16437eb845e9475da78d1e14a97f0285"
# secret="87d2965d6fe348b6918188a029fad346"
# url="https://test-api.int.parcelfuture.com/open/api/v1/provider/parcel/international/delivery/no"
#
#
# headers={"Content-Type": "application/json",
#          "sign": "9c95ad6be97bd56903548ea2fc78bc73",
#          "appId": "16437eb845e9475da78d1e14a97f0285",
#          "contextId": "213123",
#          "timestamp": str(int(time.time() * 1000))
#          }
#
# body=json.dumps([{
#         "parcelNoType": "1000",
#         "parcelNo": "e1299ea376564485961898a991457b15",
#         "relatedNo": "20190428111",
#     }],ensure_ascii=False)
# content=(appId + secret+str(int(time.time() * 1000))+ body).encode('utf-8')
# new_signature=hashlib.md5(content).digest().hex()
# print(new_signature)
# headers["sign"]=new_signature
# print(headers["sign"])
# print(headers)
#
# r=requests.post(url, data=body.encode('utf-8'), headers=headers)
# print(r.content)
