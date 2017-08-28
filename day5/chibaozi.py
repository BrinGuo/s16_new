import time
from collections import Iterable
def consumer(name):
    print("%s 准备吃饺子" %name)
    while True:
        baozi = yield #接收到 producter send 传过来的包子 赋值给 baozi 变量
        print("包子%s来了,被%s 吃了"%(baozi,name))

def producer(name):
    c = consumer("sb")
    c2 = consumer('2b')
    c.__next__()
    c2.__next__()
    print("%s要做包子了"%name)
    for i in range(2*5):
        #time.sleep(1)
        print("%s做了两个包子"%name)
        c.send(i)  #调用 next 并传传了一个参数给 yield
        c2.send(i)
    if isinstance(100,Iterable):
        print("ok")
    else:
        print("false")


producer('BrinGuo')
