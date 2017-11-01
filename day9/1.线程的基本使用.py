import threading
import time


"""  多线程示例之一
def task(arg):
    time.sleep(arg)
    print(arg)

for i in range(5):
    t = threading.Thread(target=task,args=[i,])
    #t.setDaemon(True) #主线程终止,不等待子线程
    #t.setDaemon(False) #默认为 False,等待子线程

    t.start()
    #t.join()  #一直等
    t.join(1) #只等一秒钟,等待最大时间


print("end")

"""


# class MyThread(threading.Thread):
#
#
#     def __init__(self,func,*args,**kwargs):
#         super(MyThread,self).__init__(*args,**kwargs)
#         #self._target = 函数
#         #self._target()
#         self.func = func
#
#
#
#     def run(self):
#         #print("...........")
#         self.func()
# def task():
#     time.sleep(1)
#     print(13)
#
# obj = MyThread(func=task)
# obj.start()


