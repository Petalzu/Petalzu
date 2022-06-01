#原问题：

Project 1:
Write a python program to mimic the software of the coffee vending machine in our
teaching building. In summary, coffee vending machine is an automatic machine which
provides coffee items to consumers. When consumerselectsthe coffee item they want
and enters cash into the machine, the machine will make the selected item and guide
consumer to get it. In this project, the coffee vending process should include the
following operations:

1. Program starts with the menu of available items waiting for selection. Each coffee
   item should list its detail information, like Coffee_Name [Ingredients: water 50ml,
   milk 20ml, coffee 30ml, etc.] and price; the menu page should set selection for
   quitting;
2. Once an item is selected, machine should check whether the currently total
   ingredient resource is enough to make the item. If not, print user guide information
   and return to the menu; otherwise continue;
3. Coupon state checking. Ask consumer whether a coupon is available; if yes, guide
   consumer to enter the coupon ID and check its state, and print discount detail; if no,
   guide consumer to continue;
4. Accepting cash. Guide consumer to enter cash and automatically count the total
   amount; accepted cash values are 20 ￥, 10 ￥, 5 ￥ and 1 ￥;
5. Cash processing. Check whether the total amount is enough for the item; if yes,
   guide consumer to receive change; otherwise go back to enter cash continuously or
   quit the transaction;
6. Making coffee. Print the steps of coffee making, e.g., preparing, making, packaging;
7. Guide consumer to take out the item. Return to the welcome menu;
8. Machine should automatically record the sold items and update the profile account
   once a transaction finished.
   An example of this program is:
   #####################################################################
   ################ A nice day starts with a cup of coffee! ##################
   #####################################################################
9. Cappuccino [Water: 50ml; Milk: 50ml; Coffee: 50ml]: 12 ￥
10. Latte [Water: 80ml; Milk: 20ml; Coffee: 50ml]: 10 ￥
11. Mocha [Water: 50ml; Milk: 50ml; Coffee: 40ml; Mocha: 10ml]: 15 ￥
12. Cafe Americano [Water: 100ml; Milk: 0ml; Coffee: 50ml]: 10 ￥
13. Espresso [Water: 70ml; Milk: 0ml; Coffee: 80ml]: 14 ￥
    Quit [Q/q]
    #####################################################################
    $ please select your item: 3
    your item is available, please enter ‘c’ to continue: c
    a coupon is available? [y/n]: y
    please enter your coupon No.: 4312570
    you have a coupon with 80% discount, your item price is: 15\*0.8=12.0
    please enter your cash, how many 20 ￥ count? : 0
    how many 10 ￥ count? :1
    how many 5 ￥ count? :0
    how many 1 ￥ count? :0
    your total amount is: 10.0
    you have not enough money amount for buying, please continue to enter your cash [c]
    or quit with [q]: c
    how many 20 ￥ count? : 0
    how many 10 ￥ count? :0
    how many 5 ￥ count? :1
    how many 1 ￥ count? :0
    your total amount is: 15.0
    your change is: 3.0, please receipt it.
    your coffee is making:
    ……………………………….

## coffee preparing finished!

……………………………….

## coffee making finished!

……………………………….

## coffee packaging finished!

Please take you coffee carefully!
The items sold on this machine are:

# Cappuccino: 0

# Latte: 0

# Mocha: 1

# Cafe Americano: 0

# Espresso: 0

### Total profile: 12.0

coffee.py 为原python文件
dist/coffee.exe 为打包后的exe程序