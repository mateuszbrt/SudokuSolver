board = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0]
]

def solve (board):
    find = find_empty(board)
    if not find:
        return True
    else: 
        row, col = find
    for i in range(1,10):
        if checkValid(board, i, (row, col)):
            board[row][col] = i
            if solve(board): 
                return True
            
            board[row][col] = 0
    return False

def checkValid (board, number, pos) :

    # Check Row

    for i in range(len(board[0])):
        if board[pos[0]][i] == number and pos[1] !=i :
            return False

    # Check column

    for i in range(len(board)):
        if board[i][pos[1]] == number and pos[0] !=i :
            return False

    # Check Box

    box_X = pos[1] // 3
    box_Y = pos[0] // 3

    for i in range(box_Y * 3, box_Y * 3 + 3):
        for j in range(box_X * 3, box_X * 3 + 3):
            if board[i][j] == number and (i,j) != pos:
                return False
    return True


def print_board (board) :
    for i in range(len(board)) :
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            if j == 8 : 
                print(board[i][j])
            else: 
                print(str(board[i][j]) + " ", end="")

def find_empty (board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0 :
                return (i,j)
    return None

print_board(board)
solve(board)
print(".........................")
print_board(board)