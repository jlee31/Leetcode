class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Top down
        cache = {}
        r = len(word1)
        c = len(word2)

        def memo(r,c):
            # base case

            if r == 0:
                return c
            if c == 0:
                return r

            if (r,c) in cache:
                return cache[(r,c)]
            
            if word1[r-1] == word2[c-1]:
                cache[(r, c)] = memo(r - 1, c - 1)
            else:
                cache[(r,c)] = 1 + min(
                                        memo(r-1, c),   # deletion
                                        memo(r, c-1),   # insertion
                                        memo(r-1, c-1)  # replacement
                                    )
             
            return cache[(r,c)]
        return memo(r,c)
