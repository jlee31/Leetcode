class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        s_len = len(s)
        p_len = len(p)

        def memo(i,j):
            if j == p_len:
                res = i == len(s)
                cache[(i,j)] = res
                return res

            if i == s_len:
                if j + 1 < p_len and p[j + 1] == '*':
                    result = memo(i, j + 2)
                    cache[(i, j)] = result
                    return result
                return False

            if (i, j) in cache:
                return cache[(i, j)]
            
            first_match = (s[i] == p[j]) or p[j] == "."

            if j + 1 < p_len and p[j + 1] == '*':
                
                zero_occurrences = memo(i, j + 2)
                one_or_more = first_match and memo(i + 1, j)
                result = zero_occurrences or one_or_more
                cache[(i,j)] = result
                return result
            

            if first_match:
                result = memo(i+1,j+1)
                cache[(i,j)] = result
                return result
            
            cache[(i,j)] = 0
            return False            
        
        return memo(0,0)
