class Trie:
        

    def __init__(self):
        self.trie = dict()

    def insert(self, word: str) -> None:
        curr = self.trie
        for i in range(len(word)):
            if word[i] not in curr:
                curr[word[i]] = [dict(), False]
            if i == len(word) - 1:
                curr[word[i]][1] = True 
            curr = curr[word[i]][0]


    def search(self, word: str) -> bool:
        curr = self.trie
        for i in range(len(word)):
            if word[i] not in curr:
                return False
            if i == len(word) - 1:
                return curr[word[i]][1]
            curr = curr[word[i]][0]
        return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for i in range(len(prefix)):
            if prefix[i] not in curr:
                return False
            curr = curr[prefix[i]][0]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)