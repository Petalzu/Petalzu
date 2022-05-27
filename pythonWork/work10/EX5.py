word = input("enter your word: ")
check = input("enter your check: ")
word1 = []
check1 = []
for i in range(0,len(word)):
    word1.append(word[i])
for i in range(0,len(check)):
    check1.append(check[i])
boolen = set(word1) >= set(check1)
print(boolen)