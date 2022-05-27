def search(lists, need):
    begin = 0 
    finish = len(lists) - 1
    while begin <= finish:
        mid = (begin+finish)//2
        guess = lists[mid]
        if guess < need:
            begin = mid + 1
        elif guess > need:
            finish = mid - 1
        else:
            return(mid)
print(search([1, 5, 8, 7, 3, 6, 4, 2, 9], 1))