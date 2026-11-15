class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        n = len(s)
        ret = 0
        left = 0

        for r in range(n):
            while s[r] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[r])
            ret = max(ret, len(seen))
        return ret