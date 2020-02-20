import random
"""
def generate_sudoku(clues):
    board = [['' for i in range(9)] for j in range(9)]
    
    coordinates = []
    
    for r in range(9):
        for c in range(9):
            coordinates.append((r, c))
    
    selected = random.sample(coordinates, clues)
    
    counter = 0
    while counter < clues:
        counter = 0
        column_sets = [{1,2,3,4,5,6,7,8,9} for i in range(9)]
        row_sets = [{1,2,3,4,5,6,7,8,9} for i in range(9)]
        quadrant_sets = [[{1,2,3,4,5,6,7,8,9} for i in range(3)] for j  in range(3)]
                
        for r, c in selected:
            counter += 1
            
            intersect = column_sets[c] & row_sets[r] & quadrant_sets[r//3][c//3]
            if len(intersect) == 0:
                print ("no intersection")
                break
            
            temp = random.sample(intersect, k = 1)[0]
                    
            column_sets[c].remove(temp)
            row_sets[r].remove(temp)
            quadrant_sets[r//3][c//3].remove(temp)
            
            board[r][c] = str(temp)
        
    
    return board
"""

def generate_sudoku(clues):
    
    board = [['' for i in range(9)] for j in range(9)]
        
    generate(board)
    
    coordinates = []
    
    for r in range(9):
        for c in range(9):
            coordinates.append((r, c))
    
    hidden = random.sample(coordinates, 81 - clues)
    
    for r, c in hidden:
        board[r][c] = ''
    
    
    return board
    
   
def generate(board):
                
    row, col = untested(board)
    
    if row == -1 and col == -1:
        return True
        
    
    random_list = [1,2,3,4,5,6,7,8,9]
    random.shuffle(random_list)
    
    for num in random_list:
        num_str = str(num)
        if is_valid(board, row, col, num_str):
            board[row][col] = num_str
            if generate(board):
                return True
            else:
                board[row][col] = ''       
                
    return False
        
    
def untested(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '':
                return i, j
    
    return -1, -1 


def is_valid(board, row, col, num_str):
    
    box_row = row - row % 3
    box_col = col - col % 3
    
    if check_row(board, row, num_str) and check_col(board, col, num_str) and check_square(board, box_row, box_col, num_str):
        return True
    
    return False

def check_row(board, row, num_str):
    for i in range(9):
        if board[row][i] == num_str:
            return False
    return True

def check_col(board, col, num_str):
    for i in range(9):
        if board[i][col] == num_str:
            return False
        
    return True

def check_square(board, box_row, box_col, num_str):
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num_str:
                return False
    
    return True