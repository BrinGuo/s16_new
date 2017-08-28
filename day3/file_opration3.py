#!/bin/env python3


# f = open("file","r",encoding="utf-8")
#
# print("cursor:",f.tell())
# print(f.read())
#
# print("cursor:",f.tell())
#
# print("----------------------")
# print(f.read())
# print("cursor:",f.tell())
#
#
# f.close()


#-----------
# f = open("file","r",encoding="utf-8")
#
# print("cursor:",f.tell())
# f.seek(10)
# print(f.read(5))
#
# print("cursor:",f.tell())
#
# f.close()

#-----------------
# f = open("file","w+",encoding="utf-8")
# print("cursor:",f.tell())
#
# f.write("asdfsafaafasfa\n")
#
# f.write("我爱你永远")
# print(f.tell())
# f.seek(0)
# print(f.read())
# f.close()

#-------------------
# f = open("file","r+",encoding="utf-8")
# f.write("testtest======test")
# f.close()




#--------------------
f = open("file","rb")

print(f.read(100))


f.close()