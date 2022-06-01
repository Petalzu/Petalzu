#重启前的初始数据
contains_list ={"Water":100,
    "Milk":100,
    "Coffe": 100,
    "Mocha": 100}
kinds_list = {"Cappuccino": 0,
    "Latte": 0,
    "Mocha": 0,
    "CafeAmericano": 0,
    "Espresso" : 0}

#函数封装：1.方便循环。2.方便双重循环的跳出。
def coffee():
    menu_list =[
        {"id": 1, "name":"1.Cappuccino","contains":"[Water: 50ml; Milk: 50ml; Coffee: 50ml]:","price":12,"$":"￥"},
        {"id": 2, "name":"2.Latte","contains":"[Water: 80ml; Milk: 20ml; Coffee: 50ml]:", "price": 10,"$":"￥"},
        {"id": 3, "name":"3.Mocha","contains":"[Water: 50ml; Milk: 50ml; Coffee: 40ml; Mocha: 10ml]:", "price": 15,"$":"￥"},
        {"id": 4, "name":"4.Cafe Americano", "contains":" [Water: 100ml; Milk: 0ml; Coffee: 50ml]:","price": 10,"$":"￥"},
        {"id": 5, "name":"5.Espresso","contains":" [Water: 70ml; Milk: 0ml; Coffee: 80ml]:","price":14,"$":"￥"},
        {"id": 6, "name":"  Quit [Q/q]","contains":" ","price":" ","$":" "}]
    print('##############################################################################\n'
    "##################A nice day starts with a cup of coffee! ####################\n"
    '##############################################################################')
    for menu in menu_list:#从字典取值
        print(menu.get('name'),menu.get('contains'),menu.get('price'),menu.get('$'))
    
    i = 0#用变量来引导前后循环过程，单次循环
    while i < 1: 
        print('#'*78)
        server1 = (input("$ please select your item:(Q/q to quit):"))
        i = i + 1
        if server1 == '1':#判断字典中储存数据是否够
            if contains_list["Water"] >= 50 and contains_list["Milk"] >= 50 and contains_list["Coffe"] >= 50:
                price = 12#拟定价格
                break#跳出循环
            else:
                print("your item is inavailable , back to menu")#无效输入返回函数
                coffee()
        elif server1 == '2':
            if contains_list["Water"] >= 80 and contains_list["Milk"] >= 20 and contains_list["Coffe"] >= 50:
                price = 10
                break
            else:
                print("your item is inavailable , back to menu")
                coffee()
        elif server1 == '3':
            if contains_list["Water"] >= 50 and contains_list["Milk"] >= 50 and contains_list["Coffe"] >= 40 and contains_list["Mocha"] >= 10:
                price = 15
                break
            else:
                print("your item is inavailable , back to menu")
                coffee()
        elif server1 == '4':
            if contains_list["Water"] >= 100 and contains_list["Coffe"] >= 50:
                price = 10
                break
            else:
                print("your item is inavailable , back to menu")
                coffee()
        elif server1 == '5':
            if contains_list["Water"] >= 70 and contains_list["Coffe"] >= 80:
                price = 14
                break
            else:
                print("your item is inavailable , back to menu")
                coffee()
        elif server1 == 'q':
            exit()#重启函数
        elif server1 == 'Q':
            exit()
        else:
            coffee()




    while True:#继续操作判断
        server2 = input("your item is available, please enter 'c' to continue:")
        if server2 == 'c':
            break
        else:
            continue

    #判断是否使用优惠券
    #使用函数封装（此处为coffee()）
    try:#使用try……finally使函数跳出双循环后继续执行之后的代码
        while True:#外循环
            coupon = input("a coupon is available? [y/n]: ")
            if coupon == 'y':
                while True:#内循环
                    number = input("please enter your coupon No.(Q/q to quit):")
                    if number == '666':
                        price = float(price*0.6)
                        print("you have a coupon with 60% discount, your item price is:")
                        print(price)
                        return#跳出函数
                    elif number == '888':
                        price = float(price * 0.8)
                        print("you have a coupon with 80% discount, your item price is:")
                        print(price)
                        return
                    elif number == 'q':
                        break#跳出内循环，继续外循环
                    elif number == 'Q':
                        break
                    else:
                        print("wrong number!")
                        continue#继续内循环
            elif coupon == 'n':
                print("you have a coupon with no discount, your item price is:")
                print(price)
                break#跳出外循环，继续函数
            else:
                continue#继续内循环
    finally:#跳出后继续函数
        #判断金额
        cash = float(0)
        if cash <= price:#首次条件判断
            cash20 = float(input("please enter your cash, how many 20￥count? :"))
            cash10 = float(input("how many 10￥count? :"))
            cash5 = float(input("how many 5￥count? :"))
            cash1 = float(input("how many 1￥count? :"))
            cash = cash1 + cash5*5 + cash10*10 + cash20*20 + cash
            print("your total amount is: " + str(cash))
            while True:
                if cash <= price:#循环条件判断
                    server3 = input("you have not enough money amount for buying, please continue to enter your cash [c] or quit with [q]: ")
                    if server3 == 'c':#循环
                        cash20 = float(input("how many 20￥count? :"))
                        cash10 = float(input("how many 10￥count? :"))
                        cash5 = float(input("how many 5￥count? :"))
                        cash1 = float(input("how many 1￥count? :"))
                        cash = cash1 + cash5*5 + cash10*10 + cash20*20 + cash
                        print("your total amount is: 1" + str(cash))
                        continue
                    elif server3 == 'q':
                        coffee()
                    elif server3 == 'Q':
                        coffee()
                elif cash > price:#判断成功后，打印结束语句
                    charge = float(cash - price)
                    print("your change is: "+ str(charge) + " please receipt it. ")
                    print("your coffee is making:\n"
                    "……………………………….\n"
                    "## coffee preparing finished!\n"
                    "……………………………….\n"
                    "## coffee making finished!\n"
                    "……………………………….\n"
                    "## coffee packaging finished!\n\n\n\n\n")
                
                break


        #记录售卖情况
        if server1 == '1':
            kinds_list["Cappuccino"] = kinds_list["Cappuccino"] + 1
        elif server1 == '2':
            kinds_list["Latte"] = kinds_list["Latte"] + 1
        elif server1 == '3':
            kinds_list["Mocha"] = kinds_list["Mocha"] + 1
        elif server1 == '4':
            kinds_list["CafeAmericano"] = kinds_list["CafeAmericano"] + 1
        elif server1 == '5':
            kinds_list["Espresso"] = kinds_list["Espresso"] + 1
        print("The items sold on this machine are:\n"
        "# Cappuccino: " + str(kinds_list["Cappuccino"]) +"\n"
        "# Latte: " + str(kinds_list["Latte"]) +"\n"
        "# Mocha: " + str(kinds_list["Mocha"]) +"\n"
        "# Cafe Americano: " + str(kinds_list["CafeAmericano"]) +"\n"
        "# Espresso: " + str(kinds_list["Espresso"]) +"\n"
        "### Total profile:"+ str(price))

        #最终确定更改字典中的数据
        if server1 == '1':
            contains_list["Water"] = contains_list["Water"] - 50
            contains_list["Milk"] = contains_list["Milk"] - 50
            contains_list["Coffe"] = contains_list["Coffe"] - 50
        elif server1 == '2':
            contains_list["Water"] = contains_list["Water"] - 80
            contains_list["Milk"] = contains_list["Milk"] - 20
            contains_list["Coffe"] = contains_list["Coffe"] - 50
        elif server1 == '3':
            contains_list["Water"] = contains_list["Water"] - 50
            contains_list["Milk"] = contains_list["Milk"] - 50
            contains_list["Coffe"] = contains_list["Coffe"] - 40
            contains_list["Mocha"] = contains_list["Mocha"] - 10
        elif server1 == '4':
            contains_list["Water"] = contains_list["Water"] - 100
            contains_list["Coffe"] = contains_list["Coffe"] - 50
        elif server1 == '5':
            contains_list["Water"] = contains_list["Water"] - 70
            contains_list["Coffe"] = contains_list["Coffe"] - 80
        coffee()#将数据传到下个循环
coffee()#第一次执行函数

#收获
#1.先用函数封装，再使用try…finally来使跳出双循且结束的部分继续运行之后的代码，这样双跳和单跳都能在同一函数的同一双重循环里运行。
#2.字典确定键值对，然后扔到函数中循环使用就可以了。像变量啊元组都不可以更改地址，但是列表或者字典可以，所以就能保留上一次循环的结果。
#3.不可更改数值更换的是地址指向，称为值传递。
#4.另外一种方法就是把数据储存到库中，在使用时调用数据库一遍一遍覆写，这样就可以永久性更改数值。想恢复数据的话就整个恢复保存的初始数据库。
#总结：有一实际参数a，在调用时又产生一个新的变量x（形式参数），x和a指向相同的地址。如果对x赋值，意味着改变了x指向的内存块，而不改变a的值、
#      如果x是列表，对x[0]赋值，则改变了x[0]指向的内存块，而又因为x[0]的地址是存放在列表中，a又指向了这个列表，因此a也被修改了。