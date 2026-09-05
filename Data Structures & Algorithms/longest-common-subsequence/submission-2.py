class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.sub(text1, text2, 0, 0, {})
        
    def sub(self, text1, text2, i, j, memo):
        key = (i, j)
        if key in memo:
            return memo[key]

        if i == len(text1) or j == len(text2):
            return 0

        if text1[i] == text2[j]:
            return 1 + self.sub(text1, text2, i + 1, j + 1, memo)
        
        text1_inc = self.sub(text1, text2, i + 1, j, memo)
        text2_inc = self.sub(text1, text2, i, j + 1, memo)

        memo[key] = max(text1_inc, text2_inc)
        return memo[key]