name = "Alec Guoooo"

print(name.capitalize())
print(name.casefold())

print(name.center(20,"1"))


print(name.count("G",0,6))

print(name.endswith("oo"))

# name = "Alec\tguo"
# print(name.expandtabs(30))

print(name.find("c"))


msg = "my name is {0},and i am  {1} years old!"
msg2 = "my name is {name},and i am  {age} years old!"

print(msg.format("Alec",22))
print(msg2.format(age=29,name="Jack"))

print("sdfasfas".isalpha())  #是不是字母
print("asfdasf".isalnum())   #是不是阿拉伯数字和字母

print("3".isdecimal())   #是不是整数
print("1".isdigit())
print("ale_x".isidentifier())  #是不是一个合法的变量名

print("alec_x".islower())  #字符是不是全是小写
print("ALEC_X".isupper())  #字符是不是全是大写
print("0".isnumeric())     #是不是数字纯整数不能是小数

print(float("3.1"))     #转成小数

print("My Name Is Alec".istitle())  #判断首字母是不是大写

print("M".join(["alec","gjlin","Jack","4"]))  #把列表以指定字符连接成字符串
print(",".join("alec"))      #把字符串以指定字符连接成字符串

print("Alec".ljust(30,"-"))   #从左往右加够30个字符不够使用指定字符来填充
print("Alec".rjust(30,"7"))    #从右往左加够30个字符不够使用指定字符来填充


print("Alec".lower())      #把大写变小写
print("Alec".upper())      #把小写变大写

print("       Alec Guo \n".lstrip())     #只在左边的去空格
print("       Alec Guo \n".rstrip())     #只在右边去空格
print("   Alec Guo\n".strip())
print("--------------------------")

#不怎么用类似于一个简单加密
from_str = "!@#$%^&"
to_str = "abcdefg"
trans_table = str.maketrans(to_str,from_str)
print("alec".translate(trans_table))

print("alec guo".partition("c"))
print("alec guo".replace("uo","lllll"))
print("alec guo".replace("uo","g",1))   #替换字符 最后跟的数字为替换次数,不跟数字默认是全部匹配替换

print("alec \n g\n uo".splitlines()) #以换行符分割
print("alec guo".split())     #默认以空格分割




