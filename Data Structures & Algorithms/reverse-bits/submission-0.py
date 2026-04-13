class Solution:
    def reverseBits(self, n: int) -> int:
        tmp = []
        bits = format(n, '032b')  # e.g. '00000000000000000000000000000101'
        for i in range(31, -1, -1):
            tmp.append(bits[i])
        return int(''.join(tmp), 2)