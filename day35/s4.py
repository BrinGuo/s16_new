import requests


requests.get()
requests.request(
    method='POST',
    url='baidu.com',
    params={},
    data={},#json


)

#data参数(json)
import  json
requests.post(url="baidu.com",data={'name':"brin","age":18}) #application/x-www-form-urlencoded
requests.post(url="baidu.com",data="name=brin&age=18")  #application/x-www-form-urlencoded


requests.post(url='www.baidu.com',data=json.dumps({'name':"brin","age":18}),headers={'Content-type':'apllication/json'})#application/json;charset=UTF-8
requests.post(url='www.baidu.com',json={'name':"brin","age":18})#application/json;charset=UTF-8

#headers 请求头



#cookies,cookie


"""
这些是必须要会的参数
1.methed
2.url
3.params
4.data
5.json
6.headers
7.cookies
8.files
9.auth
10.timeout
11.allow_redirects
12.proxies
13.stream
14.cert
===============session=============
"""
import requests
session_is = requests.Session()



i1 = session_is.get(url="http://dig.chouti.com/help/service")
i2 = session_is.post(
    url="http://dig.chouti.com/help/service",
    data={
        'phone':'1333333333',
        'password':'111111111',
        'oneMonth':'',
    },

                     )

i3 = session_is.post(
    url="http://dig.chouti.com/link/vote?linkesId=8876788",

)

print(i3.text)

#==================session===========
#8.files


#9.auth,github和无线路由器的登录都是这样的

from requests.auth import HTTPBasicAuth,HTTPDigestAuth
from requests.auth import HTTPProxyAuth

ret = requests.get('http://api.github.com/user',auth=HTTPBasicAuth('Bringuo','password'))
print(ret.text)

