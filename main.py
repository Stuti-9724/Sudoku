def is_valid_move(grid,row,col,num):
    for x in range(9):
        if grid[row][x]==num:
            return False
        
    for x in range(9):
        if grid[x][col]==num:
            return False
    corner_row=row-row%3
    corner_col=col-col%3
    for x in range(3):
        for y in range(3):
            if grid[corner_row+x][corner_col+y]==num:
                return False
    
    return True

def solve(grid,row,col):
    if col==9:
        if row==8:
            return True
        row+=1
        col=0
    if grid[row][col]>0:
        return solve(grid,row,col+1)
    for num in range(1,10):
        if is_valid_move(grid,row,col,num):
            grid[row][col]=num
            if solve(grid,row,col+1):
                return True
        grid[row][col]=0

    return False




grid=[[ 3, 8, 5, 0, 0, 0, 0, 0, 0],
      [9 ,2, 1, 0, 0, 0, 0, 0, 0 ],
      [6 ,4, 7, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 1, 2, 3, 0, 0, 0],
      [0, 0, 0, 7, 8, 4, 0, 0, 0 ],
      [0, 0, 0, 6, 9, 5, 0, 0, 0 ],
      [0, 0, 0, 0, 0, 0, 8, 7, 3 ],
      [0, 0, 0, 0, 0, 0, 9, 6, 2],
      [0, 0, 0, 0, 0, 0, 1, 4, 5]]

if solve(grid,0,0):
    for i in range(9):
        for j in range(9):
            print(grid[i][j],end=" ")
        print()
else:
    print("No solution exists")
