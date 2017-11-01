import requests



"""
基本操作,python伪造浏览器发送 http 请求获取指定内容
需要安装以下组件模块
- pip3 install requests
- pip3 install beautifulsoup4
#单间的请求
response = requests.get("http://baidu.com/")
response.text

"""
from bs4 import BeautifulSoup

response = requests.get("http://baidu.com/")
response.text


soup = BeautifulSoup(response.text,'html.parser')
soup.find(name="h3",class_="c1")
soup.find_all(name="h3",class_='c1')



