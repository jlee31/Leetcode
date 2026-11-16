class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)

        if s2_len < s1_len:
            return False 

        hmap = {}

        for s in s1:
            if s in hmap:
                hmap[s] += 1
            else:
                hmap[s] = 1


        print(hmap)

        for i in range(0, s2_len-s1_len+1):
            hmap2 = {}
            for j in range(s1_len):
                if s2[j+i] in hmap2:
                    hmap2[s2[i + j]] += 1
                else:
                    hmap2[s2[i + j]] = 1
            
            print(hmap2)
            for item in hmap2:
                if hmap == hmap2:
                    return True
        return False