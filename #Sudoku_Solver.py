#Sudoku Solver
#import numpy as np

board = [
            [".","6",".",".","9",".",".",".","."],
            [".",".",".",".","7",".",".","3","."],
            [".",".",".","3",".","1",".","4","6"],
            ["3",".","."," 6",".",".",".",".","."],
            [".",".",".","8","5",".","3",".","."],
            [".","2","1",".","3",".",".",".","."],
            [".",".","9",".",".","5",".","1","3"],
            [".","4",".",".",".",".","5",".","."],
            ["7",".",".",".",".",".","8",".","."]
        ]      

#hello world
def convert(grid:list): #conversion function
    for row in grid: #access each row
        for column in row: #access each column within a row.
            item = row[row.index(column)].strip() #Assign variable item
            if item == ".": #catering for empty slots
                row[row.index(column)] = 0
            else:
                row[row.index((column))] = int(item) #type casting items for easier iteration
    return grid 

new_board = convert(board)
print(f"\n    Problem board:\n {(new_board)}\n")

#defining possible criteria for sudoku

def possible (row, column, number):
    for i in range(0,9): #row iteration
        if new_board[row][i] == number:
            return False
    
    #column interation
    for i in range(0,9):
        if new_board[i][column] == number:
            return False
        
    #square iteration, introducing new variables
    X = (column//3)*3
    Y = (row//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if new_board[Y+i][X+j] == number:
                return False
    return True
        

#defining the solution function
def solve():
    global new_board
    #count = 0
    for row in range(0,9):
        for column in range(0,9):
            #count += 1
            #print(count)
            if new_board[row][column] == 0:
                for number in range(1,10):
                    if possible( row, column, number):
                        new_board[row][column] = number
                        solve()
                    
                        new_board[row][column] = 0
                return
    print(f"\n    Solved board:\n {(new_board)}\n")

solve()


            
