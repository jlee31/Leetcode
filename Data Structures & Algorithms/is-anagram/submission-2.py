from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = len(s)
        l2 = len(t)
        if l1 != l2:
            return False
        count1=defaultdict(int)
        count2=defaultdict(int)
        for c in s:
            count1[c]+=1
        for c in t:
            count2[c]+=1
        
        return count1 == count2
        