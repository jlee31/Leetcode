class Solution:
    def reverseBits(self, n: int) -> int:
        # using python methods
        # i dont really like this method
        '''
        tmp = []
        bits = format(n, '032b')
        for i in range(31, -1, -1):
            tmp.append(bits[i])
        return int(''.join(tmp), 2)
        '''
        
        # Solution 2:
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res