pi = 3.1416
while True:
    try:
        str_num = input('$ Please enter the radius of the circle:')
        num= float(str_num) 
        number = int(num)
        perimeter = 2*number*pi
        area = pi*(number ** 2)
        print("perimeter ="+ str(perimeter) +" "+ "area ="+ str(area))
        break
    except:
        print('You have not inserted a valid number!')
