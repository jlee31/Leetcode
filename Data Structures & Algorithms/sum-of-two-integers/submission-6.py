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
        # https://algo.monster/liteproblems/371#code

        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        a = a & mask
        b = b & mask

        while b != 0:
            carry = ((a&b) << 1) & mask
            a = a^b
            b = carry
        
        if a > max_int:
            return ~(a ^ mask)
        else:
            return a
