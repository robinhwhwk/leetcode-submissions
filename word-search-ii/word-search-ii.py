class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.isWord = True

    def search(self, word) -> bool:
        curr = self.root
        for i in word:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        return curr.isWord
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        res = set()
        def findWord(i, j, current_word, node):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == "#":
                return
            if not board[i][j] in node.children:
                return
            current_word += board[i][j]
            node = node.children[board[i][j]]
            
            if node.isWord:
                res.add(current_word)

            temp = board[i][j]
            board[i][j] = "#"
            
            findWord(i + 1, j , current_word, node) 
            findWord(i - 1, j, current_word, node)  
            findWord(i, j + 1, current_word, node) 
            findWord(i, j - 1, current_word, node) 
            board[i][j] = temp
        
        trie = Trie()
        for word in words:
            trie.insert(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                findWord(i, j, "", trie.root)
        return list(res)