

def calc(n):
    print(n)
    if int(n/2) > 0:
        n = calc(int(n/2))

    print(n)
    return n

res = calc(10)
print(res)


