#!/bin/env python3


product_list = [

    ['iphone7',6500],
    ['macbook',1200],
    ['pythonbook',66],
    ['coffee',31],
    ['bike',999]
]


shooping_cart = []
salary = int(input('input your salary:'))

while True:
    for index,v in enumerate(product_list):
        print("%s.\t%s\t%s" %(index,v[0],v[1]))
    choice = input(">>>>:").strip()

    if len(choice) == 0:
        print("不往下走了...")
        choice = input(">>>>:")
    if choice.isdigit():
        choice = int(choice)
        if choice < len(product_list) and choice >= 0:
            product_item = product_list[choice]
            print(product_item)
            if salary >= product_item[1]: #买得起
                salary -= product_item[1]  #扣钱
                shooping_cart.append(product_item)
                print("added \033[32;1m %s\033[0m input your shooping cart ,you current balance \
                is \033[31;1m%s\033[0m" %(product_item[0],salary))
            else:
                print("sorry,Can't afford this product ,still need %s" %(product_item[1] - salary))
        else:
            print("没有此商品!")
    elif choice == "exit":
        total_cost = 0
        print("you have bought below products:")
        for shopping_list in shooping_cart:
            print(shopping_list)
            total_cost += shopping_list[1]
        print('your current balance is :',salary,"      total cost is:",total_cost)
        break