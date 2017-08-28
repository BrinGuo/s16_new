def Sayhi(name):
    name = name
    print("i am is %s" %name)


Sayhi("gjlin")  #调用函数



#===============================
a = 10
b = 15

c = a ** b

print(c)


def calc(A,B):
    return A ** B
c = calc(a,b)

print(c)


#===============================


def change(N):
    #global n
    N = "change by fuc"
    return N
n = "test"
print(n)
c = change(n)
print(c)
print(n)



#_++++++++========================

def change_list():
    print(names)
    names.append("26")
    names[0] = "alec"
    info['age'] = 22



names = ["gjlin","jack"]
info = {"name":"alec"}
print(id(names),id(names[0]))

change_list()
print(names)
print(id(names),id(names[0]))


