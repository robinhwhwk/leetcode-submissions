class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for word in wordDict:
                wordLen = len(word)
                if wordLen > i:
                    continue
                if s[i - wordLen:i] == word and dp[i - wordLen]:
                    dp[i] = True
                    break
        return dp[len(s)]