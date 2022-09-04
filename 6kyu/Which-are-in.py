#takes in two arrays of strings
#returns a sorted list of all strings in list 1 that are contained within the strings in list 2 as substrings
def in_array(array1, array2):
    # your code
    final = []
    for a1 in array1:
        for a2 in array2:
            if a1 in a2:
                if not a1 in final:
                    final.append(a1)
    final.sort()
    return final