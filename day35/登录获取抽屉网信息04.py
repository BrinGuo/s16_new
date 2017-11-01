

import requests
from bs4 import BeautifulSoup

r1 = requests.post("http://dig.chouti.com")
r1_cookie_dic = r1.cookies.get_dict()

r2 = requests.post("http://dig.chouti.com/login",data={'phone':"863444",'password':"sdfsf",'oneMonth':"1"},cookies=r1_cookie_dic)
r2_cookie_dic = r2.cookies.get_dict()

r3 = requests.post('http://xxxx.com',cookies=r1_cookie_dic)


#print(r3.text)

