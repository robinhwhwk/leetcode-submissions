class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # bfs process queue
        queue = [beginWord]
        visited = set()
        visited.add(beginWord)
        wordSet = set(wordList)
        len_sequence = 1
        while queue:
            size = len(queue)
            for i in range(size):
                current_word = queue.pop(0)
                if current_word == endWord:
                    return len_sequence
                for j in range(len(current_word)):
                    for k in range(0,27):
                        replace = chr(ord('a') + k)
                        new_word = current_word[:j] + replace + current_word[j + 1:]
                        if new_word in wordSet and new_word not in visited:
                            queue.append(new_word)
                            visited.add(new_word)
            len_sequence += 1
        return 0