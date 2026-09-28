class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sofar = set()
        l = 0
        longest = 0
        
        for r in range(len(s)):
            while s[r] in sofar:
                sofar.remove(s[l])
                l += 1
            sofar.add(s[r])
            longest = max(longest, len(sofar))
        return longest