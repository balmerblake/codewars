#Find and store position and value of all peaks in an array
#a peak is any value where the surrounding values are less than the peak value
def pick_peaks(arr):
    pos = []
    peaks = []
    for iter, val in enumerate(arr):
        #skip first val
        if iter == 0: continue
        #set boundary end
        if iter + 1 < len(arr):
            #check for prev val less than current
            if arr[iter - 1] < arr[iter]:
                #check for next val less than curren -> current val is peak
                if arr[iter] > arr[iter + 1]:
                    pos.append(iter)
                    peaks.append(val)
                #check if plateau
                elif arr[iter] == arr[iter + 1]:
                    #use temp iter2 for while loop over plateau length
                    iter2 = iter
                    #escapes on boundary end
                    while (iter2 + 1 < len(arr)) and arr[iter2] == arr[iter2 + 1]:
                        iter2 += 1
                    #if val after plateau is less than plateau val, user orig iter and pos for peak ref
                    if iter2 + 1 < len(arr) and arr[iter] > arr[iter2 + 1]: #+1?
                        pos.append(iter)
                        peaks.append(val)
        #skip final val
        if iter == len(arr) - 1: continue
    return {'pos':pos, 'peaks':peaks}