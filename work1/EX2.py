line1 = input("Please enter the first number: ")
line2 = input("Please enter the seccond number: ")
a = int(line1)
b = int(line2)
div = a // b
mod = a % b
while mod < 11:
    if(mod == 0):
        a = str(a)
        b = str(b)
        print(a + " is a multiple of " + b)
        break
    else:
        a = str(a)
        b = str(b)
        print(a + " is not a multiple of " + b)
        break