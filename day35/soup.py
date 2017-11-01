from  bs4 import BeautifulSoup
import json

html_doc = """
<html>
    <head>
        <title>
        The dormouse's story!
        </title>
    </head>
    <body>
        <!--<a  class="c1">详解</a>-->
        <div class="c1">
            dfdasf
            <a class="">内容一<span>888</span></a>
        </div>
    </body>
</html>
"""



#soup = BeautifulSoup(html_doc,features="html.parser")#也可以使用"lxml"这个效率更高,但是需要安装使用方法和"html.parser"一模一样
#tags = soup.find_all(attrs={'class':'c1'})


#1.name属性
"""
#1.name属性
soup = BeautifulSoup(html_doc,features="html.parser")#也可以使用"lxml"这个效率更高,但是需要安装使用方法和"html.parser"一模一样
tags = soup.find_all(attrs={'class':'c1'})
for tag in tags:
    print(tag.name)
"""


#2.attrs 属性
"""
soup = BeautifulSoup(html_doc,features="html.parser")#也可以使用"lxml"这个效率更高,但是需要安装使用方法和"html.parser"一模一样
#tag = soup.find(attrs={"class":'c1'})
tag = soup.find(class_="c1")
print(tag)

tag.attrs['id'] = 1  #attrs可以查找\修改\添加\删除属性,而find只能查找
del tag.attrs['class']

print(tag)
"""


#3.children 属性,所有子标签(所有的孩子)
"""
soup = BeautifulSoup(html_doc,features="html.parser")#也可以使用"lxml"这个效率更高,但是需要安装使用方法和"html.parser"一模一样
tag = soup.find(attrs={"class":'c1'})
print(list(tag.children))
"""

#4.descendant属性,所有的后代
"""
soup = BeautifulSoup(html_doc,features="html.parser")#也可以使用"lxml"这个效率更高,但是需要安装使用方法和"html.parser"一模一样
tag = soup.find(attrs={"class":'c1'})
print(list(tag.descendants))

#find_all 是只找标签不会把标签里面的内容单独找出来
soup = BeautifulSoup(html_doc,features="html.parser")#也可以使用"lxml"这个效率更高,但是需要安装使用方法和"html.parser"一模一样
tag = soup.find(attrs={"class":'c1'})
print(tag.find_all())
print(tag.find_all(recursive=False))  #这个recursive=False参数是 False 时他找所有子标签,True 只找一层
"""


#5.clear. 清除这个标签内的所有子标签和内容,保留当前标签
"""
soup = BeautifulSoup(html_doc,features="html.parser")#也可以使用"lxml"这个效率更高,但是需要安装使用方法和"html.parser"一模一样
tag = soup.find(attrs={"class":'c1'})
tag.clear()
print(soup)

"""

#



