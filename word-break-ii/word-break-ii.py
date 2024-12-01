class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        def backtrack(currentWord, currentS, path):
            if len(currentS) < len(currentWord) or currentWord != currentS[:len(currentWord)]:
                return
            path.append(currentWord)
            if "".join(path) == s:
                res.append(" ".join(path))
                path.pop()
                return
            for word in wordDict:
                backtrack(word, currentS[len(currentWord):], path)
            path.pop()
        for word in wordDict:
            backtrack(word, s, [])
        return res