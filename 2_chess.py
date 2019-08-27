def solution(src, dest):
    # Breadth First Search (BFS)
    # Starting at source, expand search radius by 1 move each iteration, ignoring previously visited squares,
    # and keeping track of number of moves (distance) taken so far.
    # If shortest distance to destination is N, it will be reached in Nth iteration.
    
    if src == dest:
        return 0
    
    NOT_VISITED = -1
    
    # Create 2D 8x8 chess board array, and set all squares to NOT VISITED
    board = [[NOT_VISITED]*8 for i in range(8)]
    # Note: Although this approach might waste space by storing unvisited squares, it is simple.
    # Alternative might be to create a dictionary of visited squares.
    
    
    # Convert linear 64-length position to 8x8
    src_i, src_j = src/8, src%8
    dest_i, dest_j = dest/8, dest%8

    board[src_i][src_j] = 0         # Set source distance to 0

    # All L-shape offsets
    knight_moves = [[1, 2], [1, -2],
                    [2, 1], [2, -1],
                    [-1, 2], [-1, -2],
                    [-2, 1], [-2, -1]]

    queue = []
    queue.append([src_i,src_j])     # Add source to Q
    
    while queue:
        current = queue.pop(0)                          # Get FIFO square position
        distance = board[current[0]][current[1]]        # Get current distance
        
        for move in knight_moves:
            i,j = [sum(x) for x in zip(current, move)]  # Generate new square positions
            
            if 0<= i <8 and 0<= j <8:                   # If new square position is within board
                if board[i][j] == NOT_VISITED:              # If it is not visited
                    board[i][j] = distance + 1              # Set new distance
            
                    if [i,j] == [dest_i,dest_j]:                # If destination reached
                        return board[i][j]                      # Return distance
                    else:                                       # Else
                        queue.append([i,j])                     # Add new square to Q
                else:                                       # Else (NASA style account for every branch)
                    pass                                    # Ignore visited squares
            else:                                       # Else
                pass                                    # Ignore invalid positions