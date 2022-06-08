second = input("please enter rhe number of seconds:")
second = int(second)
num1 = second % 86400
day = int((second - num1)/86400)
num2 = num1 % 3600
hour = int((num1 - num2)/3600)
num3 = num2 % 60
minutes = int((num2 - num3)/60)
seconds = int(num3)
print(second,"seconds correspond to ",day,"day, ",hour,"hours",minutes,"minutes and",seconds,"seconds")