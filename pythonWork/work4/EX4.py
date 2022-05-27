word = str()
word = input("Please enter a character:")
while True:
    if word != 'q':
        a = int(input("Please enter the number of lines:"))
        b = int(input("Please enter the number of columns:"))
        if a == b == 1:
            print(word)
        else:
            print("{}".format(word)*b)
            for i in range(a-2):
                print("{}".format(word)+" "*(b-2)+"{}".format(word))
            print("{}".format(word)*b)
        word = input("Please enter a character:")
    else:
        print("exception raising")
        break