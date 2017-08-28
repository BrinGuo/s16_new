
#file in 2.x only

#3.x is open only


#data = open("file",encoding="utf-8").read()
#file mode r = read   w = write a = append

#写文件
# f = open("file",mode="w",encoding="utf-8")
# f.write("what the fuck!")
# f.write("what the fuck!")
# f.write("what the fuck!")
# f.close()
# #追加文件
# f = open("file",mode="a",encoding="utf-8")
# f.write("\nwhat the fuck!")
#
# f.close()

#修改文件
#先以r 模式  读出来进行修改数据
f = open("file",mode="r",encoding="utf-8")
data = f.read()
data = data.replace("my","memememememe")
f.close()

#修改完成的数据再以 W 覆盖的方式写到文件中
f = open("file",mode="w",encoding="utf-8")
f.write(data)

f.close()
