def gameOfLife(board):
    """
    Do not return anything, modify board in-place instead.
    """
    neighbors = [(-1,0), (1,0), (0, 1), (0, -1), (1,1), (-1,-1), (-1, 1), (1,-1)]
    copy = [row[:] for row in board]
    
    for row in range(len(copy)):
        for col in range(len(copy[row])):
            count = 0
            for neighbor in neighbors:
                new_row = row+neighbor[0]
                new_col = col+neighbor[1]
                if new_row < 0 or new_row >= len(copy):
                    continue
                elif new_col < 0 or new_col >= len(copy[0]):
                    continue
                elif copy[new_row][new_col] == 1:
                    count+=1

            if copy[row][col] == 1: 
                if count < 2:
                    board[row][col] = 0
                elif count == 2 or count == 3:
                    continue
                elif count >3:
                    board[row][col] = 0
            elif copy[row][col] == 0 and count == 3:
                board[row][col] = 1
    
    return board