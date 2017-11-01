
"""
自动登录github,获取个人信息
1 get https://github.com/session   (get访问获取authenticity_token信息)
    - get访问获取authenticity_token信息
2 post:把以下信息带过去
   commit:Sign in
   utf8:✓
   authenticity_token:BYoWiMkjDJBWpLvi7Q49kWxzSHi+GgEMoZbdjg8EQLr795DwayT6m9kbJAuzsUdfluxDfg0By/+hIqoRwxO7RQ==
   login:sdf
   password:sdff
   响应信息应该有:cookie
3 获取个人信息
   - 携带 cookie

"""

import requests
from bs4 import BeautifulSoup
import conf

#第一次请求,获取token
res1 = requests.get("https://github.com/login")
b1 = BeautifulSoup(res1.text,'html.parser')
authenticity_token = b1.find(name='input',attrs={'name':'authenticity_token'},).get('value')
print(authenticity_token)
print(res1.cookies.get_dict())
res1_cookie_dic = res1.cookies.get_dict()

#第二次请求,发送用户名密码以及token

res2 = requests.post("https://github.com/session",
                     data={
                         'commit':"Sign in",
                         'utf8':"✓",
                         'authenticity_token':authenticity_token,
                         'login':conf.USER,
                         'password':conf.PWD
                     },
                     cookies=res1_cookie_dic)


res2_cookie_dic = res2.cookies.get_dict()
all_cookie_dic = {}
all_cookie_dic.update(res1_cookie_dic)
all_cookie_dic.update(res2_cookie_dic)
print(all_cookie_dic)

#第三次请求,只有登录成功之后才能访问的页面
res3 = requests.get("https://github.com/settings/emails",cookies=all_cookie_dic) #获取个人信息中的email信息
res3_obj = BeautifulSoup(res3.text,'html.parser')

email_obj = res3_obj.find(name='span',attrs={'class':"css-truncate-target"})
#print(res3_obj)
email_content = email_obj.text

print(email_content)