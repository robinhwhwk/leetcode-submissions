class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidBox(i, j):
            uniques = set()
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in uniques:
                        # print("not valid box at:", row, col)
                        return False
                    uniques.add(board[row][col])
            return True
        def isValidRow():
            for i in range(len(board)):
                uniques = set()
                for col in range(len(board[0])):
                    if board[i][col] == ".":
                        continue
                    if board[i][col] in uniques:
                        # print("not valid row:", i)
                        return False
                    uniques.add(board[i][col])
            return True
        def isValidCol():
            for j in range(len(board[0])):
                uniques = set()
                for row in range(len(board)):
                    if board[row][j] == ".":
                        continue
                    if board[row][j] in uniques:
                        # print("not valid col:", j)
                        return False
                    uniques.add(board[row][j])
            return True
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not isValidBox(i, j):
                    # print("not valid box:", i, j)
                    return False
        return isValidRow() and isValidCol()