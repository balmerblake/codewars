def find_uniq(arr):
    udict = {}
    for num in arr:
        if num in udict:
            udict[num] += 1
        else:
            udict[num] = 1
    for item, value in udict.items():
        if value == 1:
            n = item
    # your code here
    return n   # n: unique number in the array