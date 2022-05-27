num = input("enter the number: ")
number = []
number1 = []
for i in range(0,len(num)):
    number.append(int(num[i]))
    number1.append(int(num[i]))
for i in range(0,len(number)-1):
    for j in range(0,len(number)-1-i):
        if number[j] > number[j+1]:
            number[j],number[j+1] = number[j+1],number[j]
number = [i *10**index for index,i in enumerate(number[::-1])]
a = sum(number)
for i in range(0,len(number1)-1):
    for j in range(0,len(number1)-1-i):
        if number1[j] < number1[j+1]:
            number1[j],number1[j+1] = number1[j+1],number1[j]
number1 = [j *10**index for index,j in enumerate(number1[::-1])]
b = sum(number1)
if a <= b:
    print(b-a)
else:
    print(a-b)