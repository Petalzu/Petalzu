from tkinter import N


number = input("please enter a number: ")
number = int(number)
num1 = number % 10
outnum1 = int((number - num1)/10)
outnum2 = int(num1)
print(outnum1,"\n",outnum2)