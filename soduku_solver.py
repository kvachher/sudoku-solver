# Creates an empty 9x9 Sudoku board
board = [[0 for _ in range(9)] for _ in range(9)]

# Takes user input, row by row, and creates an array with values to be used in
# the board
def populate_board(bo):
    for i in range (9):
        # prompts the user nine times for each row
        row_input = input("Enter row " + str(i + 1) + 
                          " (9 numbers). Specify empty squares as 0.\n")
        # creates an array of integers, where one index contains the 
        # corresponding number in the input
        row = [int(num) for num in row_input]
        
        # transfers the values over into the parameter board 'bo'
        bo[i] = row
    
# Utilizes a backtracking algorithm to recursively solve each "empty" (0) value
# within the board
def solve(bo):
    # Base case - there are no empty spots
    found = find_empty(bo)
    if not found:
        return True
    else: 
        row, col = found

    # Otherwise, try numbers 1-9 within that spot to see if its valid
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            
            # If able to proceed to next empty spot, then accepted as solved
            if solve(bo) : 
                return True
            
            # If unable to proceed, inserted value is reset to empty
            bo[row][col] = 0
            
    return False

# Uses three different loops in order to check if the value given in the num
# parameter already exists within the column, row, or 3x3 box relative to the 
# position given in the pos parameter
def valid(bo, num, pos):
    # Check to see if same value exists within row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
        
    # Check to see if same value exists within column
    for i in range(len(bo)) : 
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    
    # Check to see if same value exists within 3x3 box
    
    # Uses integer division to index the boxes within the board between (0,0) and
    # (2,2). Stores the index as (box_x, box_y). 
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    
    # Loops through the 3x3 range of box_x and box_y to check if num exists
    for i in range(box_y * 3, box_y * 3 + 3) : 
        for j in range(box_x * 3, box_x * 3 + 3) : 
            if bo[i][j] == num and (i, j) != pos: 
                return False
            
    return True

# Prints the values within the board formatted with horizontal and vertical 
# lines
def print_board(bo):
    for i in range(len(bo)) : 
        # every third row, print a horizontal line
        if i % 3 == 0 and i != 0: 
                print ("- - - - - - - - - - - -")
        
        # prints a horizontal line
        for j in range(len(bo[0])) : 
            if j % 3 == 0 and j != 0: 
                print (" | ", end = "")
            
            # if in the last position, print \n to go to the newline
            if j == 8: 
                print(bo[i][j])
            else: 
                print(str(bo[i][j]) + " ", end = "")

    

# Loops through the entirety of the board, looking for 0-valued (empty) squares
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])) : 
            if bo[i][j] == 0: 
                # if found, return the (row, col)
                return (i, j)
    return None

# Function calls
populate_board(board)
print_board(board)
solve(board)
print("Here is the solved board: ")
print_board(board)
