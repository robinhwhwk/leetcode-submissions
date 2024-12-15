class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        wordSet = set(wordDict)
        for i in range(len(s)):
            for j in range(i, -1, -1):
                word = s[j:i+1]
                if word in wordSet and dp[j]:
                    dp[i + 1] = True
                    break
        return dp[len(s)]