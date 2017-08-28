#!/bin/env python3


#name = 'Alec'
#name2 = name


#print(name,name2)
#print('hello!')


#name = 'Jack'

#print(name,name2)

#%s 字符串  %d 整数 %f浮点数 %r  raw string原生字符

#msg = "my name is %s and age is %s" %("alec",22)

#msg = "my name is %s and age is %s" %("alec","sdfsafsafasf\ndsfsf\t")
msg = "my name is %s and age is %r" %("alec","sdfsafsafasf\ndsfsf\t")
print(msg)

#128  64  32  16  8  4  2  1
#0    0   1   1   1  1  0  0


a = 60    #0    0   1   1   1  1  0  0

b = 13    #0    0   0   0   1  1  0  1

a / 2 = 30 #0 0 0 1 1 1 1 0
#a ^ b = 0 0 1 1 0 0 0 1 = 49
#a & b = 0 0 0 0 1 1 0 0 = 12
#a | b = 0 0 1 1 1 1 0 1 = 61

a = 0 0  1  1  1  1  0  0
~a = 1 1  0  0  0  0  1  1
~a = 128 + 64 + 2 + 1 =195 +1 = 196 -256 +1 = -61
c = a | b
print(c)




#128  64  32  16  8  4  2  1

a = 22 = 0 0 0 1 0 1 1 0
o = 56 = 0 0 1 1 1 0 0 0

a & o =  0 0 0 1 0 0 0 0 = 16
a | o =  0 0 1 1 1 1 1 0 = 62
a ^ o =  0 0 1 0 1 1 1 0 = 46   #一样的都为0 不一样的都为1
~a =
a >> 1 = 0 0 0 0 1 0 1 1 = 11
o << 1 = 0 1 1 1 0 0 0 0 = 112

#三元运算
a = 3
b = 4
if a> b:
    c = a + b
else:
    c = a - b
#转成三元运算
c = a + b if a> b else a - b