class Solution:
    def countSubstrings(self, s: str) -> int:
        # dynamic programming soln
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for length in range(1,n+1): # of length 1 2 3 
            for j in range(n - length + 1): #dp[0][i]
                k = j + length - 1
                if length == 1:
                    dp[j][k] = 1
                elif length == 2:
                    if s[k] == s[j]:
                        dp[j][k] = 1
                elif s[j] != s[k]:
                    continue
                elif s[j] == s[k]:
                    if dp[j+1][k-1]:
                        dp[j][k] = 1

        ret = 0
        for length in range(1,n+1): # of length 1 2 3 
            for j in range(n - length + 1): #dp[0][i]
                k = j + length - 1 
                if dp[j][k] == 1:
                    ret += 1
        return ret
        