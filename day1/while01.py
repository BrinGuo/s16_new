#!/bin/env python3
import  time

t0_starttime = time.time()
count = 0
while True:
    #print("你是风儿我是沙,缠缠绵绵到天涯....",count)


    count +=1

    if count == 100000000:
        break

print("cost_0:",time.time() - t0_starttime,"num:",count)



t1_starttime = time.time()
count = 0
while count < 100000000:
    count +=1
print("cost_1:",time.time() - t1_starttime,"num:",count)

