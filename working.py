board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# displays the board and 3x3 squares within the board
def display_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])  # prints and then goes to next line
            else:
                print(str(bo[i][j]) + " ", end="")  # end on the same line

# finds the empty cells within the board (represented by zeroes)
def find_empty(bo):
    for row in range(len(bo)):
        for column in range(len(bo[0])):
            if bo[row][column] == 0:
                return (row,column)  # row, col

def valid(bo, num, pos):
    # Check row
    for row in range(bo[0]):
        if num == bo[pos[0]][row] and pos[1] != row:
            return False
    return None

    
    # Check column
    for row in range(len(bo)):
        if bo[row][pos[1]] == num and pos[0] != row:
            return False
    
   




display_board(board)

