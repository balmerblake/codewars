def move_zeros(lst):
    res = []
    zero_count = 0
    for num in lst:
        if num != 0:
            res.append(num)
        else:
            zero_count += 1
    for i in range(zero_count):
        res.append(0)
    return res