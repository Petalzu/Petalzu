from ast import Num
from statistics import median


numbers = []
while True:
        line = input("enter a number or Enter to finish :")
        numbers.append(line)
        if line != (""):
            continue
        else:
            break
del numbers[-1]
numbers = [ int(x) for x in numbers]

def get_median(numbers):
    numbers = sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        median = (numbers[size//2]+numbers[size//2-1])/2
        numbers[0] = median
        if size % 2 == 1:
            median = line[(size-1)//2]
            numbers[0] = median
        return numbers[0]
median = get_median(numbers)
print(median)