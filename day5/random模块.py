import random
import string


print(random.randint(1,10))

print(random.randrange(1,10))
print(random.randrange(1,20,2))
print(random.sample([1,2,3,4,4],3))
print(random.sample(range(100),3))
print(random.sample(list({"a":3,"b":4,"c":5,"d":6,"e":7}),3))


#随机验证码生成

source = string.digits + string.ascii_lowercase
print("".join(random.sample(source,7)))