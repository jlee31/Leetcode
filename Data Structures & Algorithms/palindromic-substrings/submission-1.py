class Solution:
    def countSubstrings(self, s: str) -> int:
        ret = 0

        for i in range(len(s)):
            # odd case
            l,r = i,i
            while l >= 0 and r < len(s) and s[r] == s[l]:
                ret += 1
                l -= 1 
                r += 1
            # even case
            l,r = i,i+1
            while l >= 0 and r < len(s) and s[r] == s[l]:
                ret += 1
                l -= 1 
                r += 1
        return ret