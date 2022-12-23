#Function takes a list of strings as input
#It then finds the longest substring of vowels in each string
#It then stable sorts the strings based on the longest substring of vowels
def sort_strings_by_vowels(seq): 
    counts = []
    v_count = 0
    mv_count = 0
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    
    for sent in seq:
        for char in sent:
            #Each time a vowel is encountered, add to the counter
            #If the counter is greater than the current max counter for the string
            #Change the max counter to the new count
            if char in vowels:
                v_count += 1
                if v_count > mv_count:
                    mv_count = v_count
            #If a non-vowel is encountered, reset the current counter
            else:
                v_count = 0
        #After all characters are traversed, 
        #append the sentence and count to a list
        #reset the counter and max count
        counts.append([sent, mv_count])
        v_count = 0
        mv_count = 0
        
    #sort the list of sentence/counts by the count value, with reverse to keep stable
    counts.sort(key=lambda x : x[1], reverse = True)
    
    #return the list of sentences after sorting
    return [sent[0] for sent in counts]
    pass