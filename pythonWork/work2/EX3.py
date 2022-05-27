from pickletools import string1


string1 = input("please enter a string :")
string2 =string1 [::]
if string1 == string2:
    print(string1,"is a palindrome")
else:
    print(string1,"is not a palindrome")