# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

def find_it(seq):
    count = 0
    
    #create a dictionary of key:value tuples where key is the number in the seq and value is the count
    occ = {item : seq.count(item) for item in seq}
    #loop through the tuples created above and check the values for odd counts if an odd count is found, return the key
    for ct in occ.items():
        if (ct[1] == 1) or (ct[1]%2 == 1):
            return ct[0]
    return None