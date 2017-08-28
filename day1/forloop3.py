#!/bin/env python3


# for i in range(10):
#
#     if i == 5:
#         pass
#     else:
#         print("loop",i)

#break 跳出整个循环
#continue 跳出本次循环,进入下次循环

for i in range(10):

    if i == 5:
        for j in range(10):
            print("inner loop",j)
            if j == 6:
                break
        continue
    print("loop",i)