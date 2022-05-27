def fuction(lists):
    for i in range(0,len(lists)-1):
        for j in range(0,len(lists)-1-i):
            if lists[j] > lists[j+1]:
                lists[j],lists[j+1] = lists[j+1],lists[j]
                print(lists)
lists = [9,6,4,5,7,2,4,8,1,0]
fuction(lists)
