class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        lenRes = 0

        for i in range(len(s)):

            # odd case
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > lenRes:
                    res = s[l:r+1]
                    lenRes = r - l + 1
                l -= 1
                r += 1

            # even case
            l,r = i, i+1
            # print(s[i])
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > lenRes:
                    res = s[l:r+1]
                    lenRes = r - l + 1
                l -= 1
                r += 1

        return res
