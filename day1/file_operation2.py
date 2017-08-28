import  os
#file in 2.x only

#3.x is open only
f = open("file",mode="r",encoding="utf-8")
# print(f.readline().strip())
#
# print(f.readline().strip())
# print(f.readline().strip())
f_new = open("file_2",mode="w",encoding="utf-8")
for line in f:
    if "my" in line:
        line = line.replace("my","me")
    f_new.write(line)
f.close()
f_new.close()

os.remove("file")
os.rename("file_2","file")