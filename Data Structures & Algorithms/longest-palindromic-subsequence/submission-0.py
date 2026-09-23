class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        test2 =s[::-1]

        dp = [[0 for i in range(len(test2) + 1)] for i in range(len(s)+ 1)]
        for i in range(len(s)-1,-1,-1):
            for j in range(len(test2)-1,-1,-1):
                if s[i] == test2[j]:
                        dp[i][j] = 1 + dp[i+1][j+1]
                else:
                        dp[i][j] = max(dp[i+1][j] , dp[i][j+1])

        return dp[0][0]
