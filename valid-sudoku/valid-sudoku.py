class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # print("==== TESTING COLS ====")
        for row in range(len(board)):
            uniques = set()
            for col in range(len(board)):
                if board[row][col] in uniques:
                    return False
                if board[row][col] != ".":
                    uniques.add(board[row][col])
                # print(uniques)
        # print("==== TESTING ROWS ====")
        for col in range(len(board)):
            uniques = set()
            for row in range(len(board)):
                if board[row][col] in uniques:
                    return False
                if board[row][col] != ".":
                    uniques.add(board[row][col])
                # print(uniques)
        # print("==== TESTING BOXES ====")
        for i in range(9):
            starting_row = (i // 3) * 3
            starting_col = (i % 3) * 3
            # print("BOX row:", starting_row, "BOX col:", starting_col)
            uniques = set()
            for j in range(3):
                for k in range(3):
                    nr = starting_row + j
                    nc = starting_col + k
                    if board[nr][nc] in uniques:
                        return False
                    if board[nr][nc] != ".":
                        uniques.add(board[nr][nc])
                    # print(uniques)
        return True