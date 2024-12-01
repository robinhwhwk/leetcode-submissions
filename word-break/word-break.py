class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 1-d dp solution
        # iterate through the string
        # if current string matches a word, set it to true
        # for each word in wordDict, check if current_string - word is true
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        wordSet = set(wordDict)
        for i in range(1, len(s) + 1):
            for j in range(i - 1, -1, -1):
                if s[j:i] in wordSet and dp[j]:
                    dp[i] = True
                    break
        return dp[len(s)]
