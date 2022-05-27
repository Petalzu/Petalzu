import numbers
import random
import sunau
sum = input("line num=")
number = 1
while True:
    if sum == "":
        if number <= 5:
            articles = ["the","a"]
            subjects = ["cat","dog","man","woman"]
            verbs = ["sang","ran","jumped"]
            adverbs = ["loudly","quietly","well","badly"]
            a = random.sample(articles,1)
            b = random.sample(subjects,1)
            c = random.sample(verbs,1)
            d = random.sample(adverbs,1)
            sen1 = a + b + c + d
            sen2 = a + b + c
            senlist = [sen1,sen2]
            print(random.sample(senlist,1))
            number = number + 1
            continue
        else:
            break
    else:
        sum = int(sum)
        if number <= sum: 
            articles = ["the","a"]
            subjects = ["cat","dog","man","woman"]
            verbs = ["sang","ran","jumped"]
            adverbs = ["loudly","quietly","well","badly"]
            a = random.sample(articles,1)
            b = random.sample(subjects,1)
            c = random.sample(verbs,1)
            d = random.sample(adverbs,1)
            sen1 = a + b + c + d
            sen2 = a + b + c
            senlist = [sen1,sen2]
            print(random.sample(senlist,1))
            number = number + 1
            continue
        else:
            break