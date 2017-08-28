


names = {
    "stu001":{"name":"Gjlin","age":22,"hobbie":"girl"},
    "stu002":"alec",
    "stu003":"jack",
    "stu004":"josons",
}

# #search
# print(names["stu001"]["hobbie"])
# print("stu005" in names)   #判断这个key是不是在这个字典里
# print("stu004" in names)   #判断这个key是不是在这个字典里
# print(names.get("stu005"))
# print(names.get("stu001"))  #
# print(names.get("stu005","nonono"))
#
# #add
# names["stu005"] = ['qizhao',26,"zhuli"]
# print(names.get("stu005"))
#
# #update
# names['stu005'][0] = "QiZhao"
# print(names.get("stu005")[0])
#
#
# #delete
#
# print(names.pop("stu008","no find"))
# del names["stu003"]
# print(names)
#
#
#
# namess = ["alec",'gjlin','jack']
#
# #n3 = dict.fromkeys(namess,1)
# n3 = dict.fromkeys(namess,[1,2,3])
# #n3['alec'] = 2
# n3['alec'][1] = 2
# print(id(n3['alec']),id(n3["gjlin"]))
#
#
#
# print(names.items())
#
#
# for key in names:            #效率高
#     print(key,names[key])
#
# for k,v in names.items():    #效率低
#     print(k,v,"========")
#
#
# print(names.keys())
# print(names.values())
#
#
# names.popitem()
# print(names)
#
#
# print(names.setdefault("stu1101","rain"))     #获取一个keys值如果存在就连输出如果不存在就添加
# print(names)
#
#
#
# d1 = {"stu009":'dory',2:3}
# names.update(d1)     #把后面的字典合并到 前面的字典里面
# print(names)
#
#
# #hash  中文又叫散列
#
# #字典的特性:无序  key天生去重 查询效率高于列表

import copy    #深copy
names = {
    "stu001":{"name":"Gjlin","age":22,"hobbie":"girl"},
    "stu002":"alec",
    "stu003":"jack",
    "stu004":"josons",
}
n3 = copy.deepcopy(names) #深copy
n2 = names.copy()    #shalow copy
names["stu003"] = "RAIN"
names["stu001"]["age"] = 24

print(names)
print(n2)
print(n3)

