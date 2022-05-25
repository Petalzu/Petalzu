from statistics import mean


numbers = []
while True:
        line = input("enter a number or Enter to finish :")
        numbers.append(line)
        if line != (""):
            continue
        else:
            break
del numbers[-1]
numbers = [ int(x) for x in numbers ]
count = len(numbers)
sum1 =  sum(numbers)
maxNum = max(numbers)
minNum = min(numbers)
mean1 = mean(numbers)
print("count =",count,"sum =",sum1,"min =",minNum,"max =",maxNum,"min =",mean1)