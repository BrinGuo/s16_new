#!/usr/bin/env python3

# def stu_register(name,age,course,country="CN",hobbie="girl"):
#     print("-------------注册学员--------------")
#     print("name:",name)
#     print("age:",age)
#     print("country:",country)
#     print("course:",course)
#     print("hobbie:",hobbie)
#
#
# stu_register("alec",22,"python devops","JP")
# stu_register("alec",22,"python devops",hobbie="sex",country="JP")
# #stu_register("gjlin",25,"CN","linux")
# #stu_register("rain",26,"CN","linux")



#-------------------------------------
def stu_register(name,age,course,country="CN",hobbie="girl",*args,**kwargs):
    print("-------------注册学员--------------")
    print("name:",name)
    print("age:",age)
    print("country:",country)
    print("course:",course)
    print("hobbie:",hobbie)
    print(args,kwargs)
    print(kwargs["stu_id"])
    return True,age


#stu_register("alec",22,"python devops","JP")
a = stu_register("alec",22,"python devops","CN","mm","it","MAN",stu_id="st111")
print(a)
#stu_register("gjlin",25,"CN","linux")
#stu_register("rain",26,"CN","linux")


