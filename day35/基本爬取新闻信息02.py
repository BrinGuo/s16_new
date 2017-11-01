"""
1 http://autohome.com.cn/
  代码发送get请求
2 接收响应: 响应头  响应体

3 获取响应体进行解析,方便的获取响应内容

"""


import  requests
from bs4 import BeautifulSoup


#respones = requests.get("http://www.autohome.com.cn/news/")
# respones.status_code
# respones.cookies
# respones.headers
# respones.content  #字节类型的数据
# respones.text     #字符串

#print(respones.text)  #默认中文会乱码


#respones.encoding = "gbk"
#print(respones.text)

#标签对象
#obj = BeautifulSoup(respones.text,'html.parser')
#obj.find('div',attrs= {'id':"auto-channel-lazyload-article",'class':"xxxxx"}) 等于 obj.find(id = "auto-channel-lazyload-article",_class = "article-wrapper")
#obj.find(id = "auto-channel-lazyload-article",_class = "article-wrapper")

#标签对象
#tag = obj.find(name ='div',id='auto-channel-lazyload-article')
#tag.
#列表试的标签对象是一个列表
#tag = obj.find_all(name ='div',id='auto-channel-lazyload-article')
#tag[0].


#示例
respones = requests.get("http://www.autohome.com.cn/news/")
respones.encoding = "gbk"



root = BeautifulSoup(respones.text,"html.parser")
#root.find(id='div',id="auto-channel-lazyload-article")

outer_div_obj = root.find(name='div',id="auto-channel-lazyload-article")
li_obj_list = outer_div_obj.find_all(name= 'li')

for li_obj in li_obj_list:
    if not li_obj.find('h3'):
        continue
    title_obj =  li_obj.find('h3')
    summary_obj = li_obj.find('p')
    #img_obj = li_obj.find('img').attrs#获取所有属性数据类型是一个字典
    img_obj = li_obj.find('img')
    img_src = img_obj.attrs.get('src')
    print(title_obj.text,summary_obj.text,img_src)
    #下载图片
    img_respones = requests.get("http:"+img_src)
    #v = img_src.rsplit('/',maxsplit=1)[1]
    #img_filename = v[1]
    img_filename = img_src.rsplit('/',maxsplit=1)[1]
    print(img_filename)
    with open(img_filename,"wb") as f:
        f.write(img_respones.content)


