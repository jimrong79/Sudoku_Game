import random

def is_valid_sudoku(board):

    rows = [set() for i in range(9)]
    cols = [set() for i in range(9)]
    quads = [[set() for i in range(3)] for j in range(3)]
    
    
    for r in range(9):
        for c in range(9):
            if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in quads[r//3][c//3]:
                return False
            else:
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                quads[r//3][c//3].add(board[r][c])
                
    return True


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