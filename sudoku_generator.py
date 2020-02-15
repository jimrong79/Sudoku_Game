import random

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
  