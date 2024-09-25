class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    # Iterate over every cell in the 9x9 grid
    for r in range(9):
        for c in range(9):
            val = board[r][c]
            
            if val == ".":
                continue  # Skip empty cells
            
            # Calculate box index based on row and column
            box_index = (r // 3) * 3 + (c // 3)
            
            # Check if the value is already in the row, column, or box
            if val in rows[r] or val in cols[c] or val in boxes[box_index]:
                return False
            
            # Add the value to the respective row, column, and box sets
            rows[r].add(val)
            cols[c].add(val)
            boxes[box_index].add(val)
    
    return True
