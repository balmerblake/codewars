def next_bigger(n):
    num = str(n)
    print("num: ", num)
    ord = [dig for dig in num]
    rev = [dig for dig in num[::-1]]
    
    digs = len(rev)

    if digs == 1:
        return -1

    if digs == 2:
        if rev[0] > rev[1]:
            tmp = rev[0]
            rev[0] = rev[1]
            rev[1] = tmp
            return rev_list_to_num(rev)
    
    if digs == 3:
        if rev[0] < rev[1] < rev[2]:
            return -1
        if rev[0] > rev[1]:
            tmp = rev[0]
            rev[0] = rev[1]
            rev[1] = tmp
            return rev_list_to_num(rev)
        elif rev[0] < rev[1] and rev[0] > rev[2]:
            tmp = rev[0]
            rev[0] = rev[2]
            rev[2] = tmp
            return rev_list_to_num(rev)
        elif rev[1] > rev[2]:
            tmp = rev[1]
            rev[1] = rev[2]
            rev[2] = tmp
            return rev_list_to_num(rev)
        else:
            return rev

    for i in range(len(rev)-1):
        if rev[i] > rev[i+1]:
            print("rev[i] ", rev[i], " is greater than rev[i+1] ", rev[i+1])
            tmp = rev[i]
            rev[i] = rev[i+1]
            rev[i+1] = tmp
        return rev_list_to_num(rev)
    
    return -1

def rev_list_to_num(rev):
    return int(''.join(rev[::-1]))



# for iter in range(len(rev)):
#         #check bound
#         if iter + 1 < len(rev):
#             #compare 1's place to 10's place, etc.
#             iter2 = iter
#             #while index in range and dig <= next digit
#             if iter2 + 1 < len(rev) and rev[iter2] <= rev[iter2+1]:
#                 print("rev[iter2]  : ", rev[iter2])
#                 print("rev[iter2+1]: ", rev[iter2+1])
#                 #continue looking through to find next dig smaller than current
#                 while iter2 + 1 < len(rev) and rev[iter2] <= rev[iter2+1]:
# #                     print("iter2++")
#                     iter2+=1
#                 #if found, swap
#                 if rev[iter] > rev[iter2-1]:
#                     for b in rev[iter:iter2]:
#                         if rev[iter] > b:
#                             continue
#                         else:
#                             tmp = rev[iter]
#                             rev[iter] = rev[iter2]
#                             rev[iter2] = tmp
#                             #sort remaining digits after iter2
#                             sub = rev[0:iter]
#                             sub = sub.sort(reverse = True)
#                             sub.append(rev[iter+1:-1])
#                             return list_to_num(new_rev)
#             #swap if 1's place bigger
#             elif iter + 1 < len(rev) and rev[iter] > rev[iter+1]:
#                 print("rev[iter]   : ", rev[iter])
#                 print("rev[iter+1] : ", rev[iter+1])
#                 tmp = rev[iter]
#                 rev[iter] = rev[iter+1]
#                 rev[iter+1] = tmp
                
#                 if len(rev[iter+1:-1]) > 2:
#                     sub = rev[0:iter]
#                     if sub != None and rev[iter:-1] != None:
#                         sub = sub.sort(reverse = True)
#                         print("Sub: ", sub)
#                         print(rev[iter+1:-1])
#                         sub.append(rev[iter:-1])
#                         rev = sub
#                 return list_to_num(rev)