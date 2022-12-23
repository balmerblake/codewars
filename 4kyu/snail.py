#Given an n x n array, return the array elements 
#arranged from outermost elements to the middle element, 
#traveling clockwise.

def snail(snail_map):
    answer = []
    #tracks row/col start boundary
    row_s = 0
    col_s = 0
    #tracks row/col end boundary
    row_e = len(snail_map) - 1
    col_e = len(snail_map[0]) - 1
    
    #set bound to not overlap start end vals
    while row_s <= row_e and col_s <= col_e:
        #iter through first row by elem,
        for c in range(col_s, col_e + 1):
            answer.append(snail_map[row_s][c])
        #increment row start val to move downward
        row_s += 1
        
        #iter through last col by elem starting at next row, 
        #append each val
        for r in range(row_s, row_e + 1):
            answer.append(snail_map[r][col_e])
        #decrement col end val to move leftward
        col_e -= 1
        
        #check boundary cond for row start <= row end
        #only needed for non-square matrices
        if row_s <= row_e:
            #iter through last row starting at col end
            for c in range(col_e, col_s - 1, -1):
                answer.append(snail_map[row_e][c])
            #decrement row end val
            row_e -= 1
        
        #check bound cond for col start <= cond end
        #only needed for non-square matrices
        if col_s <= col_e:
            #iter through first row starting at row end
            for r in range(row_e, row_s - 1, -1):
                answer.append(snail_map[r][col_s])
            #increment col start val
            col_s += 1

    return answer