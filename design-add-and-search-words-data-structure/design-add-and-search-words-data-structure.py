class TrieNode:
    def __init__(self):
        self.word = False
        self.children = dict()

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.trie
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.word = True

    def search(self, word: str) -> bool:
        def search_subtree(root, word):
            if not word:
                return root.word
            ch = word[0]
            if ch == ".":
                for child in root.children.values(): # child is a trie node
                    # check if this path has word
                    if search_subtree(child, word[1:]):
                        return True
                return False
            elif ch not in root.children:
                return False
            else:
                root = root.children[ch]
                return search_subtree(root, word[1:])

        return search_subtree(self.trie, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)