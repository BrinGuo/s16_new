import  time


print(time.time())
print(time.altzone/60/60)

print(time.asctime())
print(time.localtime())

t = time.localtime()

print(t.tm_year,t.tm_mon,t.tm_mday,t.tm_hour,t.tm_min,t.tm_wday)


print(time.gmtime())

str_time = time.localtime(time.time() - 86400)
print(time.strftime("%Y%m%d%H%M",str_time))

print(time.ctime())

s_tim = time.strptime("2017-05-08 17:26","%Y-%m-%d %H:%M")
print(time.mktime(s_tim))

p_tim = time.gmtime(1494235560.0)
print(time.strftime("%Y%m%d%H%M",p_tim))


import datetime
print(datetime.datetime.now())


print(datetime.datetime.fromtimestamp(time.time()))

print(datetime.datetime.now() + datetime.timedelta(3))
print(datetime.datetime.now() + datetime.timedelta(-2,hours=-3,minutes=30))

print(datetime.datetime.now().replace(year=2016,month=2))

