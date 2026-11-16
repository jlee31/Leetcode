class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        # o(m+n)
        if s2_len < s1_len:
            return False 

        hmap = {}
        for s in s1:
            if s in hmap:
                hmap[s] += 1
            else:
                hmap[s] = 1

        # make a copy of hmap for now
        hmap2 = {}
        for i in range(s1_len):
            char = s2[i]
            hmap2[char] = hmap2.get(char, 0) + 1

        if hmap == hmap2:
            return True

        for i in range(s2_len - s1_len): #slide through the rest
            # Remove outgoing character
            char = s2[i]
            hmap2[char] -= 1

            if hmap2[char] == 0:
                del hmap2[char]

            # Add incoming character
            char = s2[i + s1_len]
            hmap2[char] = hmap2.get(char, 0) + 1

            if hmap == hmap2:
                return True

        return False