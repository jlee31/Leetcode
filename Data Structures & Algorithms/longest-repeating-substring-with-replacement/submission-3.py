class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        A = [0] * 26
        
        for r in range(len(s)):
            A[ord(s[r]) - 65] += 1  
            while (r-l+1) - max(A) > k:
                A[ord(s[l]) - 65] -= 1
                l += 1
            longest = max(longest, (r-l+1))
        return longest
        