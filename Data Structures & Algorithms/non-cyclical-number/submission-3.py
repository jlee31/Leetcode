class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        print(n)
        while n not in seen:
            # find the sum of the digits, then change n add to seen
            seen.add(n)
            tmp = str(n)
            tot = 0
            for char in tmp:
                tot += int(char) ** 2
            n = tot
            if tot == 1:
                return True
            print(n)

        return False

        # 19 - 1 + 81 = 82 n = 82 seen has 82 82 = 64 + 4 = 84