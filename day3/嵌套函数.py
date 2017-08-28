name = "Alec1"
def change_name():
    name = "Alec2"
    def change_name2():
        name = "Alec3"
        print("第三层打印",name)
    change_name2()  #调用内层函数
    print("第二层打印",name)
change_name()
print("最外层打印",name)