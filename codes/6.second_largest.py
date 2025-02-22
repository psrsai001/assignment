def second_largest():
    lst = list(map(int, input("enter space seperated numbers for list: ").split(" ")))
    fst = lst[0]
    sec = float("-inf")
    for ele in lst:
        if ele > fst:
            sec = fst
            fst = ele
        if fst != ele and ele > sec:
            sec = ele
    print("Second largest in list:", sec)
