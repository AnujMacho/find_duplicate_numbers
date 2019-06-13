def find_the_duplicate(lst):
    for a in lst:
        if lst.count(a)>1:
            return a

print(find_the_duplicate([1,2,1,4,3,12]))