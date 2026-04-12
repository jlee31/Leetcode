class Solution:
    def getSum(self, a: int, b: int) -> int:
        # return a + b # hehe
        # XOR finds a difference in bits
        # leftshift << to go to the next bit
        # & checks if both are 1

        # steps
        # while loop
        # check for carry over with &
        # then XOR
        # then shift 

        # o(1)

        k = 32
        while b and k:
            k-=1
            a, b = (a^b), (a & b) << 1
        if k==0:
            return a&0xFFFFFFFF
        return a
