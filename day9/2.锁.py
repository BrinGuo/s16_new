import threading
import time


##############1.只能有一人使用这个锁同时,其他人等
"""
#lock = threading.Lock()  #一个人不能用多个锁
lock = threading.RLock()  #支持一个人带多把锁


v = 10
def task(arg):
    time.sleep(2)
    #申请使用锁,其他人等
    lock.acquire()
    lock.acquire()



    global v
    v -= 1
    print(v)
    lock.release()
    lock.release()
for i in range(10):
    t = threading.Thread(target=task,args=(i,))
    t.start()


"""
###########2.多个人同时使用锁
"""
lock = threading.BoundedSemaphore(3)  #一个人不能用多个锁



v = 10
def task(arg):

    #申请使用锁,其他人等
    lock.acquire()
    time.sleep(2)


    global v
    v -= 1
    print(v)
    lock.release()

for i in range(10):
    t = threading.Thread(target=task,args=(i,))
    t.start()

"""


###########3.事件锁(所有的解脱锁的限制)
#
# lock = threading.Event()  #
#
#
#
# v = 10
# def task(arg):
#
#
#     time.sleep(2)
#     #锁住所有的线程
#     lock.wait()
#     print(arg)
# for i in range(10):
#     t = threading.Thread(target=task,args=(i,))
#     t.start()
# while True:
#     value = input(">>>>>>")
#     if value == '1':
#         lock.set()
#         lock.clear()



##########4.想让他锁几个就锁几个

# lock = threading.Condition()  #
#
# v = 10
# def task(arg):
#
#
#     time.sleep(1)
#     #锁住所有的线程
#
#     lock.acquire()
#     lock.wait()
#
#
#     print("线程",arg)
#
#     lock.release()
#
# for i in range(10):
#     t = threading.Thread(target=task,args=(i,))
#     t.start()
# while True:
#     value = input(">>>>>>")
#     lock.acquire()
#     lock.notify(int(value))
#     lock.release()
