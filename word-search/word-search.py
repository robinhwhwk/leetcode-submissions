class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, j, current_word):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == "#":
                return False
            current_word += board[i][j]
            index = len(current_word) - 1
            if len(current_word) > len(word) or current_word[index] != word[index]:
                return False
            if current_word == word:
                return True
            temp = board[i][j]
            board[i][j] = "#"
            # match until this current word
            dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for r, c in dirs:
                if backtrack(i + r, j + c, current_word):
                    return True
            board[i][j] = temp

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, ""):
                    return True
        return False
