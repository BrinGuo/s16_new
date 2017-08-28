

#天生去重
# name = {1,2,3,4,4,4,5,6,6,}
#
# name.add(2222)
# name.remove(2)
# print(name)


#关系运算


a = {1,3,5,7,10}

b = {2,3,4,5,6,8}

print(a & b)   #取交集
print(a.intersection(b)) #取交集


print(b - a)  #取差集
print(b.difference(a)) #取差集

print(a | b)  #取并集
print(a.union(b)) #取并集

print(a ^ b)  #对称差集
print(a.symmetric_difference(b))   #对称差集


print(a.intersection(b))
print(a.intersection_update(b))   #print(a = a.intersection(b))



print(a.issubset(b))  #a是不是 B 的子集

print(a.issuperset(b))  #a是不是 B 的父集




