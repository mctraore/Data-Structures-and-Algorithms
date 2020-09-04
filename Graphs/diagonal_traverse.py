def findDiagonalOrder(matrix):
    output = []
    direction = 1
    row = 0
    col = 0
    while (row <= len(matrix)-1 and col<= len(matrix[0])-1):
        output.append(matrix[row][col])
        
        # if moving to right, but next value is out of bounds
        if direction==1 and (row-1< 0 or col+1> len(matrix[0])-1):
            direction = -1

            #if curr value is along top edge, except right corner
            if col < len(matrix[0])-1:
                col+=1
            #if curr value is along right edge
            else :
                row+=1
        #moving diagonal right    
        elif direction ==1:
            row-=1
            col+=1
        #if moving to the left, but next value out of bounds
        elif direction==-1 and (row+1> len(matrix)-1 or col-1<0):
            direction = 1

            #if next value is along left edge, except left corner
            if row < len(matrix)-1:
                row+=1
            #next value along bottom edge  
            else:
                col+=1
        #moving diagonal left
        else:
            row+=1
            col-=1
    return output