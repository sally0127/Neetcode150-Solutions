**8.Valid Sudoku**
-
🔗 Link: Valid Sudoku(https://neetcode.io/problems/valid-sudoku)

💡 Difficulty: Medium

🛠️ Topics: Array/Matrix,Hashing or Sets

==========================================================
You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.

Each column must contain the digits 1-9 without duplicates.

Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.

Example 1:

Input: board = 
[["1","2",".",".","3",".",".",".","."],

 ["4",".",".","5",".",".",".",".","."],
 
 [".","9","8",".",".",".",".",".","3"],
 
 ["5",".",".",".","6",".",".",".","4"],
 
 [".",".",".","8",".","3",".",".","5"],
 
 ["7",".",".",".","2",".",".",".","6"],
 
 [".",".",".",".",".",".","2",".","."],
 
 [".",".",".","4","1","9",".",".","8"],
 
 [".",".",".",".","8",".",".","7","9"]]

Output: true

Example 2:

Input: board = 
[["1","2",".",".","3",".",".",".","."],

 ["4",".",".","5",".",".",".",".","."],
 
 [".","9","1",".",".",".",".",".","3"],
 
 ["5",".",".",".","6",".",".",".","4"],
 
 [".",".",".","8",".","3",".",".","5"],
 
 ["7",".",".",".","2",".",".",".","6"],
 
 [".",".",".",".",".",".","2",".","."],
 
 [".",".",".","4","1","9",".",".","8"],
 
 [".",".",".",".","8",".",".","7","9"]]

Output: false

Explanation: There are two 1's in the top-left 3x3 sub-box.

Constraints:

．board.length == 9
．board[i].length == 9
．board[i][j] is a digit 1-9 or '.'.

**UMPIRE Method**:

**Understand**

．Can the board contain empty cells?

．Do we need to solve the Sudoku?

．Is the input always a 9x9 board?

**Match**

This problem falls under the Array/Matrix category and can be solved using Hashing or Sets to track the unique numbers.

Key Observations:

．We need to validate three things: rows, columns, and sub-boxes.

．Each check can be done independently by traversing the board.

**Plan**

General Idea:

．Use three sets to track:

1.Numbers in each row.

2.Numbers in each column.

3.Numbers in each 3x3 sub-box.

For every element in the Sudoku board:

．Check the row, column, and sub-box for duplicates.

．If any rule is violated, return false. If all checks pass, return true.

Pseudocode:
1.Initialize three data structures:

．A set for each row.

．A set for each column.

．A set for each 3x3 sub-box.

2.Loop through each cell in the 9x9 grid:

．If the cell contains a digit (i.e., not .):

    Check if the digit exists in the current row's set, column's set, or sub-box's set.

    If it exists, return false.

    If not, add the digit to the respective sets.

3.If the entire board is valid, return true.

**Implement**

see solution.py

**Review**

board = 
[["5","3",".",".","7",".",".",".","."],

 ["6",".",".","1","9","5",".",".","."],
 
 [".","9","8",".",".",".",".","6","."],
 
 ["8",".",".",".","6",".",".",".","3"],
 
 ["4",".",".","8",".","3",".",".","1"],
 
 ["7",".",".",".","2",".",".",".","6"],
 
 [".","6",".",".",".",".","2","8","."],
 
 [".",".",".","4","1","9",".",".","5"],
 
 [".",".",".",".","8",".",".","7","9"]]

Output: True

**Evaluate**

Time Complexity:

．We are iterating through all 81 cells of the 9x9 grid once, so the time complexity is O(81) = O(1) (since the board size is fixed).

Space Complexity:

．We use three sets for rows, columns, and boxes, each containing up to 9 elements, so the space complexity is O(9*3) = O(1).

This approach efficiently checks all conditions for a valid Sudoku board.




