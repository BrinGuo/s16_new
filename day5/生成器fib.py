

def fib(max):
    n,a,b = 0,0, 1
    while n < max:
        #print(b)
        yield  b
        # t = a +b
        # a = b
        # b = t

        a,b = b,a+b
        n = n + 1
    return 'done'
f = fib(15)

# for i in f:
#     print(i)

print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print("do somethin now")
print(f.__next__())
print(f.__next__())
print(f.__next__())